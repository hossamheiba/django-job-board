# Generated by Django 4.0.4 on 2022-05-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_job_الاسم_applay'),
    ]

    operations = [
        migrations.AddField(
            model_name='applay',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
