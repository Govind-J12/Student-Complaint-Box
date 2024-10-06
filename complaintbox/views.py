from django.shortcuts import render,redirect,HttpResponse
from . models import *
from admin_app.models import addfaculty
from django.contrib.auth import authenticate,login as authlogin
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def meetings(request):
    return render(request,'meetings.html')

def meetingdetails(request):
    return render(request,'meeting-details.html')

def complaintregister(request):
    return render(request,'complaint_register.html')

def register(request):
    if request.method == "POST":
        studentphoto = request.FILES["studentphoto"]
        studentname = request.POST.get("studentname")
        studentemail = request.POST.get("studentemail")
        studentphone = request.POST.get("studentphone")
        studentpassword = request.POST.get("studentpassword") 
        data=studentdetails(studentphoto=studentphoto,studentname=studentname,studentemail=studentemail,studentphone=studentphone,studentpassword=studentpassword,)
        data.save()
    return render(request,'register.html')


def login(request):
    studentemail = request.POST.get('studentemail')
    studentpassword  = request.POST.get('studentpassword') 
    facultyemail = request.POST.get('facultyemail')
    facultypassword = request.POST.get('facultypassword')
    if studentemail == 'admin@gmail.com' and studentpassword  =='admin':
        
        request.session['adminemail'] = studentemail
        request.session['admin'] ='admin'
        return render(request,'admin_index.html',{'status': 'Admin Login Success'})

    elif studentdetails.objects.filter(studentemail=studentemail,studentpassword=studentpassword).exists():
        studentdetailss=studentdetails.objects.get(studentemail=request.POST['studentemail'],studentpassword=studentpassword)
        if studentdetailss.studentpassword == request.POST['studentpassword']:
            request.session['uid'] = studentdetailss.id
            request.session['uname'] = studentdetailss.studentname
            request.session['uemail'] = studentemail
            request.session['user'] = 'user'
        return render(request,'student_landing.html', {'status': 'User Login Success'})
    else:
            return render(request, 'login.html', {'status': 'Failed'})
        
    return render(request,'login.html')


def faclogin(request):
    facultyemail = request.POST.get('facultyemail')
    facultypassword = request.POST.get('facultypassword')
    designation = request.POST.get('designation')
    if addfaculty.objects.filter(designation=designation,facultyemail=facultyemail,facultypassword=facultypassword).exists():
        addfacultyy=addfaculty.objects.get(facultyemail=request.POST['facultyemail'],facultypassword=facultypassword)
        if addfacultyy.facultypassword == request.POST['facultypassword']:
            request.session['uid'] = addfacultyy.id
            request.session['uname'] = addfacultyy.facultyname
            request.session['uemail'] = facultyemail
            request.session['user'] = 'user'
        return render(request,'faculty_landing.html', {'status': 'User Login Success'})
    else:
        return render(request,'faculty_login.html')
    
    return render(request,'faculty_login.html')

                
        


        
        
        
        
       
    

        



