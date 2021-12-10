from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context={
    "WebmasterName":"Name- Shyed Shahriar Housaini",
    "WebmasterEmail":"E-mail- shyed2001@yahoo.com",
    "Website":"Website- https://www.digialbd.org"
  }
  return render(request, 'index.html', context)
 # return HttpResponse("This is Home Page")

def about(request):
  #return HttpResponse("This is About Page")
  return render(request, 'about.html', context)


def services(request):
  return render(request, 'services.html', context)
  
  
  """ return HttpResponse('''This is About services page \n
                      This is About services page \n
                      This is About services page ''') """

def contact(request):
  return render(request, 'contact.html', context)
  # return HttpResponse("This is About contact page")