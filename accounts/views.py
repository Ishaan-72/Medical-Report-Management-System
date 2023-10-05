from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Report
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def home(req):
    print(req.user.is_authenticated)
    # print(req.user.username)
    if(req.user.is_authenticated):
        mydata = Report.objects.filter(user=req.user).values()
        # print(mydata)
        return render(req,'home.html',context={'data':mydata})
    return render(req,'index.html')

def handlesignup(request):
    if request.method == 'POST':
        email=request.POST.get('emailsignup','default@user')
        confirmemail=request.POST.get('confirmemailsignup','default@user')
        pass1=request.POST.get('passwordsignup','1234')
        confirmpass=request.POST.get('confirmpasswordsignup','1234')
        username = email
        if (pass1!= confirmpass):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        if (email!= confirmemail):
             messages.error(request, " Email do not match")
             return redirect('/')
        myUser=User.objects.create_user(username,email,pass1)
        myUser.save()
        messages.success(request,"User created")
        return redirect('/')

    else:
        return HttpResponse('404-not-found')
    

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginemail=request.POST.get('loginemail')
        loginpassword=request.POST.get('loginpassword')
        loginusername=loginemail
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("reports/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found") 

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def reports(req):
    if req.user.is_anonymous:
        return redirect('/')
    print(req.user.is_authenticated)
    # print(req.user.username)
    if(req.user.is_authenticated):
        mydata = Report.objects.filter(user=req.user).values()
        # print(mydata)
        return render(req,'home.html',context={'data':mydata})

def postreport(request):
      if request.method=="POST":
            user=request.user
            patientname=request.POST.get('patientname')
            doctorname=request.POST.get('doctorname')
            reportdate=request.POST.get('reportdate')
            reportfile = request.FILES.get('reportfile') 
            # print(patientname)
            # print(doctorname)
            new_report=Report(patientname=patientname,doctorname=doctorname,reportdate=reportdate,image=reportfile,user=user)
            new_report.save()      
            # # print(request.POST['content'])
            # if(request.user.is_authenticated):
            # mydata = Report.objects.filter(user=request.user).values()
            # print(mydata)
            # return render(request,'home.html',context={'data':mydata})
            return redirect('/')
def getyear(self):
        return self.reportdate.year 
def userreport(req):
    return render(req,'user_reports.html',context={})
def about(req):
    return render(req,'about.html',context={})


def deletereport(req):
    if req.method=='POST':
        report_id=req.POST.get('report_id')
        report=Report.objects.get(id=report_id)
        # print(req.POST)
        report.delete()
        print(report_id)
        return redirect('/')
