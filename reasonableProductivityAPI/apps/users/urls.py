from django.urls import path
from apps.users import views



app_name = "users"
urlpatterns = [
    path('', views.UserCreateAPIView.as_view(), name='usercreate'),
    path('<pk>', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('<pk>/profile/', views.UserProfileCreateListAPIView.as_view(), name='user-detail'),

]