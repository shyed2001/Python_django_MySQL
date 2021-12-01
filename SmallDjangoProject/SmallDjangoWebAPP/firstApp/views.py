from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context={
    "variable1":"Shyed",
    "variable2":"Shahriar",
    "variable3":"Housaini",
  }
  return render(request, 'index.html', context)
 # return HttpResponse("This is Home Page")

def about(request):
  return HttpResponse("This is About Page")

def services(request):
  return HttpResponse("This is About services page")

def contact(request):
  return HttpResponse("This is About contact page")