from django import forms


class GenerateSummaryForm(forms.Form):
    tittle = forms.CharField(max_length=50)
    strr = forms.CharField(widget=forms.Textarea)

class ConvertCSVForm(forms.Form):
    file = forms.FileField()