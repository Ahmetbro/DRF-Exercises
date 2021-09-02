from django import urls
from django.urls import path, include
from rest_framework import routers, urlpatterns
from profiles.views import ProfileViewset
from rest_framework.routers import DefaultRouter

# profile_list = ProfileViewset.as_view({'get':'list'})
# profile_status = ProfileViewset.as_view({'get':'retrieve'})


# urlpatterns = [
#     path('user-profiles/',profile_list , name='profiles'),
#     path('user-profiles/<int:pk>',profile_status , name='profile-status')
    
# ]

router = DefaultRouter()
router.register(r'user-profiles', ProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
]