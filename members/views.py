#render() combines: loading the template, creating the context, and returning the HTTP response — all in one step.
#It's more readable and clean.
from django.shortcuts import render
from .models import Member

def all_members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'all_members.html', {'mymembers': mymembers})

def details(request, id):
    mymember = Member.objects.get(id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'main.html')
from django.shortcuts import render

def testing(request):
    return render(request, 'template.html',{'fruits': ['Apple', 'Banana', 'Cherry']})