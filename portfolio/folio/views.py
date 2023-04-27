from django.shortcuts import render , HttpResponse
from folio.models import Contact

# Create your views here.

def index(request):
    if request.method=="POST" :
        name = request.POST['lname']
        print(name)
    return render(request,'folio/index.html')
