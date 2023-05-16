from. import views
from django.urls import path

urlpatterns = [

    #path('',views.demo,name='demo'),
   # path('about/',views.about, name='about'),
   # path('contacts/',views.contacts,name='contacts')
     path ('',views.home,name='home'),
   #path('add/',views.addition,name='addition')
    # path('',views.team,name='team'),
]
