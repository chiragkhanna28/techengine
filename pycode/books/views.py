from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from books.models import Book,Author
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from ratings.models import Ratings
from django.db import models
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




def index1(request):#this view is used for creating front end(user login,admin login,new user register here)
    return render(request, 'index.html')


def register(request):#this view is used for registering the new user
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('register1.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def user_login1(request):#this view is used to provide log-in activity to a registered user
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/search_form/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)




def search_form(request):#this view is used for submitting various queries entered by user
    return render(request, 'search_form1.html')


def search(request):#this view is used for searching whether the book is available or not
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return render(request, 'search_form1.html', {'error': True})




def latest1(request):#this view is used for retrieving the latest books
    books = Book.objects.order_by("-publication_date")[0:5]
    return render(request, 'search_results2.html',
            {'books': books})


def latest(request):#this view is used for retrieving the author's latest books
    a=request.GET['firstname']
    b=request.GET['secondname']
    c=Author.objects.filter(first_name=a,last_name=b)
    d=Book.objects.filter(authors=c)
    e=d.order_by('publication_date')[0:3]
    return render(request,'search_results1.html',{'books':e,'firstname':a,'secondname':b})    
              
def rate(request):#this view is used for rating the books
    a=request.GET['rate1']
    b=request.GET['rate2']
    u=User.objects.get(username=request.user)
    books1=Book.objects.get(title=a)
    books1.ratings.rate(user=u,score=b)
    return render(request,'rate1.html',{'books':books1,'rate':b})

def popular(request):#this view is used for retrieving the latest books
    a=Book.ratings.order_by_rating()[0:5]
    return render(request,'popular1.html',{'books':a})


