from django import forms
from .models import ReportedFile

class DateInput(forms.DateInput):
    input_type = 'date'

class ReportedForm(forms.ModelForm):
    report_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': 'report_form_name_title', 'placeholder':'Report name'}))

    class Meta:
        model = ReportedFile
        fields = ['report_date_start','report_date_end']
        
        widgets = {
            'report_date_start': DateInput(attrs={'id': 'report_form_date_title', 'placeholder':'dd.mm.aaaa'}),
            'report_date_end': DateInput(attrs={'id': 'report_form_date_title', 'placeholder':'dd.mm.aaaa'}),
        }