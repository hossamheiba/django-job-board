# Generated by Django 4.0.4 on 2022-05-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='jobs/'),
        ),
    ]
