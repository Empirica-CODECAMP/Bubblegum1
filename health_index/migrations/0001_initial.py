# Generated by Django 3.2.5 on 2025-02-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthIndexRawData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('no_nurses', models.IntegerField()),
                ('no_doctors', models.IntegerField()),
                ('hospital_beds', models.IntegerField()),
                ('no_clinics', models.IntegerField()),
                ('no_hospitals', models.IntegerField()),
                ('no_mobile_clinics', models.IntegerField()),
                ('no_health_posts', models.IntegerField()),
                ('infant_mortality', models.FloatField()),
                ('life_expectancy', models.FloatField()),
                ('tb_incidence', models.IntegerField()),
                ('outpatient_visits', models.IntegerField()),
                ('maternal_mortality', models.IntegerField()),
                ('malaria_incidence', models.FloatField()),
                ('inpatient_admissions', models.IntegerField()),
                ('per_capita_expenditure', models.IntegerField()),
                ('vaccinations_administered', models.IntegerField(blank=True, null=True)),
                ('avg_waiting_time', models.FloatField(blank=True, null=True)),
                ('emergency_response_time', models.FloatField(blank=True, null=True)),
                ('hiv_incidence_rates', models.FloatField(blank=True, null=True)),
                ('qaly', models.FloatField(blank=True, null=True)),
                ('daly', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
