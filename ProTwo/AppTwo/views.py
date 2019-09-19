from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>App Two!</em>")

def help(request):
    my_dic = {'help' : "HELP PAGE"}
    return render(request, "AppTwo/help.html", context=my_dic)
