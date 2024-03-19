from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .helpers import *
 
# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	profile_pic=models.ImageField(upload_to="profile_pic/",default="static 'image/user_default.jpg' ")
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default='user')

	def __str__(self):
		return self.fname+" - "+self.lname
 
class Product(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	p_category=models.CharField(max_length=100)
	p_name=models.CharField(max_length=100)
	p_description=models.TextField()
	p_price=models.FloatField()
	p_available_from=models.DateField()
	p_available_until=models.DateField()
	slug = models.SlugField(max_length=1000, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.fname+ ' - ' +self.user.lname+' - ' +self.p_name

	def save(self, *args, **kwargs):
		self.slug = generate_slug(self.p_name)
		super(Product, self).save(*args, **kwargs)

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
	image = models.ImageField(upload_to='product_images/')

	def __str__(self):
		return self.product.user.fname+ ' - ' +self.product.p_name+' - ' +str(self.image)


# 	def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             for image in form.cleaned_data['images']:
#                 Image.objects.create(image=image, product=product)

#             return redirect('product_list')
#     else:
#         form = ProductForm()

#     return render(request, 'product_create.html', {'form': form})

# # In the original model, save the relationship to the new image model.

# def product_save(self):
#     super(Product, self).save()
#     for image in self.images.all():
#         image.product = self
#         image.save()