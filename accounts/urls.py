from django.urls import path
from accounts import views

urlpatterns = [
    path('login_page',views.login_page,name='login_page'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('login_handle',views.login_handle,name='login_handle'),
    path('signup_handle',views.signup_handle,name='signup_handle'),
    path('logout_handle',views.logout_handle,name='logout_handle'),
    path('author_page',views.user_dashboard,name='author_page'),

]
