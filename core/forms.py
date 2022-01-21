from dataclasses import field
from tabnanny import check
from django import forms
from core.models import Contact,Employer,Order,OrderOption

class ContactForm(forms.ModelForm):
    
    checkbox = forms.BooleanField()
    
    
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone',
            'content',
            'checkbox',
        )
        
        
        def __init__(self):
            self.fields['checkbox'].initial = True
        
        widgets = {

            'name':forms.TextInput(attrs={
                        'class':'inp-wp',
                        'placeholder': 'Ваш имя*'
                    }),

            'phone':forms.TextInput(attrs={
                'class':'inp-wp',
                'placeholder': 'Ваш телефон*'
            }),

            

            'content':forms.TextInput(attrs={
                'class': 'wrap-textarea',
                'placeholder': 'Ваш message*'
            }),
        }
        

class EmployerForm(forms.ModelForm):
    
    checkbox = forms.BooleanField()
    
    
    
    class Meta:
        model = Employer
        fields = (
            'name',
            'phone',
            'checkbox',
            
        )
        
        def __init__(self):
            self.fields['checkbox'].initial  = True
        
        widgets = {

            'name':forms.TextInput(attrs={
                        'class':'inp-wp',
                        'placeholder': 'Ваше имя *'
                    }),

            'phone':forms.TextInput(attrs={
                'class':'inp-wp last',
                'placeholder': 'Ваш телефон*'
            }),
            
        }
        

class OrderForm(forms.ModelForm):
    
    checkbox = forms.BooleanField()
    
    
    class Meta:
        model = Order
        fields = (
            'order_option',
            'quantity',
            'text',
            'name',
            'phone',
            'checkbox',
        )
        
    
        def __init__(self):
            self.fields['checkbox'].initial = True
            
            
        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['order_option'] = forms.ModelChoiceField(
                queryset=OrderOption.objects.all(),initial=0
            )
            
        widgets = {
            
            'quantity':forms.TextInput(attrs={
                        'class':'inp-wp',
                        'placeholder': 'Количество (м2) *'
                    }),
            
            'text':forms.TextInput(attrs={
                        'class':'wrap-textarea',
                        'placeholder': 'Дополнительная информация *'
                    }),

            
            'name':forms.TextInput(attrs={
                        'class':'inp-wp',
                        'placeholder': 'Ваше имя *'
                    }),

            'phone':forms.TextInput(attrs={
                        'class':'inp-wp last',
                        'placeholder': 'Ваш телефон*'
                    }),
        }
        
        
        
        
    