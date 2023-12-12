
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('setsession',views.setsession,name='setsession'),
    path('getsession',views.getsession,name='getsession'),
    path('delsession',views.delsession,name='delsession')
    # path('set',views.settestcookies,name='setsession'),
    # path('get',views.checktestcookies,name='getsession'),
    # path('del',views.deltestcookies,name='delsession')
]
