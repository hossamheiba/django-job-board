from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator
from .form import Applay_form
# Create your views here.

def job_list(requset):
    # context={'job_list':job.objects.all()}
    job_list=job.objects.all()
    paginator=Paginator(job_list,2)
    page_number=requset.GET.get("page")
    page_obj=paginator.get_page(page_number)
    context={"job_list":page_obj}
    return render(requset,'job/job_list.html',context)
    


def job_detail(requset,slug):
    job_detail=job.objects.get(slug=slug)
    if requset.method=="POST":
        form=Applay_form(requset.POST,requset.FILES)
        if form.is_valid():
           form.save()
    else:
        form=Applay_form()
    context={'job_detail':job_detail,'form':form}
    return render(requset,'job/job_detail.html',context)
    
    

