from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Summary, 
	TypeOfStudy,
	DeviceType,
	DiseaseType,
	PatientGroup,
	ProcedureType
from ml_files.nlp import generate_summary
from .forms import GenerateSummaryForm
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User


from statistics import  mode
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import  PyPDF2
from PyPDF2 import PdfFileReader
import io


class RootView(TemplateView):
    template_name="summaryapp/landing.html"
       
class SummaryListView(LoginRequiredMixin, ListView):
	model = Summary
	template_name = "summaryapp/summary_list.html"
	context_object_name = 'summarys'
	ordering = ['-created_on']

@login_required
def generate_summary(request):
	if request.method == 'POST':
		form = GenerateSummaryForm(request.POST)
		if form.is_valid():
			#file = io.BytesIO(request.FILES['file'].read())
			# pdf_reader = PdfFileReader(file)
			# pdf_len = pdf_reader.getNumPages()
			# strr = ' '
			# for i in range(0,pdf_len):
			# 	page = pdf_reader.getPage(i)
			# 	strr += page.extractText()
			# file.close()
			strr = request.POST.get('strr')
			
			types_of_study=list(TypeOfStudy.objects.all().values('stemmed'))
			patient_group = list(PatientGroup.objects.all().values('stemmed'))
			procedure_type = list(ProcedureType.objects.all().values('stemmed'))
			device_type = list(DeviceType.objects.all().values('device_type_stemmed', 'device_maker_stemmed'))
			disease_type = list(DiseaseType.objects.all().values('stemmed'))
		    
		    	
			strr = strr.replace(',', ' ')
			strr = strr.replace('\n', ' ')
			strr=strr.lower()
			article_tokens=word_tokenize(strr)
			study_type="STUDY NOT FOUND"
			study_tokens=article_tokens
		    
			for word in study_tokens:
				if word in types_of_study:
					study_type=word
					break
			
			patient_token=article_tokens
			patients_list = []
			total_patient = 0
			l = len(patient_token)
		    
			for i in range(0,l-1):
				num=patient_token[i].strip()
				if num.isdigit() and (patient_token[i+1]=="patients"):
					patients_list.append(num)
			if(len(patients_list)>0):
				total_patient=mode(patients_list)
			else:
				total_patient="PATIENT NOT FOUND"
			ages_token = sent_tokenize(strr)
			age_value = ""
			for w in ages_token:
				word_tok=word_tokenize(w)
				flag1=0
				flag2=0
				for wo in word_tok:
					if wo=="mean":
						flag1=1
					if wo=="age":
						flag2=1
				if (flag1==1 and flag2==1):
					age_value = w
					break
			if age_value == "":
				age_value = "NO MEAN AGE FOUND"

		    ### Getting Device Type ###
			device_type_ans = ""
			device_maker_ans = ""
			device_type_token = word_tokenize(strr)

			for w in device_type_token:
				if w in device_type:
					device_type_ans = w
					break

			if device_type_ans == "":
				device_type_ans = "DEVICE TYPE NOT FOUND"
			else:
				device_type_ans = device_type_ans + " device"

			if device_maker_ans == "":
				device_maker_ans = "DEVICE MAKER NOT FOUND"



		    ### Getting The Indication ###

			indication_type_token = sent_tokenize(strr)
			indication_type_ans = ""
			for w in indication_type_token:
				if "indication" in w:
					indication_type_ans = indication_type_ans + w
			if indication_type_ans == "":
				indication_type_ans = "NO INDICATION FOUND"


		    ### Patient Group ###
			patient_grp="NO PATIENT GROUP FOUND"
			pat_grp_word_token=word_tokenize(strr)
		    
			for w in pat_grp_word_token:
				if w in patient_group:
					patient_grp=w
					break
			answer=" Summary: "+" This " +study_type +" study involves total "+total_patient +" Patients ."+ age_value +\
		    " who presented with DISEASE TYPE -- .All of these patients were treated with ",device_type_ans," from ",device_maker_ans+\
		    " While the "+device_type_ans+" is the excellent tool for these indications : "+indication_type_ans+" Patient Group : "+patient_grp+"...."
			
			tittle = request.POST.get('tittle')
		
			summary = Summary(tittle=tittle, detail=answer,author=request.user)
			summary.save()
			
			return redirect('summary-list')
	else:
		form = GenerateSummaryForm()
	return render(request, 'summaryapp/generate_summary.html', {'form': form})


