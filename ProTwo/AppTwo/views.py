from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import SignUp

# Create your views here.
def index(request):
    return HttpResponse("<em>App Two!</em><br><br> <h2 align='center'>Try: /help, /signup, or /user<h2>")

def help(request):
    my_dic = {'help' : "HELP PAGE"}
    return render(request, "AppTwo/help.html", context=my_dic)

def user(request):
    user_list = User.objects.order_by('last')
    u = {'user': user_list}
    return render(request, 'AppTwo/user.html', context=u)

def form_name(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR! FORM INVALID")

    return render(request, "AppTwo/signup.html", {'sign_form': form})

