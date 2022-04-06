from django.urls import path
from .views import (HomeView, ThankYouView, ContactFormView, 
                    TeacherCreateView, TeacherListView, 
                    TeacherDetailView, TeacherUpdateView,
                    TeacherDeleteView)

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('thanks/', ThankYouView.as_view(), name="thankyou"),
    path('contact/', ContactFormView.as_view(), name="contact"),
    path('teacher/', TeacherCreateView.as_view(), name="teacher"),
    path('teacherlist/', TeacherListView.as_view(), name="teacherlist"),
    path('teacherdetail/<int:pk>/', TeacherDetailView.as_view(), name="teacherdetail"),
    path('teacherupdate/<int:pk>/', TeacherUpdateView.as_view(), name="teacherupdate"),
    path('teacherdelete/<int:pk>/', TeacherDeleteView.as_view(), name="teacherdelete"),
]