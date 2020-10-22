from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('ninjas', views.ninja),
    path('dojos', views.dojo),
    path('remove_1/<int:dojo_id>', views.remove_1)
]