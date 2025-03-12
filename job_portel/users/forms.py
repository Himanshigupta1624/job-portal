from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

class RegisterUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['email','password1','password2']
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'first_name', 'last_name', 'is_applicant', 'is_recruiter', 'has_company', 'has_resume')

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'first_name', 'last_name', 'is_applicant', 'is_recruiter', 'has_company', 'has_resume')        