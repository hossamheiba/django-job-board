from django.urls import path
from . import views
from .import api

app_name="job"
urlpatterns = [
    path("job_list",views.job_list,name="job_list"),
    path("add_job",views.add_jobs,name="add_job"),
    path("<str:slug>",views.job_detail,name="job_detail"),
    
    #API
    path("api/list",api.API,name="api"),
    path("api/list/<str:id>",api.API_detail,name="api"),
       
]
