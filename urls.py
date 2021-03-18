from django.urls import path
from django.contrib import admin
from .views import Home,PostDetail,PostCreate,Dashboard,PostUpdate,PostDelete,PostCategory

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('post/cat/<int:pk>/', PostCategory.as_view(), name='post_by_category'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/add/', PostCreate.as_view(), name='post_add'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
