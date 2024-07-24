from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.login, name="login"),
    re_path(r'^submit/expense/$', views.submit_expense, name="submit_expense"),
    re_path(r'^submit/income/$', views.submit_income, name="submit_income"),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^home/$', views.home, name="home"),
]

