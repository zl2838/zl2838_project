from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.all_pets),
    path('<int:pet/',views.pet_details,name='34'),


]
