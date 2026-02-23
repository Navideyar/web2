from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

def index_view(request):
    # این تابع به صورت خودکار HttpResponse برمی‌گرداند
    return render(request, 'index.html')

def about_view (request):
    return render ( request , 'website/about.html')

def contact_view (request):
    return render ( request , 'contact.html')