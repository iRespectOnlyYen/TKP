from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def add(request):
    print(request)
    print()
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        result = num1 + num2
        return render(request, 'result.html', {'result': result})
    return render(request, 'add.html')
