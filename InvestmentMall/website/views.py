from django.http import HttpResponseRedirect
from django.shortcuts import render
from.forms import ClientForm

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def ContactPage(request):
    if request.method =='POST':
        fm = ClientForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            product = fm.cleaned_data['product']
            location = fm.cleaned_data['location']
            form = ClientForm(name=name,email=email,phone=phone,product=product,location=location)
            form.save()
            return HttpResponseRedirect('/')
        else:
            print('form not saved')
    else:
        fm = ClientForm()
        return render(request,'contact.html',{"form":fm})

def AboutUs(request):
    return render(request,'about.html')


def Service(request):
    return render(request,'services.html')
    
    