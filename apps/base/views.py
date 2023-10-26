from django.shortcuts import render, redirect
from django.contrib import messages

from apps.base.models import Application
def index(request):
    title = "Codex Studio"
    return render(request, "index-twelve.html", locals())

def about(request):
    title = "О Codex Studio"
    return render (request,"about.html", locals())

def service(request):
    title = "Услуги Codex Studio"
    return render(request, "service.html")

def portfolio(request):
    title = "Портфолио Codex Studio"
    return render(request, "portfolio.html")

def contact(request):
    title = "Портфолио Codex Studio"
    if request.method == 'POST':
        user = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        print(user, email, number, message)
        
        if user and email and number:
            if not number.startswith("+996"):
                messages.info(request, "Номер должен начинаться с '+996'")
                return redirect('contact')
            elif Application.objects.filter(email=email).exists():
                messages.info(request, 'Почта уже занята')
                return redirect('signup')
            else:
                user = Application.objects.create(user=user, email=email, number=number, message=message)
                user.save()
                return redirect("/")
        else:
            messages.info(request, "Неправильный запрос. Попробуйте еще раз")
    return render(request, "contact.html", locals())
