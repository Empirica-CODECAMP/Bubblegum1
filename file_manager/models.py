from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255, unique=True)  # File name
    file = models.FileField(upload_to='uploads/')  # Upload path
    description = models.TextField(blank=True, null=True)  # Optional description
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically set upload date

    def __str__(self):
        return self.name


class Dashboard(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='research_images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  


class ExcelFile(models.Model):
    name = models.CharField(max_length=255, unique=True)  
    file = models.FileField(upload_to='excel_uploads/', help_text="Upload an Excel file (.xls, .xlsx)")  
    description = models.TextField(blank=True, null=True)  
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
    
    
class Inflation(models.Model):
    year = models.PositiveIntegerField(unique=True)
    bpmos_medical_inflation = models.DecimalField(max_digits=5, decimal_places=2, help_text="Enter BPMOS Medical Inflation (%)")
    general_inflation = models.DecimalField(max_digits=5, decimal_places=2, help_text="Enter General Inflation (%)")

    def __str__(self):
        return f"Inflation Data - {self.year}"
    
    