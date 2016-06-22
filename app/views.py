from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
import app.validate
from app.models import User
import json
import sign_up_api as register_api
# Create your views here.


@csrf_exempt
def signin(request):
	template = loader.get_template("signin.html")
	return HttpResponse(template.render())

@csrf_exempt
def start(request):
	gId = None
	cookies = request.COOKIES
	print cookies
	if "gid" in cookies:
		gId = cookies["gid"]
		firstname = cookies["firstname"]
		lastname = cookies["lastname"]
		image_url = cookies["imageURL"]
		email = cookies["email"]
	if gId is None:
		return HttpResponseRedirect("/signin")
	try:
		user = User.objects.get(gprofileId=gId)
		if user.profileId != "":
		# template = loader.get_template("home.html") #home
			temp = HttpResponseRedirect("/home")
			temp.set_cookie("profileId", user.profileId)
			request.session["active"] = True
			return temp
		else:
			return HttpResponseRedirect("/sign_up")
	except:
		User.objects.create(gprofileId=gId,firstname=firstname,lastname=lastname,email=email,image_url=image_url)
        # TODO: change name signup page
		print "here"
		return HttpResponseRedirect("/sign_up")


@csrf_exempt
def sign_up(request):
	print "here"
	template = loader.get_template("login.html")
	return HttpResponse(template.render())


@csrf_exempt
def sign_up_api(request):
	print request.body
	if request.method == "POST":
		form_data = request.POST
		gid = request.COOKIES["gid"]
		user = User.objects.get(gprofileId=gid)
		# call the api
		sign_up_response = register_api.sign_up(user,form_data) #form data
		if "key" in sign_up_response:
			profileId = sign_up_response["key"]
    		# user = User.objects
    		# template = loader.get_template("home.html")
			user.profileId = profileId
			user.save()
			response = HttpResponseRedirect("/select_courses")
			response.set_cookie("profileId", profileId)
			request.session["active"] = True
			return response
		else:
			return HttpResponse(sign_up_response)
	else:
		return HttpResponse("Get not supported")


@csrf_exempt
def home(request):
	if "active" in request.session:
		if request.session["active"]:
			template = loader.get_template("home.html")  # home
			return HttpResponse(template.render())
		else:
			return HttpResponseRedirect("/signin")


@csrf_exempt
def course_page(request):
	if "active" in request.session:
		if request.session["active"]:
	    	# course_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
			template = loader.get_template("Courses.html")
			response = HttpResponse(template.render())
	    	# response.set_cookie()
	    	return response
	else:
		return HttpResponseRedirect("/signin")


@csrf_exempt
def select_courses(request):
	template = loader.get_template("courseSelection.html")
	return HttpResponse(template.render())


@csrf_exempt
def notes_page(request):
	if "active" in request.session:
		if request.session["active"]:
    		# note_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
			template = loader.get_template("notes.html")
			response = HttpResponse(template.render())
    		# response.set_cookie()
			return HttpResponse(template.render())
	else:
		return HttpResponseRedirect("/signin")
@csrf_exempt
def assignment(request):
	if "active" in request.session:
		if request.session["active"]:
    		# note_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
			template = loader.get_template("notes.html")
			response = HttpResponse(template.render())
    		# response.set_cookie()
			return HttpResponse(template.render())
	else:
		return HttpResponseRedirect("/signin")
@csrf_exempt
def exam(request):
	if "active" in request.session:
		if request.session["active"]:
    		# note_id = QueryDict(request.META['QUERY_STRING'])["course_id"]
			template = loader.get_template("notes.html")
			response = HttpResponse(template.render())
    		# response.set_cookie()
			return HttpResponse(template.render())
	else:
		return HttpResponseRedirect("/signin")


@csrf_exempt
def profile(request):
	if "active" in request.session:
		if request.session["active"]:
			template = loader.get_template("profile.html")
    		return HttpResponse(template.render())
    	else:
    		return HttpResponseRedirect("/signin")


@csrf_exempt
def search_action(request):
	if "active" in request.session:
		if request.session["active"]:
			if(request.method == "POST"):
				return HttpResponseRedirect("/search")
		else:
			return HttpResponseRedirect("/signin")


@csrf_exempt
def search_page(request):
	if "active" in request.session:
		if request.session["active"]:
			template = loader.get_template("search.html")
			return HttpResponse(template.render())
		else:
			return HttpResponseRedirect("/signin")


@csrf_exempt
def upload_page(request):
	if "active" in request.session:
		if request.session["active"]:
			template = loader.get_template("uploads.html")
			return HttpResponse(template.render())
		else:
			return HttpResponseRedirect("/signin")



@csrf_exempt
def sign_out(request):
	if "active" in request.session:
		if request.session["active"]:
			request.session["active"] = False
	return HttpResponseRedirect("/signin")



@csrf_exempt
def mobile_sign_in(request):
	if request.method == "POST":
		data = json.loads(request.body)
		gprofileId = data["gprofileId"]
		try:
			user = User.objects.get(gprofileId=gprofileId)
			if user.profileId!="":
				return HttpResponse(user.profileId)
			return HttpResponse("0")
		except:
			return HttpResponse("0")


@csrf_exempt
def mobile_sign_up(request):
	if request.method == "POST":
		data = json.loads(request.body)
		gprofile_id = data["gprofileId"]
		profile_id = data["profileId"]
		profileName = data["profileName"]
		firstname,lastname = profileName.split(" ")[0],profileName.split(" ")[1]
		email = data["email"]
		image_url = data["imageUrl"]
		User.objects.create(gprofileId=gprofile_id,profileId=profile_id,firstname=firstname,lastname=lastname,email=email,image_url=image_url)
		return HttpResponse("Success")













