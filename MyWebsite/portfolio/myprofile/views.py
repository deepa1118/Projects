from django.shortcuts import render,redirect
from django.contrib import messages
from myprofile.models import Contact,Skill
# Create your views here.
def home(request):
    return render(request, 'home.html')

def handleskill(request):
    posts=Skill.objects.all()
    context={"posts":posts}
    return render(request, 'handleskill.html',context)

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting. We will get back to you soon!")
        return redirect('/contact')
    return render(request, 'contact.html')

