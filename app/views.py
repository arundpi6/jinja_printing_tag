from django.shortcuts import render

# Create your views here.

def jinja_tag(request):
    d={'data':'CSK WIN THE TROPHY IN IPL 2024'}
    return render(request,'jinja_tag.html',d)