from django.urls import path

from subscribes.apps import SubscribesConfig
from subscribes.views import SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = SubscribesConfig.name

urlpatterns = [
    path('create/', SubscribeCreateAPIView.as_view(), name='subscribe_create'),
    path('delete/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='subscribe_delete'),
]

