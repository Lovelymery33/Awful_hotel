from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('apartament/<int:apartament_id>/', views.apartament_page, name='apartament_page'),
]