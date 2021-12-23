from django import forms
# Create your models here.


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField()
