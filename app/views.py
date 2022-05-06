from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.db.models import Q	
from .models import Profile,Cart,OrderPlaced,Product
from .forms import CustomerProfileForm,AuthenticationForm,Registration
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def base(request):
	return render(request,'base.html')

def aboutus(request):
	return render(request,'aboutus.html')

def customerservice(request):
	return render(request,'customerservice.html')

def covid19andarmani(request):
	return render(request,'covid19andarmani')


def login_request(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		User=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('welcome')
		else:
			messages.info(request,'invalid user')
			return redirect('/login')
	else:
		return render(request,'login.html')




def registration(request):
	if request.method=='POST':
		customerno=request.POST['customerno']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		username=request.POST['username']
		password=request.POST['password']
		reenterpassword=request.POST['reenterpassword']

		if password==reenterpassword:
			if User.objects.filter(username=username).exists():
				messages.info(request,'user name already exists')
				return render(request,'registration.html')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email already exists')
				return render(request,'registration.html') 
			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save()
				customer=Customer.objects.create(customerno=customerno,username=username,password=password,reenterpassword=reenterpassword,email=email,first_name=first_name,last_name=last_name)
				customer.save()
				return redirect('login')
		else:
			messages.info(request,'password not matched')
			return render(request,'registration.html')
	else:
		return render(request,'registration.html')

def settings(request):
	return render(request,'settings.html')


def countryandlanguage(request):
	return render(request,'countryandlanguage.html')

def notifications(request):
	return render(request,'notifications.html')

def alexa(request):
	return render(request,'alexa.html')


def welcome(request):
	return render(request,'welcome.html')



def logout_request(request):
	logout(request)
	return redirect('index')

@login_required
def address(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
		address = Profile.objects.filter(user=request.user)
	return render(request, 'address.html', {'address':address, 'active':'btn-primary', 'totalitem':totalitem})





def watch(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			watches = Product.objects.filter(category='W')
	elif data == 'das':
			watches = Product.objects.filter(category='W').filter(brand=data)
	elif data == 'blacks':
			watches = Product.objects.filter(category='W').filter(brand=data)
	elif data == 'piran':
			watches = Product.objects.filter(category='W').filter(brand=data)
	elif data == 'cooper':
			watches = Product.objects.filter(category='W').filter(brand=data)
	return render(request, 'watch.html', {'watches':watches, 'totalitem':totalitem})


def sunglass(request, data=None):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
	if data==None :
			sunglasses = Product.objects.filter(category='S')
	elif data == 'vincent':
			sunglasses = Product.objects.filter(category='S').filter(brand=data)
	elif data == 'lopo':
			sunglasses = Product.objects.filter(category='S').filter(brand=data)
	elif data == 'royalguard':
			sunglasses = Product.objects.filter(category='S').filter(brand=data)
	elif data == 'tracks':
			sunglasses = Product.objects.filter(category='S').filter(brand=data)
	return render(request, 'sunglasses.html', {'sunglasses':sunglasses, 'totalitem':totalitem})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
	def get(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm()
		return render(request, 'profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})
		
	def post(self, request):
		totalitem = 0
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			user = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			reg = Profile(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})

	
class ProductDetailView(View):
	def get(self,request,pk):
		totalitem=0
		product=Product.objects.get(pk=pk)
		print(product.id)
		item_already_in_cart=False
		if request.user.is_authenticated:
			totalitem=len(Cart.objects.filter(user=request.user))
			item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
		return render(request,'productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem})


class ProductView(View):
	def get(self, request):
		totalitem = 0
		watches = Product.objects.filter(category='W')
		sunglasses = Product.objects.filter(category='S')
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
		return render(request, 'index.html', {'watches':watches,'sunglasses':sunglasses, 'totalitem':totalitem})


class Registration(View):
 def get(self, request):
  form = Registration()
  return render(request, 'registration.html', {'form':form})
  
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully.')
   form.save()
  return render(request, 'registration.html', {'form':form})