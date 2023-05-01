from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import UploadedFile
from .forms import UploadFileForm
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            filename = file.name
            if UploadedFile.objects.filter(name=name).exists():
                return render(request, 'upload_file_confirm.html', {'name': name, 'file': file})
            else:
                uploaded_file = UploadedFile(name=filename, file=file)
                uploaded_file.save()
                messages.success(request, f'File "{filename}" has been uploaded.')
                return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})