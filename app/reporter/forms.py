from django import forms
from .models import ReportedFile

class ReportedForm(forms.ModelForm):
    report_name = forms.CharField(max_length=16)

    class Meta:
        model = ReportedFile
        fields = ['report_date_start','report_date_end']