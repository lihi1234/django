
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('test', views.test),
    # path('get_all_images', views.getImages),
    # path('upload_image/',views.APIViews.as_view()),

]

