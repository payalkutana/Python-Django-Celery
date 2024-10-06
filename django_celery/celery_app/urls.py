from celery_app import views
from django.urls import path, include

urlpatterns = [
    path("home/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("result/<str:task_id>",views.result, name="result")
]
