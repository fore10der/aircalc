from django import forms

class TestFileForm(forms.Form):
    file_input = forms.FileField(label="Выберите файл для загрузки в базу данных")