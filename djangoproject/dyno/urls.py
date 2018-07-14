from django.urls import path

from . import views

from dyno.views import home, ContactView, success, form, dashboard, diagnose

app_name = 'dyno'
urlpatterns = [
    # starting view, has list of all other links
    path('home', home.as_view(), name='home'),
    path('contact', ContactView.as_view(), name = 'ContactView'),
    path('success', success.as_view(), name = 'success'),
    path('form', form.as_view(), name = 'form'),
    path('dashboard', dashboard.as_view(), name = 'dashboard'),
    path('diagnose', diagnose.as_view(), name = 'diagnose'),
]
