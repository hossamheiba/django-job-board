from django.urls import path
from . import views

app_name="contact-us"
urlpatterns = [
    path("contact",views.contact,name="contact"),
    path("done",views.done,name="done")
]