from django.shortcuts import render

def greeting(request):
    if request.method == 'POST':
        selected_greeting = request.POST.get('greeting')
        selected_name = request.POST.get('name')
        selected_color = request.POST.get('color')
        return render(request, 'greeting.html', {'selected_greeting': selected_greeting, 'selected_name': selected_name, 'selected_color': selected_color})
    else:
        return render(request, 'greeting.html')