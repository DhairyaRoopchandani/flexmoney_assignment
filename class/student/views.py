from django.shortcuts import render
from .forms import member,Sform,Payment
from .models import member as m

def register(request):
    title="Member Registration"
    form=member(request.POST or None)
    if form.is_valid():
        Name=form.cleaned_data['name']
        Email=form.cleaned_data['email']
        Ph_no=form.cleaned_data['phone_no']
        Gender=form.cleaned_data['gender']
        Time=form.cleaned_data['schedule_preference']
        Age=form.cleaned_data['age']
        Date=form.cleaned_data['date']
        mail=m.objects.filter(email=Email)
        if len(mail)>0:
            return render(request,'ack.html',{"title":"Email already exists"})

        p=m(name=Name,email=Email,phone_no=Ph_no,gender=Gender,schedule_preference=Time,age=Age,date=Date)
        p.save()
        return render(request,'ack.html',{'title':"Please complete payment process To confirm booking."})

    context={
        "title":title,
        "form":form,
    }
    return render(request,'register.html',context)
def existing(request):
    title="All Registered Stuents"
    queryset=m.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context)
def search(request):
    title="Search Member"
    form=Sform(request.POST or None)
    if form.is_valid():
        Name=form.cleaned_data['name']
        queryset=m.objects.filter(name=Name)
        if len(queryset)==0:
            return render(request,"ack.html",{"title":"No such member exist"})
        context={
            'title':title,
            'queryset':queryset,
        }
        return render(request,'existing.html',context)
    context={
        'title':title,
        'form':form,
    }
    return render(request,'search.html',context)

def dropout(request):
    title="Drop Out"
    form=Sform(request.POST or None)
    if form.is_valid():
        Name=form.cleaned_data['name']
        queryset=m.objects.filter(name=Name)
        if len(queryset)==0:
            return render(request,"ack.html",{"title":"No such member exist"})
        else:
            queryset=m.objects.filter(name=Name).delete()
            return render(request,'ack.html',{'title':"Member Removed"})
    context={
        'title':title,
        'form':form,
    }
    return render(request,'drop.html',context)


def completePayment(request):
    title="Payment processing"
    form=Payment(request.POST or None)
    if form.is_valid():
        Name=form.cleaned_data['name']
        pay_id=form.cleaned_data['upi_id']
        amt=form.cleaned_data['amount']
        Date=form.cleaned_data['date']
        p=m(name=Name,upi_id=pay_id,amount=amt,date=Date)
        p.save()
        return render(request,'ack.html',{'title':"Payment Confirmed"})
    context={
        "title":title,
        "form":form,
    }
    return render(request,'payment.html',context)


        
    






# Create your views here.
