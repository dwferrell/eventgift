from django.urls import path
from . import views

app_name = 'purchases'
urlpatterns = [
    path('make_purchase/', views.make_purchase, name='make_purchase'),
]
