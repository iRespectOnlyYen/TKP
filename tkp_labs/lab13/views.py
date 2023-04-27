from django.shortcuts import render

def update_text(request):
    animal = request.GET.get('animal', 'cats')
    return render(request, 'index.html', {'animal': animal})