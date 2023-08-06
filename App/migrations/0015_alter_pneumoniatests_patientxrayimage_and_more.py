# Generated by Django 4.2 on 2023-07-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_patient_patientregdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pneumoniatests',
            name='patientXrayImage',
            field=models.ImageField(upload_to='./PN/Pneumonia'),
        ),
        migrations.AlterField(
            model_name='tuberculosistests',
            name='patientXrayImage',
            field=models.ImageField(upload_to='./TB/Tuberculosis'),
        ),
    ]