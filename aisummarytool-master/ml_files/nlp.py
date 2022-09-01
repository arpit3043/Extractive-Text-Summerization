from statistics import  mode
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import  PyPDF2
from summaryapp.models import TypeOfStudy,DeviceType,DiseaseType,PatientGroup, ProcedureType
def generate_summary(str):
    types_of_study=list(TypeOfStudy.objects.values('stemmed'))
    patient_group = list(PatientGroup.objects.all().values('stemmed'))
    procedure_type = list(ProcedureType.objects.all().values('stemmed'))
    device_type= list(DeviceType.objects.all().values('device_type_stemmed', 'device_maker_stemmed'))
    disease_type= list(DiseaseType.objects.all().values('stemmed'))
    #types_of_studys = ["retrospective",
    #                  "randomized controlled trial",
    #                  "prospective",
    #                  "cohort",
    #                  "prospective observational",
    #                 "case control",
    #                  "control groups",
    #                  "meta-analysis",
    #                 "systematic review",
    #                 "controlled clinical trials",
    #                 "quantitative studies",
    #                 "qualitative studies",
    #                 "evaluation studies"
                      
    #patient_group = ["controlled",
     #                "randomized",
      #               "uncontrolled",
       #              "analyse"
                     
    #procedure_type = ["screw insertion",
     #                 "open reduction internal fixation",
      #                "percutaneous",
       #               "minimally invasive"]
    #device_type = ["active",
     #              "passive",
      #             "implantable",
       #            "non implantable",
        #           "cardiovascular",
         #          "diagnostic equipment",
          #         "treatment equipment",
           #        "life support equipment",
            #       "medical laboratory equipment"]
    strr = strr.replace(',', ' ')
    strr=strr.lower()
    article_tokens=word_tokenize(strr)
    
    ### Getting Study ###
    study_type="STUDY NOT FOUND"
    #study_tokens=article_tokens
    #for word in study_tokens:
      #  if word in types_of_study:
       #     study_type=word
        #    break
    li=[]
    for q in types_of_study:
        if q in strr:
            li.append(q)
    ans=max(li,key=len)
    study_type=ans
    ### Getting No. of patients ###

    patient_token = article_tokens
    patients_list = []
    total_patient = 0
    l = len(patient_token)
    for i in range(0, l - 1):
        num = patient_token[i].strip()
        if num.isdigit() and (patient_token[i + 1] == "patients"):
            patients_list.append(num)
    if(len(patients_list)>0):
        total_patient=mode(patients_list)
    else:
        total_patient="PATIENT NOT FOUND"

    ### Getting Mean Age ###
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


    ### Disease Type ###
    disease_type_="NO DISEASE FOUND"
    disease_type_word_token=word_tokenize(strr)
    for w in disease_type_word_token:
        if w in disease_type:
            disease_type_=w
            break

    ### Patient Group ###
    patient_grp="NO PATIENT GROUP FOUND"
    pat_grp_word_token=word_tokenize(strr)
    for w in pat_grp_word_token:
        if w in patient_group:
            patient_grp=w
            break
    answer="Summary: "+"This " +study_type +" study involves total " +total_patient + " Patients . "+ age_value +\
           "who presented with ",disease_type_ , "All of these patients were treated with ",device_type_ans," from ",device_maker_ans+\
           "While the "+device_type_ans+" is the excellent tool for these indications : "+indication_type_ans+" Patient Group : "+patient_grp+"...."
    title ="Test Title"

    return answer
