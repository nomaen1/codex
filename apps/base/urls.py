from django.urls import path
from apps.base.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about, name='about'),
    path('services/', service, name='service'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]