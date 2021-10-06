# Python_django_MySQL
Python_django_MySQL
install postman for api testing
PS :\GitHub\Python_django_MySQL> history

  Id     Duration CommandLine
  --     -------- -----------
   1     pip install django

   3     pip install djangorestframework

   4     pip install djang-cors-headers

   5     pip install django-cors-headers


roblems running django-admin¶
“command not found: django-admin”¶
django-admin should be on your system path if you installed Django via pip. If it’s not on your path, you can find it in site-packages/django/bin, where site-packages is a directory within your Python installation. Consider symlinking to django-admin from some place on your path, such as /usr/local/bin.

If django-admin doesn’t work but django-admin.py does, you’re probably using a version of Django that doesn’t match the version of this documentation. django-admin is new in Django 1.7.

django-admin startproject DjangoAPI

