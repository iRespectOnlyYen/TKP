from django.shortcuts import render
from .forms import FileForm
from django.shortcuts import render, redirect

from .models import File

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = FileForm()
    files = File.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})