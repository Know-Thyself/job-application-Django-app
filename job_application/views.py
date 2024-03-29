from django.shortcuts import render, redirect
from .form import ApplicationForm
from .models import ApplicationFormModel
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.cleaned_data
            ApplicationFormModel.objects.create(**application)
            messages.success(
                request,
                f"Thank you for your interest, {application['first_name']}! Your application has been submitted successfully!",
            )
            message_body = f"Hello, {application['first_name']}!\nWe've recieved your job application and we will notify you the outcome of your application once it is processed.\nThank you for your interest!"
            email_message = EmailMessage(
                subject="Application Submission Confirmation",
                body=message_body,
                to=[application["email"]],
            )
            email_message.send()
            return redirect(request.META["HTTP_REFERER"])
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
