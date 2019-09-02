from django.urls import include, path
from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

import testapp

from . import views

urlpatterns = [
    path('login', views.login_action, name="login"),
    path('logout', views.logout_action, name="logout"),
    path('signup', views.signup_action, name="signup"),
    path('message-save', testapp.views.message_save, name='message-save'),
    path('message-load', testapp.views.message_load, name='message-load'),
    path('chatlist-load', testapp.views.chatlist_load, name='chatlist-load'),

    path('rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
]
