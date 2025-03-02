
from django.db import models

class HealthIndexRawData(models.Model):
    year = models.IntegerField()
    no_nurses = models.IntegerField()
    no_doctors = models.IntegerField()
    hospital_beds = models.IntegerField()
    no_clinics = models.IntegerField()
    no_hospitals = models.IntegerField()
    no_mobile_clinics = models.IntegerField()
    no_health_posts = models.IntegerField()
    infant_mortality = models.FloatField()
    life_expectancy = models.FloatField()
    tb_incidence = models.IntegerField()
    outpatient_visits = models.IntegerField()
    maternal_mortality = models.IntegerField()
    malaria_incidence = models.FloatField()
    inpatient_admissions = models.IntegerField()
    per_capita_expenditure = models.IntegerField()
    vaccinations_administered = models.IntegerField(null=True, blank=True)
    avg_waiting_time = models.FloatField(null=True, blank=True)
    emergency_response_time = models.FloatField(null=True, blank=True)
    hiv_incidence_rates = models.FloatField(null=True, blank=True)
    qaly = models.FloatField(null=True, blank=True)  # Quality Adjusted Life Years
    daly = models.FloatField(null=True, blank=True)  # Disability Adjusted Life Years

    def __str__(self):
        return f"Health Data {self.year}"
