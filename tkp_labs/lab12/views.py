import calendar
from datetime import datetime
from django.shortcuts import render

def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month
    month_calendar = calendar.monthcalendar(year, month)
    context = {
        'month_calendar': month_calendar,
        'current_year': year,
        'current_month': month,
        'current_day': now.day,
    }
    return render(request, 'calendar.html', context)