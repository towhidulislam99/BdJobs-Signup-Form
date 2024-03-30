from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/', CreateSkills),
    path('skills_update/<int:pk>/', Update_skills),
    path('country/', CreateCountry),
    path('country_update/<int:pk>/', Update_country),
    path('createaccount/', CreateUserRegistration),
    path('account_update/<int:pk>/', Update_UserRegistration),
]