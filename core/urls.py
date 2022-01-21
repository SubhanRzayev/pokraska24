from django.urls import path
from . import views
from core.views import IndexView,AboutView,ContactCreateView,ImageView,ProjectView,ProcessView, ServiceView,ServiceDetailView,PriceView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('about/', AboutView.as_view(),name='about'),
    path('price/', PriceView.as_view(),name='price'),
    path('contact/', ContactCreateView.as_view(),name='contact'),
    path('foto/', ImageView.as_view(),name='foto'),
    path('project/', ProjectView.as_view(),name='project'),
    path('process/', ProcessView.as_view(),name='process'),
    path('service/', ServiceView.as_view(),name='service'),    
    path('<slug:slug>/',ServiceDetailView.as_view(),name='service_detail'),
]
    
    
    

    
