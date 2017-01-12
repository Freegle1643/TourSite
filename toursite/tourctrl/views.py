# coding = utf-8

from .forms import *
from .models import *
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.db import transaction

# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            # print request.user.id
            return render(request, 'home.html' , {'currentuser':userobject})
    else:
        return render(request, 'home.html' , {})


# @csrf_protect
@transaction.atomic
def loginpage(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
    	       return HttpResponseRedirect('../home')
    elif request.method == 'POST':
        username = request.POST.get('username')
       	password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            # User seesion will expiry after a day, which is 86400 sec
            request.session.set_expiry(86400)
            return HttpResponseRedirect('../home')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

@csrf_protect
@transaction.atomic
def registerpage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uico = '/static/res/images/dico.jpg'
            username = form.cleaned_data['username']
            password = password=form.cleaned_data['password1']
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            Touruser.objects.create(user = user,
            utag=form.cleaned_data['utag'], usign=form.cleaned_data['usign'], uico=uico
            )
            newUser=auth.authenticate(username=username,password=password)
            print user.date_joined
            auth.login(request,newUser)
            return HttpResponseRedirect('../home/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'register.html',
    variables,
    )

@login_required(login_url='../login/')
def logoutfunction(request):
    auth.logout(request)
    return HttpResponseRedirect('../login/')

# @login_required(login_url='../login/')
def destination(request,destid):
    destresult = Tourdest.objects.all().filter(did=destid)
    tripresult = Tourtrip.objects.all().filter(tdest=destid)
    spotresult = Tourspot.objects.all().filter(sdest=destid)
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            return render(request, 'destination.html', {'destresult':destresult,'tripresult':tripresult,'spotresult':spotresult, 'currentuser':userobject})
    return render(request, 'destination.html', {'destresult':destresult,'tripresult':tripresult,'spotresult':spotresult})

# @login_required(login_url='../login/')
def forum(request):
    alljournal = Tourjournal.objects.all()
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            # print request.user.id
            return render(request, 'forum.html' , {'currentuser':userobject,'alljournal':alljournal})
    return render(request, 'forum.html' , {'alljournal':alljournal})

# @login_required(login_url='../login/')
def triplist(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            # print request.user.id
            return render(request, 'triplist.html' , {'currentuser':userobject})
    return render(request, 'triplist.html' , {})

# @login_required(login_url='../login/')
def trip(request,tripid):
    thistrip = Tourtrip.objects.all().filter(tid=tripid)
    content = thistrip[0].ttrip
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            return render(request, 'trip.html', {'currentuser':userobject, 'thistrip':thistrip,'content':content})
    return render(request, 'trip.html', {'thistrip':thistrip,'content':content})

# @login_required(login_url='../login/')
def journal(request,jjid):
    thisjournal = Tourjournal.objects.all().filter(jid=jjid)
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            return render(request, 'journal.html' , {'currentuser':userobject,'thisjournal':thisjournal})
    return render(request, 'journal.html', {'thisjournal':thisjournal})

@login_required(login_url='../login/')
def editjournal(request):
    if request.user.is_staff:
        return HttpResponseRedirect('../admin')
    else:
        return render(request, 'journaledit.html' , {})

@login_required(login_url='../login/')
def addjournal(request):
    if request.user.is_staff:
        return HttpResponseRedirect('../admin')
    else:
    # getinfo = Tourjournal.objects.all()

    # getuser = Touruser.objects.all()
    # print(getuser[0].uid)

        if request.is_ajax():
            if request.method == 'POST':
                print ('come to ajax...')
                print (request.user.id)
                #  print ("come into ajax! " + request.body)
                # newrecord = Tourjournal.objects.create(jname='Test', jcontent=request.body, juser_id=request.user.id)

                # we use this way to solve the problem of foreign key instead of Tourjournal.objects.create()
                d1 = Touruser.objects.get(user=request.user.id)
                u1 = Tourjournal(jname=request.POST['jname'], jcontent=request.POST['jhtml'], jdescrip=request.POST['jdescrip'],jtag=request.POST['jtag'],juser=d1,jcover="/static/res/images/rf1.jpg")
                # save in database
                print (u1)
                u1.save()

        return HttpResponseRedirect('../personal')
        # return HttpResponse("OK")

@login_required(login_url='../login/')
def personal(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            tuser = Touruser.objects.get(user=request.user.id)
            myjournal = Tourjournal.objects.all().filter(juser = tuser)
            return render(request, 'user.html' , {'currentuser':userobject, 'myjournal':myjournal})

@login_required(login_url='../login/')
def profile(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            return render(request, 'userprofile.html' , {'currentuser':userobject})

@login_required(login_url='../login/')
def editprofile(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            return render(request, 'userprofileedit.html' , {'currentuser':userobject})

def aboutpage(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            # print request.user.id
            return render(request, 'about.html' , {'currentuser':userobject})
    else:
        return render(request, 'about.html' , {})

def linkWechat(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            # print request.user.id
            return render(request, 'about.html' , {'currentuser':userobject})
    else:
        return render(request, 'linkWechat.html' , {})

def aboutTour(request):
        if request.user.is_authenticated():
            if request.user.is_staff:
                return HttpResponseRedirect('../admin')
            else:
                userobject = Touruser.objects.all().filter(user=request.user.id)
                # print request.user.id
                return render(request, 'about.html', {'currentuser': userobject})
        else:
            return render(request, 'aboutTour.html', {})


def member(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'about.html', {'currentuser': userobject})
    else:
        return render(request, 'member.html', {})


def contact(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'about.html', {'currentuser': userobject})
    else:
        return render(request, 'contact.html', {})