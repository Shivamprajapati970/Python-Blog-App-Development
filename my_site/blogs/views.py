from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts=[
    {
        "author":"Shivam Prajapati",
        "date_posted":datetime.now(),
        "title":"First Post",
        "content":"This is a sample post",
    },
    {
        "author":"Shivam Prajapati",
        "date_posted":datetime.now(),
        "title":"Second Post",
        "content":"This is a sample post",
    }

]

# Create your views here.
def home(request):
    context={
        'title':'HOME PAGE',
        'posts':posts,
    }
    return render(request, template_name='blogs/home.html',context=context)

def about(request):
    return render(request, template_name='blogs/about.html')