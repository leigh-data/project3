from django.urls import path

from . import views

app_name = "menu"

urlpatterns = [
    path(route='', view=views.MenuDisplayView.as_view(), name="index")
]
