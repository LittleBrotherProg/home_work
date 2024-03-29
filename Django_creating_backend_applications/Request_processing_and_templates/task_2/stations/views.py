from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    with open("data-398-2018-08-30.csv", "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [{"Name":row['Name'], "Street":row["Street"], "District":row["District"]} for row in reader]
    pagination = Paginator(data, 10)
    page = pagination.get_page(page_number)
    context = {
               "bus_stations":page, 
                "page": page
              }
    return render(request, 'stations/index.html', context)
