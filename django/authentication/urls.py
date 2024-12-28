from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path(
        'authentication/', TokenObtainPairView.as_view(), name='obtem-token'
    ),
    # path(
    #     'authentication/token/resfresh/', TokenRefreshView.as_view(), name='update-token'
    # ),
    # path(
    #     'authentication/token/verify/', TokenVerifyView.as_view(), name='verify-token'
    # ),
]
