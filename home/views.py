from django.shortcuts import render, HttpResponseRedirect
from home.models import contacts

# Create your views here.
def home(request):
    #return HttpResponse("this is the data")
    context={'name':'vaibhav','test':'django'}
    return render(request,'home.html', context)

# def about(request):
#     context={'name':'about','test':'django'}
#     return render(request,'about.html', context)

def portfolio_details(request):
    context={'name':'about','test':'django'}
    return render(request,'portfolio-details.html', context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        concern=request.POST['concern']
        ins=contacts(name=name, email=email, phone=phone, concern=concern)
        #print(name)
        ins.save()
        print(name)
        return render(request,'home.html')


    #context={'name':'contact','test':'django'}
    return render(request,'home.html')






