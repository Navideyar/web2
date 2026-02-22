from django.urls import path
from core.views import *

urlpatterns = [
    path ('home', index_view ),
    path ('about' , about_view),
    path('contact', contact_view)
]
