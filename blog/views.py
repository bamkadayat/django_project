from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author':'Bam', 'title':'Blog post one', 'content':'first content', 'date_posted':'May 20, 2020'},
    {'author':'Baneet', 'title':'Blog post two', 'content':'first content', 'date_posted':'May 30, 2020'}
]
def home(request):
    context = {
        'posts':posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
