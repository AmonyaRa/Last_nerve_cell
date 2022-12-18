from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account.views import RegisterApiView, ActivationApiView, ForgotPasswordApiView, ForgotPasswordCompleteApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordCompleteApiView.as_view())
]

