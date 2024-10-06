from django.shortcuts import render,redirect
from.models import *
from complaintbox.models import studentdetails
from student_app.models import *


# Create your views here.
def viewstudents(request):
    data=studentdetails.objects.all()
    return render(request,'view_students.html',{'res':data})

def ddelete(request,id):
    data=studentdetails.objects.get(pk=id)
    data.delete()
    return redirect(viewstudents)

def faculty(request):
    if request.method == "POST":
        designation = request.POST.get("designation")
        facultyname = request.POST.get("facultyname")
        facultyemail = request.POST.get("facultyemail")
        facultypassword = request.POST.get("facultypassword") 
        data=addfaculty(designation=designation,facultyname=facultyname,facultyemail=facultyemail,facultypassword=facultypassword)
        data.save()
    return render(request,'add_faculty.html')

def viewfaculty(request):
    data=addfaculty.objects.all()
    return render(request,'view_faculty.html',{'res':data})

def adminackno(request):
    if request.method == "POST":
        ackdate = request.POST.get("ackdate")
        ackdesignation = request.POST.get("ackdesignation")
        ackname = request.POST.get("ackname")
        ackemail = request.POST.get("ackemail") 
        ackmsg = request.POST.get("ackmsg") 
        data=adminack(ackdate=ackdate,ackdesignation=ackdesignation,ackname=ackname,ackemail=ackemail,ackmsg=ackmsg)
        data.save()
    return render(request,'admin_ack.html')


def fdelete(request,id):
    data=addfaculty.objects.get(pk=id)
    data.delete()
    return redirect(viewfaculty)

def admincomview(request):
    data=complaintdetailss.objects.all()
    return render(request,'admin_com_view.html',{'res':data})

def acdelete(request,id):
    data=complaintdetailss.objects.get(pk=id)
    data.delete()
    return redirect(admincomview)

def adminindex(request):
    return render(request,'admin_index.html')

def stdupdate(request,id):
    
    data=studentdetails.objects.get(pk=id)
    return render(request,'student_update.html',{'res':data})

def stdupdates(request,id):
    if request.method == "POST":
        studentphoto = request.FILES["studentphoto"]
        studentname = request.POST.get("studentname")
        studentemail = request.POST.get("studentemail")
        studentphone = request.POST.get("studentphone")
        studentpassword = request.POST.get("studentpassword") 
        data=studentdetails(studentphoto=studentphoto,studentname=studentname,studentemail=studentemail,studentphone=studentphone,studentpassword=studentpassword,id=id)
        data.save()
        return redirect(viewstudents)
    return render(request,'student_update.html')

def facupdate(request,id):
    data=addfaculty.objects.get(pk=id)
    return render(request,'update_faculty.html',{'res':data})

def facupdates(request,id):
    if request.method == "POST":
        designation = request.POST.get("designation")
        facultyname = request.POST.get("facultyname")
        facultyemail = request.POST.get("facultyemail")
        facultypassword = request.POST.get("facultypassword") 
        data=addfaculty(designation=designation,facultyname=facultyname,facultyemail=facultyemail,facultypassword=facultypassword,id=id)
        data.save()
        return redirect(viewfaculty)
    return render(request,'update_faculty.html')

    
    
    
    

    
