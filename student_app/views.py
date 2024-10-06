from django.shortcuts import render,redirect
from . models import *
from complaintbox.views import *
from complaintbox. models import *
from faculty_app.models import *
# Create your views here.

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(complaintregister)

def viewprofile(request):
    u_id=request.session['uid']
    data=studentdetails.objects.get(pk=u_id)
    return render(request,"viewprofile.html",{'res':data})
    
def comregister(request):
    u_id=request.session['uid']
    if request.method == "POST":
        complaintto=request.POST.get("complaintto")
        date=request.POST.get("date")
        name=request.POST.get("name")
        email=request.POST.get("email")
        complaintmsg=request.POST.get("complaintmsg")
        data=complaintdetailss(userid=u_id,complaintto=complaintto,date=date,name=name,email=email,complaintmsg=complaintmsg,)
        data.save()
    return render(request,'complaint_form.html')

def mycomplaints(request):
    u_id=request.session['uid']
    data=complaintdetailss.objects.filter(userid=u_id)
    return render(request,'view_complaints.html',{'res':data})

def cdelete(request,id):
    data=complaintdetailss.objects.get(pk=id)
    data.delete()
    return redirect(mycomplaints)

def viewuserack(request):
    u_id=request.session['uemail']
    data=stdack.objects.filter(useremail=u_id)
    return render(request,'view_user_ack.html',{'res':data})
    
def home(request):
    return render(request,'student_landing.html')

def adelete(request,id):
    data=stdack.objects.get(pk=id)
    data.delete()
    return redirect(viewuserack)

def comupdate(request,id):
    data=complaintdetailss.objects.get(pk=id)
    return render(request,'update_complaint.html',{'res':data})

def comupdates(request,id):
    u_id=request.session['uid']
    if request.method == "POST":
        complaintto=request.POST.get("complaintto")
        date=request.POST.get("date")
        name=request.POST.get("name")
        email=request.POST.get("email")
        complaintmsg=request.POST.get("complaintmsg")
        data=complaintdetailss(userid=u_id,complaintto=complaintto,date=date,name=name,email=email,complaintmsg=complaintmsg,id=id)
        data.save()
        return redirect(mycomplaints)
    return render(request,'update_complaint.html')