
from django.urls import path,include
from . import views

urlpatterns = [
    path('student/', views.studentview),
    path('student/<int:pk>/',views.studentdetailview),
    
    path('teacher/', views.Teacher.as_view()),
    path('teacher/<int:pk>/',views.Teacherdetail.as_view()),
    
    path('stuff/', views.StuffListCreateView.as_view()),
    path('stuff/<int:pk>/',views.StuffDetailView.as_view()),
    
    path('parents/', views.ParentsListCreateView.as_view()),
    path('parents/<int:pk>/',views.ParentsDetailView.as_view()),

]
