from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app.forms import FormName

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
   # my_dic = {'insert_me': "Hello from views.py!"}
    return render(request, 'first_app/index.html', context=date_dict)

def kitty(request):
    return render(request, 'first_app/kitty.html')

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(request, 'first_app/form_name.html', {'form':form})