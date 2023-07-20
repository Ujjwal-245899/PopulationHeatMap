from django.shortcuts import render
import folium
from folium import plugins

from .models import Data
# Create your views here.
def map(request):
    # data=Data.objects.all()
    #data_list= Data.objects.values_list('latitude','longitude','population')
    #print(data_list)
    data_list=[[22.345,17.226,503],[56.22336,78.9090,5666]]
    #print(data_list)
    map1=folium.Map(location =[-40,40],zoom_start=2)
    #folium.Marker(location=[Data.latitude, Data.longitude], popup='Marker').add_to(map1)
    #map1.fit_bounds([[28.6273928, 77.1716954]])
    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)
    map1=map1._repr_html_()
    context={
        'map1':map1
    }
    return render(request, 'partials/base.html',context)
def refresh(request):
    return(request,'partials/nav.html')
# def contact(request):
#     return(request,'partials/map.html')
def test1(request):
    return render(request,"partials/test.html")

def about(request):
    return render(request,"partials/about.html")

def about_home(request):
    return render(request,"partials/test.html")
def base_home(request):
    return render(request,"partials/test.html")
def base_about(request):
    return render(request,"partials/about.html")

def Home_KnowYourMap(request):
    return render(request,"partials/knowyourmap.html")
def Home_Contact(request):
    return render(request,"partials/contact.html")

def about_Contact(rquest):
    return render(rquest,"partials/contact.html")
def contact_toabout(request):
    return render(request,"partials/about.html")
def contact_toReturntoMapPage(request):
    return render(request,"partials/base.html")
    
