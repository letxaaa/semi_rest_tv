from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('validate', views.validate),
    path('shows', views.dash),
    path('shows/new', views.new),
    path('shows/<int:show_id>', views.show),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/delete', views.delete),
    
]