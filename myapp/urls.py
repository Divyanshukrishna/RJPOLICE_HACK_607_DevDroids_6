from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.cybervision, name="cybervision"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('afterlogin/',views.afterlogin, name="afterlogin"),
    path('cameraperson/',views.cameraperson, name="cameraperson"),
    
    path('datasetpublic/',views.datasetpublic, name="datasetpublic"),
    
    path('chooseoption/',views.chooseoption, name="chooseoption"),
    path('camerapublic1/',views.camerapublic1, name="camerapublic1"),
    path('camerapublic2/',views.camerapublic2, name="camerapublic2"),
    path('camerapublic3/',views.camerapublic3, name="camerapublic3"),
    path('camerapublic4/',views.camerapublic4, name="camerapublic4"),
    
    path('datasetprivate/',views.datasetprivate, name="datasetprivate"),
    
    path('cameraprivate1/',views.cameraprivate1, name="cameraprivate1"),
    path('cameraprivate2/',views.cameraprivate2, name="cameraprivate2"),
    path('cameraprivate3/',views.cameraprivate3, name="cameraprivate3"),
    path('cameraprivate4/',views.cameraprivate4, name="cameraprivate4"),

    path('geotrack/',views.geotrack, name="geotrack"),

]

handler404 = 'myapp.views.error_404'