from django import forms

class TestFileForm(forms.Form):
    file = forms.FileField(label="Выберите файл для загрузки в базу данных")