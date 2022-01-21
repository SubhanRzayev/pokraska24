from multiprocessing.dummy import Process
from pyexpat import model
from django.contrib import admin

# Register your models here.

from core.models import About, Address, Contact, Employer,Image, Index, OrderOption, Price,ProjectImage,ProcessContent,Process, Service, ServiceCategory,OurWork,Order


class AboutImageInline(admin.TabularInline):
    model = Image
    extra = 10
    
class ServiceImageInline(admin.TabularInline):
    model = Image
    extra = 15
    

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag',]
    readonly_fields = ('image_tag',)
    

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['image_tag',]
    readonly_fields = ('image_tag',)



@admin.register(ProcessContent)
class ProcessContentAdmin(admin.ModelAdmin):
    list_display = ['price_head_content' ,'content','service_content','price_content',]

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['count','title','description','image_tag',]
    readonly_fields = ('image_tag',)
    
    


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag',]
    readonly_fields = ('image_tag',)
    list_filter = ['title',]
    inlines = [AboutImageInline]
    

@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ['title','description','description1','image_tag',]
    readonly_fields = ('image_tag',)
    list_filter = ['title',]
    
    
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','content','checkbox',]
    list_filter = ['name','checkbox',]
    search_fields = ('name',)  
    
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['title','location','email','phone','phone1',]
    list_filter = ['email',]
    search_fields = ('email',)
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag',]
    list_filter = ['title',]
    search_fields = ('title',)
    inlines = [ServiceImageInline]
    
    
    
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['title',]
    search_fields = ('title',)
    
    
    
    
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['title','price',]
    list_filter = ['title',]
    search_fields = ('title',)
    
    

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['name','phone',]
    list_filter = ['name','phone',]
    search_fields = ('name',)
    



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['about','service','image_tag',]
    readonly_fields = ('image_tag',)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_option','quantity','text','name','phone','checkbox',]
    list_filter = ['quantity','name','phone',]
    
    
@admin.register(OrderOption)
class OrderOptionAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['title',]
    