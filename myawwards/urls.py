from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from django.conf import settings
from django.conf.urls.static import static

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
    path('api/projects/',views.ProjectList.as_view()),
    # path('api/profiles/',views.ProfileList.as_view()),
    # path('api_token/', obtain_auth_token),
    path('search/$',views.search,name='search'),
    path('users/(?P<pk>\d+)',views.users_profile,name='users_profile'),
    path('delete/(?P<project_id>\d+)',views.delete,name='delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)