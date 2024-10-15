from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# list all the pages here
def home(request):
    return HttpResponse("""<h1> Hello, Django from home</h1>, <p> Digitalbd org </p> <br> <a href='/index'>Index</a> <br>, <a href='/Viewindex'>Viewindex</a> <br> <a href='/wfb'>wfb</a> <br> <a href='AppDjDemo1/baseTemplateDemo'>baseTemplateDemo</a> <br> <a href='AppDjDemo1/HomeTemplateDemo'>HomeTemplateDemo</a>""")


def index(request):
    return HttpResponse("<h1> Hello, Django from index </h1>, <p> Digitalbd org </p>")

 
def Viewindex(request):
    return HttpResponse("<h1> Hello, Django from Viewindex </h1>, <p> Digitalbd org </p>")


def numbers(request, Numbers):
    return HttpResponse("<h1> %s </h1>, <p> Digitalbd org </p>" % Numbers)


def Member_Names(request, Names):
    return HttpResponse("<h1> %s </h1>, <p> Digitalbd org </p>" % Names)


def wfb(request):
    return HttpResponse("""
        <h1>
            <a href='https://www.techempower.com/benchmarks/#section=data-r22&test=fortune&o=c'> 
            Web Framework Benchmarks techempower
            </a>
        </h1> 
        <p> Digitalbd org </p>
        <br/>
        <h1>
            <a href='https://web-frameworks-benchmark.netlify.app'> 
            Web Frameworks Benchmark  netlify
            </a>
        </h1>
        <p> Digitalbd org </p>
    """)


# def baseDemo(response):
#     return render(response, 'AppDjDemo1/base.html')

# def homeDemo(response):
#     return render(response, 'AppDjDemo1/home.html')

def baseTemplateDemo(response):
    return render(response, "AppDjDemo1/baseTemplateDemo.html",{})


def HomeTemplateDemo(response):
    return render(response, "AppDjDemo1/HomeTemplateDemo.html",{})

# End of file
