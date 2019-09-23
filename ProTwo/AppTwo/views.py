from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>App Two!</em>")

def help(request):
    my_dic = {'help' : "HELP PAGE"}
    return render(request, "AppTwo/help.html", context=my_dic)

def user(request):
    user_list = User.objects.order_by('last')
    u = {'user': user_list}
    return render(request, 'AppTwo/user.html', context=u)
