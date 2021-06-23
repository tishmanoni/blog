from django.contrib import admin
from django.urls import path
from . import views


app_name = "blog"


urlpatterns = [
    # path("home", views.home, name="home")
    path("", views.postlist, name ="bloglist"),
    path("<int:year>/<int:month>/<int:day>/<slug>/", views.postdetail , name="post_detail")
    
]
