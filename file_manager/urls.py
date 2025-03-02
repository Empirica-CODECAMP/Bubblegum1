from django.urls import path
from .views import  home_page
from .views import *
from . import views 
urlpatterns = [
    # path('', file_list, name='file-list'),
    path('',home_page,name='home'),
    path('files/', file_list, name='file_list'),
    path('excel-files/', excel_files_list, name='excel_files_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('inflation/', inflation_list, name='inflation_list'),
    path('nhi/survey/', views.nhi_survey, name='nhi_survey'),
    path('nhi/summary/', views.nhi_summary, name='nhi_summary'),
    path('wage/summary/', views.wagesummary, name='wagesummary'),
    path('wage/survey/', views.wagesurvey, name='wagesurvey'),
    path('age-group-analysis/', views.age_distribution_view, name='age_group_analysis'),
    path('alcohol-consumption/', views.alcohol_consumption, name='alcohol_consumption'),
    path('medical-inflation/', views.medical_inflation, name='medical_inflation'),
     path('metrics/', views.healthcare_metrics, name='healthcare_metrics'),
    
]



