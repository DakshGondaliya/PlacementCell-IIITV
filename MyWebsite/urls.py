from django.conf.urls import url

from MyWebsite import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^student/$', views.student, name='student'),
    url(r'^recruiter/$', views.recruiter, name='recruiter'),
    url(r'^about/$', views.about, name='about'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^academic/$', views.academic, name='academic'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^department/$', views.department, name='department'),
    url(r'^recruiter/form$', views.recruiter_form, name='recruiter_form'),
    ]