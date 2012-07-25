# Create your views here.


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
#from django import forms 0.95 style
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django import  forms #need this for the registration ...it simply the same
from django.contrib.auth.forms import UserCreationForm



#Handling registration  obeng william 

'''
class registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def register(request):
    form = registration()
    if request.method == 'POST':
       data = request.POST.copy()
       if form.is_valid:
           new_user = form.save(data)
           return HttpResponseRedirect("/books/")
    else:
        pass

    return render_to_response("reg/base_register.html", {'form' : form})



'''

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Login view - Nana B.
#tested code and it works logs in perfectly
@csrf_exempt
def do_login(request):
	
	disabled_accMsg = ''
	invalidMsg = ''
	sess_data = ''
        already_logged_in=''#william made changes to your code here...had errors to added this to work
	if request.user.username != '':
		already_logged_in = 'You are already logged in.'

	if request.method == 'POST':
   	        uname = request.POST['username']	
		pword = request.POST['password']
		user = authenticate(username=uname, password=pword)
		if user is not None:
			if user.is_active:
				login(request, user)
				#request.session["uname_sess"] = uname
				return HttpResponseRedirect(request.path)
			
			##redirect
			else:
				disabled_accMsg = "Sorry, your account has been disabled. Contact the administrator."
				
			##return a disabled account msg
		else:
			invalidMsg = "Username or Password is invalid!"
			
		#return an invalid login message
	
	#YOUR CODE HERE
	else:
        	form = LoginForm()
	form = LoginForm()
	return render_to_response('reg/base_login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated(),
	'disabled_accMsg': disabled_accMsg,
	'invalidMsg': invalidMsg,
	'already_logged_in': already_logged_in,
	'user': request.user
    })


# Login view - Nana B.

@csrf_exempt
def do_logout(request):
	if request.user.username != '':
		logout(request)
		request.user.username = ''
		return render_to_response('reg/base_logout.html',{'user': request.user})
	else:
		return HttpResponseRedirect(request.path)
