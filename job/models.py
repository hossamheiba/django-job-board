from django.db import models
# Create your models here.

# django model field
JOB_TYPE=[
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
]
class job (models.Model): # table
    title=models.CharField(max_length=100) 
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.CharField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experienc=models.IntegerField(default=1)
