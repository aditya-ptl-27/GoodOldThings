from django.shortcuts import render,redirect
from .models import User,Product,ProductImage
from django.conf import settings
from django.core.mail import send_mail
import random
from .form import ProductForm,ProductImageForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
 
# Create your views here.
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		# if user.usertype=='renter':
			# workout=Workout.objects.all()
			# blogs=BlogModel.objects.all()
			# lender=User.objects.filter(usertype='lender')
			# context={'workout':workout,'lender':lender,'blogs':blogs,'user':user}
		return render(request,'index.html',{'user':user})
		# else:
		# 	return redirect('lender_index')
	except:
		# workout=Workout.objects.all()
		# blogs=BlogModel.objects.all()
		# lender=User.objects.filter(usertype='lender')
		# context={'workout':workout,'lender':lender,'blogs':blogs}
		return render(request,'index.html')

def signup(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=='user':
			return redirect('index')
		# else:
		# 	return redirect('lender_index')
	except:	
		if request.method=='POST':
			# user=User()
			# user.fname=request.POST['fname']
			# user.lname=request.POST['lname']
			# user.email=request.POST['email']
			# user.mobile=request.POST['mobile']
			# user.address=request.POST['address']	
			# user.password=request.POST['password']
			try:
				User.objects.get(email=request.POST['email'])
				msg='Email Already Registered'
				return render(request,'signup.html',{"msg":msg,'user':user})
			except:
				if request.POST['password']==request.POST['cpassword']:
					User.objects.create(
								fname=request.POST['fname'],
								lname=request.POST['lname'],
								email=request.POST['email'],
								mobile=request.POST['mobile'],
								password=request.POST['password'],
								address=request.POST['address'],
								profile_pic=request.FILES['profile_pic'],
								# usertype=request.POST['usertype']
								)
					msg='User SignUp Successful'
					return render(request,'login.html',{'msg':msg})
				else:
					msg="Password & Confirm Password Does Not Match"
					return render(request,'signup.html',{'msg':msg,'user':user})
		else:
			return render(request,'signup.html')

def login(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=='user':
			return redirect('index')
		# else:
		# 	return redirect('lender_index')
	except:
		if request.method=='POST':
			try:
				user=User.objects.get(email=request.POST['email'])
				print(user.usertype)
				if user.password==request.POST['password']:
					# if user.usertype=='renter':
					print(user.profile_pic)
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return redirect('index')
				else:
					msg='Password Is Incorrect'
					return render(request,'login.html',{'msg':msg})
			except:
				msg='Email Does Not Exist'
				return render(request,'login.html',{'msg':msg})

		else:
			return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return redirect('login')

	except:
		return redirect('login')

def profile(request):
	try:
		user=User.objects.get(email=request.session['email'])
		print('in try')
		# if user.usertype=='user':
		if request.method=='POST':
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.mobile=request.POST['mobile']
			user.address=request.POST['address']
			
			try:
				user.profile_pic=request.FILES['profile_pic']
			except:
				pass
			user.save()
			msg='Profile Updated Successfully'
			request.session['profile_pic']=user.profile_pic.url
			request.session['fname']=user.fname
			return render(request,'profile.html',{'msg':msg,'user':user})
		else:
			return render(request,'profile.html',{'user':user})
		# else:
		# 	return redirect('index')
	except:
		return redirect('login')

def change_password(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=='user':
			if request.method=='POST':
				if user.password==request.POST['old_password']:
					if request.POST['new_password']==user.password:
						msg='You Cannot Use Your Old Password'
						return render(request,'change_password.html',{'msg':msg,'user':user})
					else:

						if request.POST['new_password']==request.POST['cnew_password']:
							user.password=request.POST['new_password']
							user.save()
							del request.session['email']
							del request.session['fname']
							del request.session['profile_pic']
							msg='Password Changed Successfully'
							return render(request,'login.html',{'msg':msg})
						else:
							msg='New Password And Confirm New Password Does Not Match'
							return render(request,'change_password.html',{'msg':msg,'user':user})
				else:
					msg='Old Password Is Incorrect'
					return render(request,'change_password.html',{'msg':msg,'user':user})

			else:
				return render(request,'change_password.html',{'user':user})
		else:
			return redirect('change_password')
	except:
		return redirect('login')

def add_product(request):
	user = User.objects.get(email=request.session['email'])
	if user.usertype == 'user':
		if request.method == 'POST':
			product_form = ProductForm(request.POST)
			image_formset = ProductImageFormSet(request.POST, request.FILES, prefix='images')
		if product_form.is_valid() and image_formset.is_valid():
			product = product_form.save(commit=False)
			product.user = request.user
			product.save()

			for form in image_formset:
				if form.cleaned_data.get('image'):
					ProductImage.objects.create(product=product, image=form.cleaned_data['image'])

			return redirect('product_list')  # Redirect to a page displaying all products

		else:
			product_form = ProductForm()
			image_formset = ProductImageFormSet(prefix='images')
			return render(request, 'add_product.html', {'product_form': product_form, 'image_formset': image_formset})
	else:
		return redirect('index')


# def add_product(request):
# 	user=User.objects.get(email=request.session['email'])
# 	# trainer=User.objects.get(email=request.session['email'])
# 	if user.usertype=='user':
# 		if request.method=='POST':
# 			form = ProductForm(request.POST, request.FILES)
# 			if form.is_valid():
# 				product = form.save()
# 				for image in form.cleaned_data['images']:
# 					Image.objects.create(image=image, product=product)
# 					Product.objects.create(
# 							user=user,
# 							p_category=request.POST['p_category'],
# 							p_name=request.POST['p_name'],
# 							p_description=request.POST['p_description'],
# 							p_price=request.POST['p_price'],
# 							p_images=request.FILES['p_images']
# 						)	
# 					msg='Product Added Successfully'
# 					return render(request,'add_product.html',{'msg':msg,'user':user,'form':form})
# 			else:
# 				form = ProductForm()

# 		else:
# 			return render(request,'add_product.html',{'user':user})
# 	else:
# 		return redirect('index')

	# def product_create(request):
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         product = form.save()
    #         for image in form.cleaned_data['images']:
    #             Image.objects.create(image=image, product=product)

    #         return redirect('product_list')
    # else:
    #     form = ProductForm()

    # return render(request, 'product_create.html', {'form': form})

# def lender_index(request):
# 	# lender=User.objects.get(email=request.session['email'])
# 	user=User.objects.get(email=request.session['email'])
# 	if user.usertype=='lender':
# 		# blogs=BlogModel.objects.filter(user=user)
# 		# workout=Workout.objects.filter(lender=lender)
# 		# lenders=User.objects.filter(usertype='lender')
# 		# context={'workout':workout,'lenders':lenders,'blogs':blogs,'user':user}
# 		return render(request,'lender_index.html',{'user':user})
# 	else:
# 		return redirect('index')