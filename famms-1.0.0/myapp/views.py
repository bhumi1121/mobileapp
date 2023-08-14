from django.shortcuts import render,redirect
from .models import User,Mobile
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
	mobile=Mobile.objects.all()
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def blog_list(request):
	return render(request,'blog_list.html')

def contact(request):
	return render(request,'contact.html')

def product(request):
	return render(request,'product.html')

def testimonial(request):
	return render(request,'testimonial.html')

def register(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg1 = "Email alredy exist..."
			return render(request,'register.html',{'msg1':msg1})
		except:
			if request.POST['pswd']==request.POST['cpswd']:
				User.objects.create(
					usertype=request.POST['usertype'],
					name=request.POST['name'],
					email=request.POST['email'],
					pswd=request.POST['pswd'],
				)
				msg = "Registration done..."
				return render(request,'login.html',{'msg':msg})
			else:
				msg1 = ('password and confirm password doesnt matched...')
				return render(request,'register.html',{'msg1':msg1})
	else:
		return render(request,'register.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			msg="login succesfull.."
			request.session['email']=user.email
			request.session['pswd']=user.pswd
			if user.usertype=="product_manager":
				return render(request,'seller_index.html')
			else:
				return render(request,'index.html')
		except:
			msg1 = "email doesn't exist..."
			return render(request,'login.html',{'msg1':msg1})
	else:
		return render(request,'login.html')

def logout(request):
	del request.session['email']
	return redirect('login')

def fpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>working till user")

			subject = 'forgot password otp'
			otp = random.randint(1000,9999)
			message = f'Hi {user.name}, thank you for registering in my app, your otp is :- '+str(otp)
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>working till otp")

			email_from = settings.EMAIL_HOST_USER
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>working till host user")

			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>working till now")
			return render(request, 'verify_otp.html',{'email':user.email,'otp':str(otp)})

		except:
			msg1 = "you are not registered user..."
			return render(request,'fpswd.html',{'msg1':msg1})

	else:
		return render(request,'fpswd.html')

def verify_otp(request):
	email=request.POST['email']
	uotp=request.POST['uotp']
	otp=request.POST['otp']
	if request.method=='POST':
		
		if uotp==otp:
			return render(request,'set_pswd.html',{'email':email})
		else:
			msg1 = "otp doesn't matched!!!"
			return render(request,'verify_otp.html',{'msg1':msg1})
	else:
		return render(request,'verify_otp.html')

def set_pswd(request):
	if request.method=="POST":
		email=request.POST['email']
		npswd=request.POST['npswd']
		cnpswd=request.POST['cnpswd']
		if npswd==cnpswd:
			user=User.objects.get(email=email)
			user.pswd=npswd
			user.save()
			return redirect('login')
		else:
			msg1="password and confirm pasword does not matched..."
			return render(request,'set_pswd.html',{'msg1':msg1})
	else:
		return render(request,'set_pswd.html')

def seller_index(request):
	return render(request,'seller_index.html')

def add_mobile(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Mobile.objects.create(
			user=user,
			mobile_brand=request.POST['mobile_brand'],
			mobile_model=request.POST['mobile_model'],
			mobile_ram=request.POST['mobile_ram'],
			mobile_storage=request.POST['mobile_storage'],
			mobile_price=request.POST['mobile_price'],
			mobile_image=request.FILES['mobile_image'],
		)
		msg="mobile added successfully.."
		return render(request,'add_mobile.html',{'msg':msg})
	else:
		return render(request,'add_mobile.html')

def mobiles(request):
	seller=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",seller)
	mobile=Mobile.objects.filter(user=seller)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",mobile)
	return render(request,'mobiles.html',{'mobile':mobile})

def update_mobile(request,pk):
	seller=User.objects.get(email=request.session['email'])
	mobile=Mobile.objects.get(pk=pk,user=seller)
	if request.method=="POST":
		mobile.user=seller
		mobile.mobile_brand=request.POST['mobile_brand']
		mobile.mobile_model=request.POST['mobile_model']
		mobile.mobile_ram=request.POST['mobile_ram']
		mobile.mobile_storage=request.POST['mobile_storage']
		mobile.mobile_price=request.POST['mobile_price']
		mobile.mobile_image=request.FILES['mobile_image']
		mobile.save()
		return render(request,'mobiles..html',{'mobile':mobile})
	else:
		return render(request,'update_mobile.html',{'mobile':mobile})

def delete_mobile(request,pk):
	seller=User.objects.get(email=request.session['email'])
	mobile=Mobile.objects.get(pk=pk,user=seller)

	mobile.delete()
	return redirect("seller_index")

def search(request):
	if request.method=="POST":
		search=request.POST['search_item']
		if request.POST['search_item'].__contains__(search):
			mobile=Mobile.objects.filter(mobile_brand=search)
			return render(request,'mobiles.html',{'mobile':mobile})

		else:
			msg="no such mobile found..."
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",msg)
			return render(request,'mobiles.html',{'msg':msg})

	else:
		return render(request,'seller_index.html')
