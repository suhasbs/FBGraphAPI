# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import json
# Create your views here.



def index(request):
	return render(request, 'graphapi/index.html')

@csrf_exempt
def get_access_token(request):
	access_token = request.POST['access_token']
	print access_token
	request.session['access_token'] = access_token
	return JsonResponse({'recieved':1})


def get_my_info(request):
	r = requests.get('https://graph.facebook.com/v2.10/me?fields=id,name,birthday,picture,email,gender&access_token='+request.session['access_token'])
	#print r.json()
	# return HttpResponse(r.json()['name']+r.json()['id'])
	myinfo= {}
	myinfo = r.json()
	print json.dumps (myinfo, indent=2)
	return render(request, 'graphapi/my_info.html', {'myinfo':myinfo})
	#return JsonResponse(r.json(), safe=False)

def search_user(request):
	name = request.GET['name']
	r = requests.get('https://graph.facebook.com/v2.10/search?q='+name+'&type=user&access_token='+request.session['access_token'])
	res = r.json()['data']
	#parsed = json.loads(str(res))
	print json.dumps(res, indent=2)
	return render(request, 'graphapi/search_results.html', {'data':r.json()['data']})
	

def get_photo_ids(request):
	r = requests.get('https://graph.facebook.com/v2.10/me/photos?type=uploaded&limit=40&fields=id,album&access_token='+request.session['access_token'])
	#print "photos"
	#print r.json()['data']
	
	photos = {}
	#print r
	up_photos = r.json()['data']
	print json.dumps(up_photos,indent=2)
	r = requests.get('https://graph.facebook.com/v2.10/me/photos?type=tagged&limit=40&fields=id,album&access_token='+request.session['access_token'])
	tag_photos = r.json()['data']
	print json.dumps(tag_photos, indent=2)
	# r = requests.get('https://graph.facebook.com/v2.10/me/albums?access_token='+request.session['access_token'])
	
	return render(request, 'graphapi/photo_ids.html', {'up_photos':up_photos, 'tag_photos':tag_photos})
	