
from django.urls import path,include
from . import views

urlpatterns = [
    path('student/', views.studentview),
    path('student/<int:pk>/',views.studentdetailview),
    path('teacher/', views.Teacher.as_view()),
    pathI('teacher/<int:pk>/',views.Teacherdetail.as_view),

]
