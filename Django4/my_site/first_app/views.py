from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page',
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR")

def add_view(request, num1, num2):
    result = num1+num2
    return HttpResponse(str(result))

def num_page_view(request, num_page):
    topics_list = list((articles.keys()))
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))

def simple_view(request):
    return render(request, 'first_app/example.html')