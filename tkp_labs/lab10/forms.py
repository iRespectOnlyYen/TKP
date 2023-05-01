from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file']

    def clean_name(self):
        name = self.cleaned_data['name']
        if UploadedFile.objects.filter(name=name).exists():
            self.instance = UploadedFile.objects.get(name=name)
        return name