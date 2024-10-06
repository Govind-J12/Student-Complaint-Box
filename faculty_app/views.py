from django.shortcuts import render,redirect
from student_app.models import *
from admin_app.models import *
from.models import*

# Create your views here.
    
def viewcomplaints(request):
    u_id=request.session['uid']
    if addfaculty.objects.filter(designation='hr',pk=u_id):
       data=complaintdetailss.objects.filter(complaintto='hr')
       return render(request,'fac_com_oh.html',{"res":data})
   
    elif addfaculty.objects.filter(designation='trainer',pk=u_id):
        data=complaintdetailss.objects.filter(complaintto='trainer')
        return render(request,'fac_com_oh.html',{"res":data})
    else:
        addfaculty.objects.filter(designation='operational head',pk=u_id)
        data=complaintdetailss.objects.filter(complaintto='operational head')
        return render(request,'fac_com_oh.html',{"res":data})
    return render(request,'fac_com_oh.html',{"res":data})

def faccomdelete(request,id):
    data=complaintdetailss.objects.get(pk=id)
    data.delete()
    return redirect(viewcomplaints)
    


def userack(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userdate = request.POST.get("userdate")
        useremail = request.POST.get("useremail")
        userackmsg = request.POST.get("userackmsg") 
        data=stdack(username=username,userdate=userdate,useremail=useremail,userackmsg=userackmsg)
        data.save()
    return render(request,'sendack.html')

def viewadminack(request):
    u_id=request.session['uemail']
    data=adminack.objects.filter(ackemail=u_id)
    return render(request,'view_admin_ack.html',{'res':data})


def facviewprofile(request):
    u_id=request.session['uid']
    data=addfaculty.objects.get(pk=u_id)
    return render(request,"fac_viewprofile.html",{'res':data})

def send_ack(request,id):
    data=complaintdetailss.objects.get(pk=id)
    return render(request,'sendack.html',{'res':data})
    
