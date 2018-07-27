from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^question/$',views.index , name='post_list' ),

    url(r'^$', views.home ),

    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='post_detail'),

    url(r'^post/$',views.view_post,name='view_post'),

    url(r'^login/$', auth_views.login,name='index'),

    url(r'^register/$', views.register,name='index1'),

    url(r'profile/$' , views.profile,name='profile')

]

