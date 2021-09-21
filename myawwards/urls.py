from django.conf.urls import url
from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from . import views 

# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/',views.register,name='register'),
    path('accounts/login/',views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'django_registration/logout.html'),name='logout'),
    path('accounts/profile/',views.profile,name='profile'),
    path('update/',views.update_profile,name='update_profile'),
    path('post/',views.post_project,name='post'),
    path('project/<int:project_id>',views.detail,  name='project.detail'),
    # path('api/projects/',app_views.ProjectList.as_view()),
    # path('api/profiles/',app_views.ProfileList.as_view()),
    # path('api_token/', obtain_auth_token),
    path(r'^search/$',views.search,name='search'),
    # re_path(r'^users/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'),
    # re_path(r'^delete/(?P<project_id>\d+)$',app_views.delete,name='delete'),
]
# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)