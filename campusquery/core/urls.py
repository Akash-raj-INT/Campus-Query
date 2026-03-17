from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask_question, name='ask_question'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes/upload/', views.upload_note, name='upload_note'),
    path('mentors/', views.mentor_matching, name='mentor_matching'),
    path('mentors/profile/', views.create_or_update_mentor_profile, name='mentor_profile'),
    path('search/', views.search, name='search'),
]
