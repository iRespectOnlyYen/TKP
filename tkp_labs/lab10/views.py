from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            # Проверяем, загружен ли уже файл с таким именем
            if UploadedFile.objects.filter(file__exact=file.name).exists():
                return render(request, 'upload_file.html', {'form': form, 'file_exists': True})
            else:
                uploaded_file = UploadedFile(file=file)
                uploaded_file.save()
                return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})