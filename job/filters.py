import django_filters
from . models import job

class job_filter(django_filters.FilterSet):
    
     title=django_filters.CharFilter(lookup_expr="icontains")
     description=django_filters.CharFilter(lookup_expr="icontains")
     experienc=django_filters.CharFilter(lookup_expr="icontains")
     class Meta:
         model=job
         fildes="__all__"
         exclude=["owner","published_at","vacancy","salary","image","slug"]
    

