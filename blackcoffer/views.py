from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Jsondatafile
# Create your views here.

def fetchData(fieldname):
    fieldname = Jsondatafile.objects.raw(f"SELECT * FROM blackcoffer_jsondatafile WHERE {fieldname} !=''")
    return len(fieldname)



def myChart(request):
    
    variables = [
        "intensity ",
        "likelihood",
        "relevance ",
        "year",
        "country ",
        "topic ",
        "region ",
    ]   
    listOfData = [
        fetchData('intensity'),
        fetchData('likelihood'),
        fetchData('relevance'),
        fetchData('end_year'),
        fetchData('country'),
        fetchData('topic'),
        fetchData('region'),        
    ]

    context = {
        "lables":variables,
        "dataset":listOfData,
    }    
    # return JsonResponse(chartData,safe=False)
    return render(request,'blackcoffer/index.html',context)
    
