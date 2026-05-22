
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.DBl, name='DBL'), 
    path('<int:racket_id>/', views.buy_racket, name='buy'),  
    path('racket_shop/',views.all_rackets, name='racket_shop'), 
    path('racket_shop/<int:racket_id>/', views.buy_racket, name='view_racket')
]
