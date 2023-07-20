from django.urls import path
from . import views


urlpatterns =[
    path('',views.test1,name='mapdikhega'),
     path('refresh/',views.refresh, name='refresh'),
     path('HeatMap/',views.map,name='map'),
     path('about/',views.about, name ='about'),
     path('about_home/',views.about_home,name='Main'),
     path('base_home/',views.base_home,name='Main'),
     path('base_about/',views.about,name='about'),
     #from main /Home page
     path('KnowUrMap/',views.Home_KnowYourMap,name='MapDetails'),
     path('contact/',views.Home_Contact,name='ContactPage'),
     #from about page
     path('contact/',views.about_Contact,name='ContactPage'),
     #from contactpage
     path('about/',views.contact_toabout,name="AboutPage"),
     path('MaDetails/',views.contact_toReturntoMapPage,name="Map"),
    #  path('contact/',views.contact,name='contact'),
     
]