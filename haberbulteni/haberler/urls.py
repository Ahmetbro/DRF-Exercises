from django.urls import path
from haberler import views as api_views

# urlpatterns = [
#     path('makaleler/', api_views.makale_list_create_api_view, name='makale-listesi'),
#     path('makaleler/<int:pk>', api_views.makale_detail_api_view, name='makale-detay'),
# ]

urlpatterns = [
    path('makaleler/', api_views.MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('makaleler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name='makale-detay'),
    path('gazeteci/', api_views.GazeteciListCreateAPIView.as_view(), name='gazeteci-listesi'),
    path('gazeteci/<int:pk>', api_views.GazeteciDetailAPIView.as_view(), name='gazeteci-detail'),
]