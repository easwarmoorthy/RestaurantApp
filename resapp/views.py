from django.shortcuts import render
from models import *
from django.http import HttpResponse
from forms import *
import oauth2 as oauth
import cgi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from social.apps.django_app.default.models import UserSocialAuth
from .models import UserProfile

def save_profile(backend, user, response, *args, **kwargs):
    users = UserProfile.objects.values('user__username')
    username = []
    print dir(user) , user.get_username(), user.is_active , user.is_authenticated()
    for x in users:
        username.append(str(x['user__username']))
    k = str(user)
    if k in username:
        print "Not Added"
    else:
        UserProfile.objects.create(user=user)


def view_res(request):
    user = None
    print request
    if request.user.is_authenticated():
        print "first"
        u = request.user
        #print type(u)
        user =  UserProfile.objects.get(user = u)
        #print type(user) , dir(user)
        #profile_name_search = UserProfile.objects.get(user = user)
        #user = UserProfile.objects.filter(user=profile_name_search.user.pk)
        print  user
        res_list = RestaurantModel.objects.all()
        paginator = Paginator(res_list, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        list2 =  []
        try:
            list1 = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            list1 = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            list1= paginator.page(paginator.num_pages)
        if user is not None:
            for k in user.restaurant.all():
                list2.append(k.id)
            if request.method == 'POST':
                interested = request.POST.getlist('checks[]')
                print interested
                user.restaurant.clear()
                for x in interested:
                    qwe = RestaurantModel.objects.get(id = x)
                    user.restaurant.add(qwe)
                list2 =  []
                for k in user.restaurant.all():
                    list2.append(k.id)
                context = {"list1":list1,"list2":list2}
                return render(request,"resapp/home.html",context)
        context = {"list1":list1,"list2":list2}
        return render(request,"resapp/home.html",context)
    else:
        #request.session['member']
        print "second"
        #list1 = RestaurantModel.objects.all()
        res_list = RestaurantModel.objects.all()
        paginator = Paginator(res_list, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        list2 =  []
        try:
            list1 = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            list1 = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            list1= paginator.page(paginator.num_pages)
        list2 =  []
        if request.method == 'POST':
            info = "Login using Twitter!!!"
            context = {"list1":list1,"list2":list2 , "info":info}
            return render(request,"resapp/home.html",context)
        if user is not None:
            for k in user.restaurant.all():
                list2.append(k.id)
            if request.method == 'POST':
                interested = request.POST.getlist('checks[]')
                print interested
                for x in interested:
                    qwe = RestaurantModel.objects.get(id = x)
                    user.restaurant.add(qwe)
                list2 =  []
                for k in user.restaurant.all():
                    list2.append(k.id)
                context = {"list1":list1,"list2":list2}
                return render(request,"resapp/home.html",context)
        context = {"list1":list1,"list2":list2}
        return render(request,"resapp/home.html",context)

def search_view(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        keyword = form.cleaned_data.get("keyword")
        list2 = RestaurantModel.objects.all().filter(city__contains = keyword)
        context = {"list2":list2}
        return render(request,"resapp/search.html",context)
    else:
        context = {"form":form}
        return render(request,"resapp/search.html",context)



# It's probably a good idea to put your consumer's OAuth token and
# OAuth secret into your project's settings.
consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
#access_token_url = 'https://api.twitter.com/oauth2/token'
# This is the slightly different URL used to authenticate/authorize.
authenticate_url = 'https://api.twitter.com/oauth/authenticate'

def twitter_login(request):
    # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    # Step 2. Store the request token in a session for later use.
    request.session['request_token'] = dict(cgi.parse_qsl(content))
    print content
    print request.session['request_token']
    # Step 3. Redirect the user to the authentication URL.
    authenticate_url="login/authenticated"
    url = "%s?oauth_token=%s" % (authenticate_url,
        request.session['request_token']['oauth_token'])

    return HttpResponseRedirect(url)


@login_required
def twitter_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')


def twitter_authenticated(request):
    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token']['oauth_token'],request.session['request_token']['oauth_token_secret'])
    print token
    #print request.GET['oauth_verifier']
    token.set_verifier(request.GET.get('oauth_verifier'))
    client = oauth.Client(consumer, token)
    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "GET")
    print resp,resp['status']
    print resp['date'],resp['status'],content
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response from Twitter.")

    """
    This is what you'll get back from Twitter. Note that it includes the
    user's user_id and screen_name.
    {
        'oauth_token_secret': 'IcJXPiJh8be3BjDWW50uCY31chyhsMHEhqJVsphC3M',
        'user_id': '120889797',
        'oauth_token': '120889797-H5zNnM3qE0iFoTTpNEHIz3noL9FKzXiOxwtnyVOD',
        'screen_name': 'heyismysiteup'
    }
    """
    access_token = dict(cgi.parse_qsl(content))

    # Step 3. Lookup the user or create them if they don't exist.
    try:
        user = User.objects.get(username=access_token['screen_name'])
    except User.DoesNotExist:
        # When creating the user I just use their screen_name@twitter.com
        # for their email and the oauth_token_secret for their password.
        # These two things will likely never be used. Alternatively, you
        # can prompt them for their email here. Either way, the password
        # should never be used.
        user = User.objects.create_user(access_token['screen_name'],
            '%s@twitter.com' % access_token['screen_name'],
            access_token['oauth_token_secret'])

        # Save our permanent token and secret for later.
        profile = Profile()
        profile.user = user
        profile.oauth_token = access_token['oauth_token']
        profile.oauth_secret = access_token['oauth_token_secret']
        profile.save()

    # Authenticate the user and log them in using Django's pre-built
    # functions for these things.
    user = authenticate(username=access_token['screen_name'],
        password=access_token['oauth_token_secret'])
    login(request, user)

    return HttpResponseRedirect('/')
