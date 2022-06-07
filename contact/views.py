from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from.models import Info
# Create your views here.


def contact(requset):
    my_info = Info.objects.first()
    if requset.method == "POST":
        subject = requset.POST.get('subject')
        email = requset.POST.get('email')
        message = requset.POST.get('message')
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            # fail_silently=False,
            )
        return redirect(reverse("contact-us:done"))
    return render(requset, "contact/contact.html", {"my_info": my_info})

def done(requset):
    return render(requset, "contact/done.html",)

