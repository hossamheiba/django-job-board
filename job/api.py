from .serializer import JobSerializer
from .models import job
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def API(requset):
    all_job=job.objects.all()
    data=JobSerializer(all_job,many=True).data
    return Response({"data":data})


@api_view(['GET'])
def API_detail(requset,id):
    job_detail_api=job.objects.get(id=id)
    data=JobSerializer(job_detail_api).data
    return Response({"data":data})