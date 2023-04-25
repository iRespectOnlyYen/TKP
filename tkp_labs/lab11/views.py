from django.shortcuts import render
import math

def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        elif operation == 'sin':
            result = math.sin(num1)
        elif operation == 'cos':
            result = math.cos(num1)
        elif operation == 'tan':
            result = math.tan(num1)
        elif operation == 'asin':
            result = math.asin(num1)
        elif operation == 'acos':
            result = math.acos(num1)
        elif operation == 'atan':
            result = math.atan(num1)
        else:
            result = 0
        return render(request, 'calculator.html', {'result': result})
    else:
        return render(request, 'calculator.html')