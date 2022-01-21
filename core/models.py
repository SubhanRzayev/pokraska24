from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe


# Create your models here.





class About(models.Model):
    title = models.CharField(max_length=80,blank=True,null=True)
    description = RichTextUploadingField()
    description1 = RichTextUploadingField()
    about_image  = models.ImageField(upload_to = 'media')
    
    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.about_image.url))
    image_tag.short_description = 'Image'
    
    
    

class Employer(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    checkbox = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    





class Index(models.Model):
    title = models.CharField(max_length=120,blank=True,null=True)
    yaer_work = models.CharField(max_length=120,blank=True,null=True)
    description = RichTextUploadingField()
    index_image = models.ImageField(upload_to='index_image')
    
    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.index_image.url))
    image_tag.short_description = 'Image'
    
    
    
class OurWork(models.Model):
    title = models.CharField(max_length=120,blank=True,null=True)
    description = RichTextUploadingField()
    description1 = RichTextUploadingField()
    image = models.ImageField(upload_to = 'ourwork')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'OurWork'


    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    
    
    

class Address(models.Model):
    title = models.CharField(max_length=1000,default='Профессиональная покраска мебели, изделий из дерева и других материалов', blank=True,null=True)
    location = models.TextField(max_length=1000,default="140186, Московская обл., г. Люберцы, деревня Токарево, ул. Петровское поле, д. 1")
    email = models.EmailField(default='info@pokraska24.com',blank=True)
    phone = models.CharField(max_length=20,default='(+7) 495 508-63-45') 
    phone1 = models.CharField(max_length=20,default='(+7) 925 508-63-45')    
    work_time = models.CharField(max_length=1000,default='с 11 до 18 часов', blank=True,null=True)
    image = models.ImageField(upload_to="media",blank=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Ünvan"
    
    

    
    
    
    
class Process(models.Model):
    count = models.PositiveIntegerField()
    title = models.CharField(max_length=100,blank=True,null=True)
    description = RichTextUploadingField()   
    process_image = models.ImageField(upload_to = 'media')
    
    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.process_image.url))
    image_tag.short_description = 'Image'
    


    

class Service(models.Model):
    #relations
    
    title = models.CharField(max_length=120)
    description = RichTextUploadingField()
    slug = models.SlugField(max_length=140,unique=True)
    service_image = models.ImageField(upload_to='service_image')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("core:service_detail", kwargs={ "slug": self.slug})
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.service_image.url))
    image_tag.short_description = 'Image'
    
    
    
    
    
    
class ServiceCategory(models.Model):
    service = models.ManyToManyField('Service',db_index=True,blank=True,related_name='service_title',default=None)
    title = models.CharField(max_length=120,blank=True,null=True)
    
    
    
    def __str__(self):
        return self.title
    
    
    
    class Meta:
        verbose_name_plural = 'ServiceCategories'
    
    
    
    



class ProcessContent(models.Model):
    price_head_content = models.CharField(max_length=300,blank=True,null=True)
    content = RichTextUploadingField()
    service_content = RichTextUploadingField()
    price_content = RichTextUploadingField()
    
    
    
    def __str__(self):
        return self.content
    
    
class Contact(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=120)
    content = models.TextField(max_length=10000)
    checkbox = models.BooleanField()
    
    
    created_at = models.DateTimeField(auto_now=True,blank=True)
    

    def __str__(self):
        return self.name
    
    
    
    
    
    



class ProjectImage(models.Model):
    project_image = models.ImageField(blank=True,upload_to='images')
    
    def __str__(self):
        return str(self.project_image)
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.project_image.url))
    image_tag.short_description = 'Image'

    

class Image(models.Model):
    about = models.ForeignKey('About',on_delete=models.CASCADE, related_name='about_images',db_index=True,blank=True,null=True)
    service = models.ForeignKey('Service',on_delete=models.CASCADE,related_name='service_images',db_index=True,blank=True,null=True)
    image = models.ImageField(blank=True,upload_to='images')
    
    
    def __str__(self):
        return str(self.image)
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    

class Price(models.Model):
    #relation
    service = models.ForeignKey('Service',db_index=True,on_delete=models.CASCADE,null=True,blank=True,related_name='service_prices')
    
    title = models.CharField(max_length=300,blank=True,null=True)
    price = models.CharField(max_length=300,blank=True,null=True)
    
    
    def __str__(self):
        return self.title




class Order(models.Model):
    #relations
    order_option = models.ForeignKey('OrderOption',on_delete=models.CASCADE,blank=True,null=True,related_name='order_options')
    
    
    quantity = models.CharField(max_length=120)
    text = models.TextField(max_length=10000)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    checkbox = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    
class OrderOption(models.Model):
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title
    
    
    
    
        
        

    
    