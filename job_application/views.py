from django.shortcuts import render, redirect
from .form import ApplicationForm
from .models import ApplicationFormModel
from django.contrib import messages


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
            return redirect(request.META['HTTP_REFERER'])
    return render(request, "index.html")
