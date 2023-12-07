
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('setcookies',views.setcookies,name='setcookies'),
    path('getcookies',views.getcookies,name='getcookies'),
    path('delcookies',views.delcookies,name='delcookies')

]
