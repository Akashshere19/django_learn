from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setcookies(request):
    response = render(request,'setcookies.html')
    response.set_cookie('name','python developer...!',expires=datetime.utcnow()
                         +timedelta(days=2)) # max_age=60*60*24*10 second*minute*hours*days
    print(response.cookies)
    return response
def getcookies(request):
    # name = request.COOKIES['name']  #suppose cookies not set then gives error unknown key
    name =request.COOKIES.get('name') # suppose cookies not set then give none value
    print(name)
    return render(request,'getcookies.html',{'data':name})

def delcookies(request):
    response = render (request,'delcookies.html')
    response.delete_cookie('name')
    return response