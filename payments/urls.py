from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentsListAPIView, PaymentsCreateAPIView, PaymentsRetrieveAPYView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/retrieve/<int:pk>/', PaymentsRetrieveAPYView.as_view(), name='payments_retrieve'),
]
