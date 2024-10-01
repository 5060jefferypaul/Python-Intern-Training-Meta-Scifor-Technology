from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Student', views.Student, name='Student'),
    path('student_details', views.student_details, name='student_details'),
    path('student_showpage', views.student_showpage, name='student_showpage'),
    path('student_editpage/<int:pk>', views.student_editpage, name='student_editpage'),
    path('edit_student_details/<int:pk>', views.edit_student_details, name='edit_student_details'),
    path('admit_card_student/<int:pk>', views.admit_card_student, name='admit_card_student'),
    path('delete_page_student/<int:pk>', views.delete_page_student, name='delete_page_student'),

    path('Teacher', views.Teacher, name='Teacher'),
    path('teacher_details', views.teacher_details, name='teacher_details'),
    path('teacher_showpage', views.teacher_showpage, name='teacher_showpage'),
    path('teacher_editpage/<int:pk>', views.teacher_editpage, name='teacher_editpage'),
    path('edit_teacher_details/<int:pk>', views.edit_teacher_details, name='edit_teacher_details'),
    path('admit_card_teacher/<int:pk>', views.admit_card_teacher, name='admit_card_teacher'),
    path('delete_page_teacher/<int:pk>', views.delete_page_teacher, name='delete_page_teacher'),
]
