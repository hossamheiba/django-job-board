from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

# django model field
JOB_TYPE = [
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
]

class job (models.Model):  # table
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    image=models.ImageField(upload_to="jobs/")
    experienc = models.IntegerField(default=1)
    cateogry = models.ForeignKey('Cateogry', on_delete=models.CASCADE)
    slug=models.SlugField(blank=True ,null=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Cateogry (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Applay (models.Model):
    job=models.ForeignKey(job,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    website=models.URLField()
    cv=models.FileField(upload_to="cv/")
    texteria=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


