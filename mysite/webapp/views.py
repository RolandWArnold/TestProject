from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    country = request.GET.get('country', '')
    if country:
        print(country)
    template = loader.get_template('webapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


#https://restcountries.eu/rest/v2/name/united?fields=name;capital

#https://restcountries.eu/rest/v2/all?fields=name;capital