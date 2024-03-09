from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('home/', views.home2, name='home2'),
]

#supports any index/crypto/
urlpatterns = [
    path('quote/<str:asset>/', views.quote, name='quote'),
]
