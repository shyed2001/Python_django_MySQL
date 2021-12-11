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

def pages(request):
  #return HttpResponse("This is About Page")
  return render(request, 'pages.html', context)

def documentations(request):
  #return HttpResponse("This is About Page")
  return render(request, 'documentations.html', context)

def service(request):
  return render(request, 'services.html', context)

  """ return HttpResponse('''This is About services page \n
                      This is About services page \n
                      This is About services page ''') """
                        
def blogs(request):
  return render(request, 'blogs.html', context)

def directions(request):
  return render(request, 'directions.html', context)


def products(request):
  return render(request, 'products.html', context)


def locations(request):
  return render(request, 'locations.html', context) 


def links(request):
  return render(request, 'links.html', context) 


def contacts(request):
  context={
    "WebmasterName":"Name- Shyed Shahriar Housaini",
    "WebmasterEmail":"E-mail- shyed2001@yahoo.com",
    "Website":"Website- https://www.digialbd.org"
  }
  return render(request, 'contacts.html', context)
  # return HttpResponse("This is About contact page")
  
def disclaimer(request):
  context={
    "WebmasterName":"Name- Shyed Shahriar Housaini",
    "WebmasterEmail":"E-mail- shyed2001@yahoo.com",
    "Website":"Website- https://www.digialbd.org"
  }  
  
  return render(request, 'disclaimer.html', context),
 
def privacypolicy(request):
  context={
    "WebmasterName":"Name- Shyed Shahriar Housaini",
    "WebmasterEmail":"E-mail- shyed2001@yahoo.com",
    "Website":"Website- https://www.digialbd.org"
  }
  
  return render(request, 'privacypolicy.html', context)