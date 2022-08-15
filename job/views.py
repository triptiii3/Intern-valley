from distutils.log import error
from django.shortcuts import render
from .models import * 
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def user_login(request):
    error = ""
    if request.method == 'POST':
        f= request.POST['fname']
        l= request.POST['lname']
        e= request.POST['email']
        p= request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e, password=p)
            StudentUser.objects.create(user=user,type="student")
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'user_login.html',d)



def employerdel(request):
    return render(request, 'employerdel.html')

def employerdetail(request):
    return render(request, 'employerdetail.html')

def employerjobs(request):
    return render(request, 'employerjobs.html')

def employerlogout(request):
    return render(request, 'employerlogout.html')

def employerpage(request):
    return render(request, 'employerpage.html')

def employerprofile(request):
    return render(request, 'employerprofile.html')

def employerpw(request):
    return render(request, 'employerpw.html')

def employershortlist(request):
    return render(request, 'employershortlist.html')

def employersubmit(request):
    return render(request, 'employersubmit.html')

def candappjobs(request):
    return render(request, 'candappjobs.html')

def canddel(request):
    return render(request, 'canddel.html')

def candidatepage(request):
    return render(request, 'candidatepage.html')

def candlogout(request):
    return render(request, 'candlogout.html')
def candprofile(request):
    return render(request, 'candprofile.html')
def candpw(request):
    return render(request, 'candpw.html')

def candresume(request):
    return render(request, 'candresume.html')
def candshortjobs(request):
    return render(request, 'candshortjobs.html')
def canduser(request):
    return render(request, 'canduser.html')
def hirefreelancer(request):
    return render(request, 'hirefreelancer.html')



