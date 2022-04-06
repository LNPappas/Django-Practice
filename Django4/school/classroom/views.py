from attr import fields
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView, 
                                  CreateView, ListView, DetailView, 
                                  UpdateView, DeleteView)
from classroom.models import Teacher
from classroom.forms import ContactForm

class HomeView(TemplateView):
    template_name = "classroom/home.html"
    
class ThankYouView(TemplateView):
    template_name = "classroom/thankyou.html"
    
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"
    # success_url = "/classroom/thanks/"
    success_url = reverse_lazy('classroom:thankyou')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacherlist')
    
class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teacher_list"
    queryset = Teacher.objects.order_by('subject')
    
class TeacherDetailView(DetailView):
    # model_detail.html - teacher_detail.html
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['subject']
    success_url = reverse_lazy('classroom:teacherlist')
    
class TeacherDeleteView(DeleteView):
    # model_confirm_delete.html - teacher_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:teacherlist')