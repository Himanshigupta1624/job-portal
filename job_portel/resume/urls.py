from django.urls import path
from . import views
urlpatterns = [
    path('update-resume/',views.update_resume,name='update-resume'),
    path('modify-resume/',views.modify_resume,name='modify-resume'),
    
]