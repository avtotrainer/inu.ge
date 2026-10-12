from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello World from Django on Oracle Cloud!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
]
