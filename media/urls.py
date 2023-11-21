from django.urls import path
from .views import main,detail

urlpatterns = [
    path('',main),
    path('detaitl/<str:pk>',detail)
]
