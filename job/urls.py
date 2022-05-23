from django.urls import path
from . import views

app_name="job"
urlpatterns = [
    path("job_list",views.job_list,name="job_list"),
    path("<str:slug>",views.job_detail,name="job_detail")
]