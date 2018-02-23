from django.conf.urls import url
from django.contrib.auth.views import login

from MyWebsite import views
from MyWebsite.views import recruiter_listview

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^accounts/login/$',login,{'template_name':'Student.html'}, name='login' ),
    url(r'^student/$', views.student, name='student'),
    url(r'^recruiter/$', views.recruiter, name='recruiter'),
    url(r'^about/$', views.about, name='about'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^academic/$', views.academic, name='academic'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^add/student/$', views.addstudent, name='addstudent'),
    url(r'^add/recruiter/$', views.addrecruiter, name='addrecruiter'),
    url(r'^department/$', views.department, name='department'),
    url(r'^recruiter/form$', views.recruiter_form, name='recruiter_form'),
    url(r'^beyond-academic$', views.beyond_academic, name='beyond_academic'),
    url(r'^addBeyondAcademicimage/$', views.add_beyond_academic_images, name='addBeyondAcademicimages'),
    url(r'^add_past_recruiter_image/$', views.add_past_recruiter_image, name='add_past_recruiter_image'),
    url(r'^add-Past-Recruiters-image/$',views.add_pastrecruiters_image,name='add_pastrecruiters_image'),
    url(r'^addBeyondAcademicvideos/$', views.add_beyond_academic_videos, name='addBeyondAcademicvideos'),
    url(r'^addBeyondAcademichighlight/$', views.add_beyond_academic_highlight, name='addBeyondAcademichighlight'),
    url(r'^addinterndescrip/$', views.add_intern_descrip, name='addinterndescrip'),
    url(r'^addngodescrip/$', views.add_ngo_descrip, name='addngodescip'),
    url(r'^change_password/$',views.change_password,name='change_password'),
    url(r'^college-team/$',views.college_team,name='college_team'),
    url(r'^alumni/$',views.alumni,name='alumni'),
    url(r'^research-development/$',views.research_development,name='research_development'),
    url(r'^studentapply/(?P<pk>[\w\-]+)/$',views.studentapply,name='studentapply'),
    url(r'^recruiter-list/$', views.recruiter_listview, name='recruiterlist'),
    url(r'^student/shortlisted/recruiter/$',views.student_shortlisted_recruiter,name='student_shortlisted_recruiter'),
    url(r'^recruiter/shortlisted/student/$',views.recruiter_shortlisted_student,name='recruiter_shortlisted_student'),
    url(r'^recruiter/shortlisted/student/(?P<pk1>[\w\-]+)/$',views.recruiter_shortlisted_student_superuser,name='recruiter_shortlisted_student_superuser'),
    url(r'^add/alumni/$',views.addalumni,name='addalumni'),
    url(r'^add/research/$',views.addresearch,name='addresearch'),
    url(r'^add/team/image/$',views.addteamimage,name='teamimage'),
    url(r'^add/faculty/image/$',views.addfacultyimage,name='facultyimage'),
    url(r'^add/student/image/$',views.addstudentimage,name='studentimage'),
    url(r'^recruiter/quiz/list$',views.recruiter_quizlist,name='recruiter_quizlist'),
    url(r'^add/academic/image/$',views.addacademicimage,name='academicimage'),
    url(r'^add/academic/video/$',views.addacademicvideo,name='academicvideo'),
    url(r'^add/academic/highlight/$',views.addacademichighlight,name='academichighlight')
    ]