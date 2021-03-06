"""Project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Project01.views import greeting, bye, get_current_date, calculate_age, c_course, css_course


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', greeting),
    path('bye/', bye),
    path('current_date', get_current_date),
    path('age/<int:age>/<int:year>', calculate_age),
    path('c_course/', c_course),
    path('css_course/', css_course)
]
