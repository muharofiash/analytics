from django.shortcuts import render
from .models import *
from django.db.models import Avg, Max, Min
from datetime import datetime, timedelta
from django.utils import timezone
import statistics


# Create your views here.
def hr_detail(request, unit_id):
    hr_min = HeartRate.objects.filter(unit_id=unit_id).aggregate(Min('heart_rate'))
    hr_min = hr_min['heart_rate__min']
    hr_avg = HeartRate.objects.filter(unit_id=unit_id).aggregate(Avg('heart_rate'))
    hr_avg = round(hr_avg['heart_rate__avg'], 2)
    hr_max = HeartRate.objects.filter(unit_id=unit_id).aggregate(Max('heart_rate'))
    hr_max = hr_max['heart_rate__max']
    hrs = HeartRate.objects.filter(unit_id=unit_id)

    hr_data = []
    count = 0
    chart = [[] for _ in range(441)]
    for hr in hrs:
        hr_data.append(hr.heart_rate)
        chart[count].append(count)
        chart[count].append(hr.heart_rate)
        count += 1  
    hr_median = round(statistics.median(hr_data), 2)
    hr_mode = statistics.mode(hr_data)
    hr_stdev = round(statistics.stdev(hr_data), 2)
    hr_var = round(statistics.variance(hr_data), 2)

    context = {
        'unit_id': unit_id,
        'hr_min': hr_min,
        'hr_avg': hr_avg,
        'hr_max': hr_max,
        'hr_median': hr_median,
        'hr_mode': hr_mode,
        'hr_stdev': hr_stdev,
        'hr_var': hr_var,
        'chart': chart
    }
    return render(request, 'uas/detail.html', context)

def hr_predict(unit_id, amount):
    limit = 1
    while limit <= amount:
        akhir = HeartRate.objects.filter(unit_id=unit_id).aggregate(Max('timestamp'))
        akhir = akhir['timestamp__max']
        awal = akhir - timedelta(minutes=amount)
        hr_count = 0
        count = 0
        while awal <= akhir:
            try:
                hr = HeartRate.objects.get(timestamp=awal)
                hr_count += hr.heart_rate  
                count += 1
            except:
                pass
            awal += timedelta(minutes=1)
        hr_avg = round(hr_count / count) 
        hr = HeartRate.objects.create(unit_id=unit_id, heart_rate=hr_avg, timestamp=(akhir + timedelta(minutes=1)), sync_time=timezone.now())
        limit += 1
    print("Heart rate prediction success")    

def hr_status(unit_id):
    awal = HeartRate.objects.filter(unit_id=unit_id).aggregate(Min('timestamp'))
    awal = awal['timestamp__min']
    akhir = HeartRate.objects.filter(unit_id=unit_id).aggregate(Max('timestamp'))
    akhir = akhir['timestamp__max']
    while awal <= akhir:
        try:
            hr = HeartRate.objects.get(timestamp=awal)
            if hr.heart_rate <= 80 and hr.heart_rate >= 60:
                hr.status = "Normal"
            elif hr.heart_rate < 60:
                hr.status = "Bradycardia"
            else:
                hr.status = "Thacycardia"
            hr.save()  
        except:
            pass
        awal += timedelta(minutes=1)
    print("Heart rate status success")




