# Generated by Django 4.0.4 on 2022-05-15 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_cateogry'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cateogry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.cateogry'),
            preserve_default=False,
        ),
    ]
