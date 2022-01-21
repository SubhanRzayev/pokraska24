from multiprocessing import context
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from core.forms import ContactForm, EmployerForm, OrderForm
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from core.models import About, Address,Contact, Employer,Image, OurWork, Price, ProcessContent, ProjectImage,Process, Service, ServiceCategory,Index
# Create your views here.



class IndexView(FormView,TemplateView):
    model = Employer
    form_class = ContactForm
    form_class = EmployerForm
    form_class = OrderForm
    
    
    
    template_name = 'index.html'
    success_url = reverse_lazy('core:index')

    
    
    
    def form_valid(self, form):
        form.save()
        context = super().form_valid(form)
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_list"] = About.objects.all()
        context["our_work_list"] = OurWork.objects.all()
        context["project_image_list"] = ProjectImage.objects.all()
        context["index_list"] = Index.objects.all()
        
        
        
        return context
    
    
    
    
class AboutView(FormView,ListView):
    model = About
    form_class = OrderForm
    success_url = reverse_lazy('core:about')
    template_name = 'about.html'
    
    
    def form_valid(self, form):
        form.save()
        context = super().form_valid(form)
        return context
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["contact_list"] = Address.objects.all()
        
        return context
        
    
    
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')
    
    
    
    def form_valid(self,form):
        form.save()
        context = super().form_valid(form)
        return context
    
class ImageView(ListView):
    model = Image
    template_name = 'foto.html'
    
class ProjectView(ListView):
    model = ProjectImage
    template_name = 'project.html'
    
    
    
class ProcessView(ListView):
    model = Process
    template_name = 'proses.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['process_content_list'] = ProcessContent.objects.all()   
        
        return context

class ServiceView(FormView,ListView):
    model = Service
    form_class = OrderForm
    template_name = 'service.html'
    success_url = reverse_lazy('core:service')
    
    
    
    def form_valid(self, form):
        form.save()
        context =  super().form_valid(form)
        return context
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['process_content_list'] = ProcessContent.objects.all()   
        context['service_categories_list'] = ServiceCategory.objects.all()   
        

        return context
    

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    success_url = reverse_lazy("core:service")
    
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["service_list"] = Service.objects.order_by('-title')[:4]
        context["price_list"] = Price.objects.all()
        
        
        return context
    
class PriceView(ListView):
    model = Price
    template_name = 'price.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['process_content_list'] = ProcessContent.objects.all()    
        return context
    
    
    
    




        

    
    

    
