# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from users.forms import *
from django.contrib.auth import *

from django.template import Context, loader
from users.models import *
import json


from django.contrib.auth.models import User

def index(request):
	#latest_user_list = User.objects.order_by(username)[:5]
	#output = ', '.join([])
	#return HttpResponse("Hello, this is index view")
	#template = loader.get_template('users/index.html')
	#return HttpResponse(template.render())


	latest_poll_list = []
	template = loader.get_template('index.html')
	context = Context({
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))

def createAccount(request):


	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			vegetarian = form.cleaned_data['vegetarian']
			password = form.cleaned_data['password']
			m = User(username=username,
				email=email,
				vegetarian=vegetarian,
				password=password,)
			m.save()
			return HttpResponseRedirect('/users')
	else:
		form = CreateUserForm()
	return render(request,'users.html',
				{'form': form})



def profile(request):
	return HttpResponse("Hello, you have loged in! Enjoy your time.")



#user=User.objects.get(email=request.user.email),


@login_required
def addRest(request):
	if request.method == 'POST':
		form = AddRestForm(request.POST)
		if form.is_valid():
			restName = form.cleaned_data['restName']
			restUserRate = form.cleaned_data['restUserRate']


			m = FavoriteRest(rate=restUserRate,
				restaurantName=restName,
				user=User.objects.get(id=request.user.id),
				)
			m.save()
			return HttpResponseRedirect('/users/profile')
	else:
		form = AddRestForm()
	return render(request,'addRest.html',
				{'form': form})





@login_required
def profile(request):
#	userProfile = UserProfile.objects.get(user = request.user.id)
	fav_rest_list = [Restaurant.objects.get(id=i.restaurantId) for i in UserRestaurant.objects.filter(user = request.user.id)]
	bm_rest_list = [Restaurant.objects.get(id=i.restaurantId) for i in BMRestaurant.objects.filter(user = request.user.id)]
	return render(request,'profile.html',
				{'fav_rest_list': fav_rest_list, 'bm_rest_list':bm_rest_list
				})

@login_required	
def search(request):

	if request.method == 'POST':



		keyword = request.POST.get('keyword')
	
		result = FavoriteRest.objects.filter(rate = keyword)

		return render(request,'profile.html',
				{'fav_rest_list': result})

		return HttpResponseRedirect('/users/profile')


	return render(request,'search.html',
				{})

def register(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			vegetarian = form.cleaned_data['vegetarian']
			password = form.cleaned_data['password']
			
			user = User.objects.create_user(username,email,password)
			if user is not None:
				user.save()
				return HttpResponseRedirect('/users')
			else:
				return HttpResponse(simplejson.dumps({'msg':'Try Again.'}))

	else:
		form = CreateUserForm()
	return render(request,'users.html',
				{'form': form})



def restaurantList(request):
	return render_to_response('restaurantList.html', {'obj': Restaurant.objects.all()})


@login_required
def restaurantProfile(request,rId):

	if request.method == 'POST':
		if request.POST.get('favorite'):
			# add user restaurant relation
			print "add favorite"


			m = UserRestaurant(rate=5,
				restaurantId=rId,
				user=User.objects.get(id=request.user.id),
				)
			m.save()

		elif(request.POST.get('bookmark')):
			print "add bookmark"
			m = BMRestaurant(
				restaurantId=rId,
				user=User.objects.get(id=request.user.id),
				)
			m.save()






	return render(request,'restaurantProfile.html', {'obj': Restaurant.objects.filter(id=rId)})

def rlist(request):

	rlist = list(Restaurant.objects.all())
	response_data=[]
	r=dict()
	for item in rlist:
		
		r['name']=item.restaurantName
		r['id']=item.id
		response_data.append({'name':item.restaurantName, 
							'id':item.id})



	return HttpResponse(json.dumps(response_data), content_type="application/json")


