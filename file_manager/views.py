
# Create your views here.
from django.shortcuts import render
from .models import File

from .models import File, ExcelFile, Dashboard, Inflation
# def file_list(request):
#     files = File.objects.all()
#     return render(request, 'home_page.html', {'files': files})
def home_page(request):
    files = File.objects.all()
    return render(request, 'home_page.html', {'files': files})
     
     


def file_list(request):
    files = File.objects.all()
    return render(request, 'files.html', {'files': files})

def excel_files_list(request):
    excel_files = ExcelFile.objects.all()
    return render(request, 'excel_files.html', {'excel_files': excel_files})

def dashboard(request):
    images = Dashboard.objects.all()
    return render(request, 'dashboard.html', {'images': images})


def inflation_list(request):
    inflation_data = Inflation.objects.all().order_by('-year')
    return render(request, 'inflation.html', {'inflation_data': inflation_data})


def nhi_survey(request):
    return render(request, 'NHI_survey.html')


def nhi_summary(request):
    return render(request, 'NHIsummary.html')


def wagesummary(request):
    return render(request, 'wage.html')


def wagesurvey(request):
    return render(request, 'wagesurvey.html')


# def age_group_analysis(request):
#     return render(request, 'analysis.html')


def age_distribution_view(request):
    data = [
        {"age_group": "0-4", "males_percent": 50.2, "females_percent": 49.8},
        {"age_group": "5-9", "males_percent": 50.1, "females_percent": 49.9},
        {"age_group": "10-18", "males_percent": 50.5, "females_percent": 49.5},
        {"age_group": "15-19", "males_percent": 50.2, "females_percent": 49.8},
        {"age_group": "20-24", "males_percent": 49.1, "females_percent": 50.9},
        {"age_group": "25-29", "males_percent": 48.7, "females_percent": 51.3},
        {"age_group": "30-34", "males_percent": 48.7, "females_percent": 51.3},
        {"age_group": "35-39", "males_percent": 49.2, "females_percent": 50.8},
        {"age_group": "40-44", "males_percent": 49.5, "females_percent": 50.5},
        {"age_group": "45-49", "males_percent": 50.1, "females_percent": 49.9},
        {"age_group": "50-54", "males_percent": 48.4, "females_percent": 51.6},
        {"age_group": "55-59", "males_percent": 44.7, "females_percent": 55.3},
        {"age_group": "60-64", "males_percent": 43.2, "females_percent": 56.8},
        {"age_group": "65-69", "males_percent": 42.9, "females_percent": 57.1},
        {"age_group": "70-74", "males_percent": 42.3, "females_percent": 57.7},
        {"age_group": "75-79", "males_percent": 39.8, "females_percent": 60.2},
        {"age_group": "80-84", "males_percent": 37.8, "females_percent": 62.2},
        {"age_group": "85-89", "males_percent": 32.1, "females_percent": 67.9},
        {"age_group": "90-94", "males_percent": 29.9, "females_percent": 70.1},
        {"age_group": "95-99", "males_percent": 27.5, "females_percent": 72.5},
        {"age_group": "100+", "males_percent": 22.7, "females_percent": 77.3},
    ]

    return render(request, "analysis.html", {"data": data})

def alcohol_consumption(request):
    data = [
        {"country": "Botswana", "alcohol_consumption": 6, "population": 3},
        {"country": "China", "alcohol_consumption": 4, "population": 1400},
        {"country": "Japan", "alcohol_consumption": 6, "population": 126},
        {"country": "Malaysia", "alcohol_consumption": 1, "population": 33},
        {"country": "Peru", "alcohol_consumption": 5, "population": 33},
        {"country": "United Kingdom", "alcohol_consumption": 9, "population": 67},
    ]
    return render(request, 'alcohol_consumption.html', {'data': data})





def medical_inflation(request):
    data = [
        {"year": 2014, "medical_inflation": 15.6, "inflation_percentage": 3.7},
        {"year": 2015, "medical_inflation": 15.2, "inflation_percentage": 3.1},
        {"year": 2016, "medical_inflation": -1.5, "inflation_percentage": 3.0},
        {"year": 2017, "medical_inflation": 9.7, "inflation_percentage": 3.2},
        {"year": 2018, "medical_inflation": 4.2, "inflation_percentage": 3.5},
        {"year": 2019, "medical_inflation": 14.2, "inflation_percentage": 2.2},
        {"year": 2020, "medical_inflation": 6.9, "inflation_percentage": 2.2},
        {"year": 2021, "medical_inflation": 6.5, "inflation_percentage": 8.7},
        {"year": 2022, "medical_inflation": 16.3, "inflation_percentage": 12.4},
        {"year": 2023, "medical_inflation": 18.2, "inflation_percentage": 3.5},
        {"year": 2024, "medical_inflation": 12.5, "inflation_percentage": 4.2},
        {"year": 2025, "medical_inflation": 13.8, "inflation_percentage": 5.0},
        {"year": 2026, "medical_inflation": 11.5, "inflation_percentage": 4.5},
        {"year": 2027, "medical_inflation": 14.2, "inflation_percentage": 5.3},
        {"year": 2028, "medical_inflation": 12.9, "inflation_percentage": 4.9},
        {"year": 2029, "medical_inflation": 16.1, "inflation_percentage": 5.7},
        {"year": 2030, "medical_inflation": 13.7, "inflation_percentage": 5.2},
        {"year": 2031, "medical_inflation": 17.4, "inflation_percentage": 6.0},
        {"year": 2032, "medical_inflation": 15.2, "inflation_percentage": 5.5},
        {"year": 2033, "medical_inflation": 18.9, "inflation_percentage": 6.3},
    ]
    return render(request, 'medical_inflation.html', {'data': data})


def healthcare_metrics(request):
    return render(request, 'health_care_metrics.html')