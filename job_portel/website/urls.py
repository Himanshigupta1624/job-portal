from django.urls import path
from . import views
urlpatterns = [
    path('',views.logout_and_redirect_home,name='home'),
    path('job-listing/',views.job_listing,name='job-listing'),
    path('job-details/<int:pk>/',views.job_details,name='job-details'),
]