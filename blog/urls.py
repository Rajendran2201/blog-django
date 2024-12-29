from django.urls import path
from . import views # to access the index function


app_name = 'blog' # defining an app name, we gonna use this in reverse URL in views.py


urlpatterns = [
  path("", views.index, name="index"),
    # empty string "" represents thr root URL
    # calling the index file written in views file
    # name -> naming the path (used later)
  path("post/<str:slug>", views.detail, name="detail"),
  path("payment", views.payment, name="payment"),   
  path("delivery/<str:place_id>", views.delivery, name="delivery"),
  path("x_url", views.old_url_redirect, name="old_url"),
  path("new_url", views.new_url_view, name="new_url"),
  path("contact", views.contact_view, name="contact"),
  path("about", views.about_view, name="about")

]