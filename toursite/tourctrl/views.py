# -*- coding:UTF-8 -*-

from __future__ import print_function
from .forms import *
from .models import *
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from django.template import RequestContext
from django.db import transaction
from PIL import Image, ImageFile


import sys
sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf8')
from qcloudapi_sdk_python.demo import *
from toursite.settings import *

# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    alldest = Tourdest.objects.all()
    alltrip = Tourtrip.objects.all()
    alljournal = Tourjournal.objects.all()

    # print alldest
    # print (alldest.count())  # 7

    # upload the database information to the yunsou

    # print ('uploading')
    #
    # for x in range(alldest.count()):
    #     # print (alldest[++x].did, alldest[++x].dname, alldest[++x].dinfo)
    #      upload1(alldest[++x].did, alldest[++x].dname, alldest[++x].dinfo)
    #
    # print ('uploaded destination')
    #
    # for x in range(alltrip.count()):
    #      upload2(alltrip[++x].tid, alltrip[++x].tdays, alltrip[++x].tname,alltrip[++x].tdescrip,alltrip[++x].tpeople,alltrip[++x].tdest)
    #
    # print ('uploaded trip')
    #
    # for x in range(alljournal.count()):
    #      upload3(alljournal[++x].jid, alljournal[++x].jname, alljournal[++x].jtag)
    #
    # print ('uploaded journal')

    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
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
            # print user.date_joined
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
            tuser = Touruser.objects.get(user=request.user.id)
            myjournal = Tourjournal.objects.all().filter(juser = tuser)
            return render(request, 'userprofile.html' , {'currentuser':userobject, 'myjournal':myjournal})

@login_required(login_url='../login/')
def editprofile(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user = request.user.id)
            tuser = Touruser.objects.get(user=request.user.id)
            myjournal = Tourjournal.objects.all().filter(juser = tuser)
            return render(request, 'userprofileedit.html' , {'currentuser':userobject, 'myjournal':myjournal})

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
                return render(request, 'aboutTour.html', {'currentuser': userobject})
        else:
            return render(request, 'aboutTour.html', {})


def member(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'member.html', {'currentuser': userobject})
    else:
        return render(request, 'member.html', {})


def contact(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'contact.html', {'currentuser': userobject})
    else:
        return render(request, 'contact.html', {})

def feature_south(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'feature_south.html', {'currentuser': userobject})
    else:
        return render(request, 'feature-south.html', {})

def feature_north(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'feature_north.html', {'currentuser': userobject})
    else:
        return render(request, 'feature-north.html', {})

def customize(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('../admin')
        else:
            userobject = Touruser.objects.all().filter(user=request.user.id)
            # print request.user.id
            return render(request, 'custom.html', {'currentuser': userobject})
    else:
        return render(request, 'custom.html', {})

def yunsou(request):
    if request.is_ajax():
        if request.method == 'POST':
            print ('come to yunsou ajax...')
            print (request.POST['searchTarget'])
            target = request.POST['searchTarget']
            # use yunsou to search searchTarget
            htmlcode = searchall(target)
    return HttpResponse(htmlcode)

            # use yunsou to search searchTarget
            # ddifExist = searchall(target)['destin']
            # ttifExist = searchall(target)['trip']
            # jjifExist = searchall(target)['jouurnal']
            #
            # if ddifExist: # no result
            #     ddresult = 'No Result'
            # else:
            #     ddresult = searchall(target)['destin'][0]['dname']
            #
            # if ttifExist:
            #     ttresult = 'No Result'
            # else:
            #     ttresult = searchall(target)['trip']['tname']
            #
            # if jjifExist:
            #     jjresult = 'No Result'
            # else:
            #     jjresult = searchall(target)['jouurnal']['jname']

        # return HttpResponse({'ddresult':ddresult},{'ttresult':ttresult},{'jjresult':jjresult})

# try to do image upload
def ImageUpload(request):

        if request.POST == None:
            return HttpResponse("error|uplode failure")
        else:
            # correct way to get object
            print (request.FILES['wangEditorH5File'])
            myfile = request.FILES['wangEditorH5File']
            # correct way to get object's name
            print(request.FILES['wangEditorH5File'].name)
            filename = request.FILES['wangEditorH5File'].name

            # save the image and back url
            parser = ImageFile.Parser()
            for chunk in myfile.chunks():
                parser.feed(chunk)
            img = parser.close()

            print ('img is')
            print(img)

            # image can go to media directory
            name = '%s\/%s' % (MEDIA_ROOT, myfile.name)
            img.save(name)

            imgUrl = "http://localhost:8000/media/" + filename
            return HttpResponse(imgUrl)

         # print(request.POST['files'])
         # print(request.POST.files[0])

         # myfile = request.files['myFileName']
         # if myfile == None:
         #     return HttpResponse('Server error!')
         # else:
         #      return HttpResponse('Success upload')
