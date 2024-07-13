from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^submit/expense/$', views.submit_expense, name="submit_expense"),
    re_path(r'^submit/income/$', views.submit_income, name="submit_income"),
    re_path(r'^login/$', views.logout, name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
]

