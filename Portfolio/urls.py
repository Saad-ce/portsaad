
from django.contrib import admin
from django.urls import path,include
from Portfolio import views
urlpatterns = [
    path("",views.index,name="index"),
    path("/contact", views.contact, name="contact"),
    path("/portfolio-details", views.portfoliodetails, name="portfolio-details"),
    path("/blog-single", views.blogsingle, name="blog-single"),
    path("/heartpredictor", views.heartpredictor, name="heartpredictor"),
    path("/resultheart", views.resultheart, name="resultheart"),

]
