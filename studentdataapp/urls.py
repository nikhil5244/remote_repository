from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('addstudent',views.add_student_view),
    path('create',views.save_data_view),
    path('edit/<id>',views.edit_view),
    path('update/<id>',views.save_edit_data),
    path('delete/<id>',views.delete_view)

]
