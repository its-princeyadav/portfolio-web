from django.shortcuts import render , HttpResponse
from folio.models import Contact

# Create your views here.

def index(request):
    if request.method=="POST" :
        name = request.POST['fname']
        email = request.POST['femail']
        phone = request.POST['fphone']
        msg = request.POST['msg']
        ins = Contact(contact_name=name,contact_email=email,contact_phone=phone,contact_message=msg)
        ins.save()
    return render(request,'folio/index.html')
