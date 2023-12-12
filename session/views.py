from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
# Create your views here.
def setsession(request):  
    request.session['name'] = 'python developer'
    return render(request,'setsession.html')

def getsession(request):
    # data = request.session.get('name') 
    if 'name' in request.session:
        data = request.session['name']
        keys = request.session.keys()
        return render(request,'getsession.html',{'data':data,'key':keys})

    else:
        return HttpResponse('your session is expireed..!')


def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'delsession.html')    


"""def settestcookies(request):
    request.session.set_test_cookie()
    return render(request,'settestcookies.html')

def checktestcookies(request):
    print(request.session.test_cookie_worked())
    return render(request,'checktestcookies.html')    

def deltestcookies(request):
    request.session.set_test_cookie()
    return render(request,'deltestcookies.html')    """