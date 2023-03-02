from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from . models import *
import math, random
from django.core.files.storage import FileSystemStorage 
from django.contrib import messages



def index(request):
    return render(request,"home.html")

def image_data(request):
    if request.method == 'POST' :
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        img = request.FILES.get('img')
        pwd=request.POST.get('pwd')
        if Data.objects.filter(email=email).exists():
            messages.success(request,'EMAIL ALREADY EXISTS')
            return redirect('/')
        elif Data.objects.filter( mobile=mobile).exists():
            messages.error(request,'MOBILE NUMBER EXISTS')
            return redirect('/')
        else:
           
            Data.objects.create(name=name,mobile=mobile,pwd=pwd,img=img,email=email)
            messages.success(request,'successfully registered')
            return render(request,'login.html')
    # else:
    #     return render(request,'home.html')



def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        if Data.objects.filter(email=email).exists() and Data.objects.filter(pwd=pwd).exists():
             o=generateOTP()
             d=Data.objects.filter(email=email)
             print(d)
             send_mail('YOUR OTP IS FROM PRINCE WEBSITE',o,'checkmail187945@gmail.com',[email])
             return render(request,'verify.html',{'otp':o,'d':d})
        else:
            messages.error(request,'email or password not match')
            return render(request,'login.html')
    else:
        return render(request,'login.html')       
    
    
    
def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP
 
 
 
def delete(request,id):
    d=Data.objects.filter(id=id)
    d.delete()
    d=Data.objects.all()
    return render(request,'show.html',{'d':d})
    
 
 
 
 

def verifyotp(request):
    otp=request.POST['otp']
    ro=request.POST['o']
    name=request.POST['name']
    if otp == ro :
        messages.success(request,'WELCOME')
        d=Data.objects.all()
        return render(request,'show.html',{'name':name,'d':d})
    else:
        messages.error(request,'WRONG OTP PLEASE TRY AGAIN')
        return render(request,'verify.html')
    
def datashow(request):
    d=Data.objects.all()
    return render(request,'show.html',{'d':d})