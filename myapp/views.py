from django.shortcuts import redirect, render
from django.http import HttpResponse
from myapp.models import registrations
import smtplib as s
import random
from django.contrib import messages


def welcomepage(request):
    return render(request,"welcomepage.html")

def welcomepagesignin(request):
    return render(request,"signin.html")

def welcomepageverifying(request):
    if request.method=="POST":
        email = request.POST['email']
        if registrations.objects.filter(email=email).exists():
            messages.success(request,'Login First As Email Already Exist !!!')
            return redirect('welcomepagelogin')
        ob = s.SMTP("smtp.gmail.com",587)
        ob.starttls()
        '''enter email and password below'''
        ob.login("Enter Your email here","Email password here")
        Subject="Verification Code"
        code=random.randint(111111,999999)
        request.session['verifycode']=code
        request.session['email']=email
        request.session.modified=True
        message = "Subject:{}\n\n Verification code is :{}".format(Subject,code)
        '''enter sender email below'''
        ob.sendmail("Senders-Email-here",email,message)
        ob.quit()
    return render(request,"verifyemail.html",{'email':email})

def welcomepageconfirmation(request):
    if request.method=="POST":
        verifycode= int(request.POST['verifycode'])
        key=request.session.get('verifycode')
        if key==verifycode:
            email=request.session.get('email')
            request.session.clear()
            request.session.clear_expired()
            return render(request,"register1.html",{'email':email})
        else:
            request.session.clear()
            request.session.clear_expired()
            return render(request,"signin.html",{'warning':"Invalid Code!!!"})
    return render(request,"signin.html",{'warning':"Signin First"})

def welcomepageregister1(request,email):
    if(request.method=="POST"):
        password=request.POST['password']
        state=request.POST['state']
        city=request.POST['city']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        countrycode=request.POST['countrycode']
        phonenumber=request.POST['phonenumber']
        gender=request.POST['gender']
        obj= registrations(password=password,firstname=firstname,lastname=lastname,state=state,countrycode=countrycode,phonenumber=phonenumber,gender=gender,city=city,email=email)           
        obj.save()
        messages.success(request,'Record Saved Successfully!!!')
        return redirect('welcomepage')
    else:
        messages.success(request,'Register First!!!')
        return redirect('welcomepage')

def welcomepagelogin(request):
    return render(request,"login.html")

def userlogin(request):
    if request.method == "POST":
        password=request.POST['password']
        if password=="":
            messages.success(request,'Enter Password!!!')
            return redirect('welcomepagelogin')
        email=request.POST['email']
        if registrations.objects.filter(email=email).exists():
            record = registrations.objects.get(email=email)
            if record.password == password:
                messages.success(request,'Valid User!!!')
                return redirect('welcomepage')
            else:
                messages.success(request,'Invalid Password!!!')
                return redirect('welcomepagelogin')
        else:
            messages.success(request,'Email Not Exist SignIn First!!!')
            return redirect('welcomepage')
    else:
        messages.success(request,'Login First!!!')
        return redirect('welcomepage')

def forgotpass(request):
    return render(request,"forgotpassword.html")

def forgotpassword(request):
    if request.method=="POST":
        email=request.POST['email']
        if registrations.objects.filter(email=email).exists():
            ob = s.SMTP("smtp.gmail.com",587)
            ob.starttls()
            '''enter email and password below'''
            ob.login("Enter Your email here","Email password here")
            Subject="Verification Code"
            code=random.randint(111111,999999)
            request.session['verifycod']=code
            request.session['email']=email
            request.session.modified=True
            message = "Subject:{}\n\n Verification code is :{}".format(Subject,code)
            '''sender email in below line'''
            ob.sendmail("Sender-email-here",email,message)
            ob.quit()
            return redirect('forgotemailpassword')
        else:
            messages.success(request,'Email Not exist SignIn First!!!')
            return redirect('welcomepage')
    else:
        messages.success(request,'Register First!!!')
        return redirect('welcomepage')

def forgotemailpassword(request):
    email=request.session.get('email')
    return render(request,"forgotemailpassword.html",{'email':email})

def verifyforgotemailpassword(request):
    if request.method=="POST":
        verifycode = int(request.POST['verificationcode'])
        code=request.session.get('verifycod')
        if verifycode==code:
            return redirect('resetpassword')
        else:
            messages.success(request,'Invalid Code!!! ')
            return redirect('forgotpass')
    else:
        messages.success(request,"yehi zara hae!!!")
        return redirect('welcomepage')

def resetpassword(request):
    return render(request,"resetpassword.html")

def changepassword(request):
    if request.method=="POST":
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if confirmpassword == password:
            email=request.session.get('email')
            request.session.clear()
            request.session.clear_expired()
            record=registrations.objects.get(email=email)
            record.password=password
            record.save()
            messages.success(request,'Password Updated!!')
            return redirect('welcomepagelogin')
        else:
            request.session.clear()
            request.session.clear_expired()
            messages.success(request,'Password Not Update!!! or Confirmpassword and Password are not same!!')
            return redirect('welcomepagelogin')
    else:
        messages.success(request,'Register First!!')
        return redirect('welcomepage')