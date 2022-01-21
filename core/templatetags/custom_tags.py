from django.shortcuts import render
from django.template import Library
from core.models import Address,ServiceCategory,Service

register = Library()

@register.simple_tag
def header_address():
    return Address.objects.all()

@register.simple_tag
def header_category():
    a = Service.objects.order_by('-title')
    

    b = ServiceCategory.objects.order_by('-title')
    context = {
        "service_list":a,
        "servicecategory":b
    }
            
    return context


    

