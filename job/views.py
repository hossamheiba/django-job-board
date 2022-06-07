from django.urls import reverse
from django.shortcuts import redirect, render
from .models import job
from django.core.paginator import Paginator
from .form import Applay_form, add_job
from django.contrib.auth.decorators import login_required
from .filters import job_filter
# Create your views here.


def job_list(requset):
    job_list = job.objects.all()
    my_filter=job_filter(requset.GET,queryset=job_list)
    job_list=my_filter.qs
    paginator = Paginator(job_list, 20)
    page_number = requset.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"job_list": page_obj,"my_filter":my_filter}
    return render(requset, 'job/job_list.html', context)

@login_required
def job_detail(requset, slug):
    job_detail = job.objects.get(slug=slug)
    
    if requset.method == "POST":
        form = Applay_form(requset.POST, requset.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
        form.save()
        return redirect(reverse("jobs:job_list"))
    
    else:
        form = Applay_form()
    context = {'job_detail': job_detail, 'form': form}
    return render(requset, 'job/job_detail.html', context)

@login_required
def add_jobs(requset):
    if requset.method == "POST":
        add = add_job(requset.POST, requset.FILES)
        if add.is_valid():
            myadd = add.save(commit=False)
            myadd.owner = requset.user
        add.save()
        return redirect(reverse("jobs:job_list"))

    else:
        add = add_job()
    context = {"add_job": job.objects.all(), "add": add}
    return render(requset, 'job/add_job.html', context)











