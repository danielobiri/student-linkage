from django.contrib import admin
from django.urls import path, include
from user.views import (
    login_view,
    signup_view,
    logout,
    get_user,
    basic_profile,
    uni_verification,
    save_degree,
    save_research,
    save_publication,
    mark_complete,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from app import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/login/", login_view),
    path("api/user/get/", get_user),
    path("api/profile/basic/", basic_profile),
    path("api/profile/university/", uni_verification),
    path("api/profile/degree/", save_degree),
    path("api/profile/publication/", save_publication),
    path("api/profile/research/", save_research),
    path("api/profile/complete/", mark_complete),
    path("api/signup/", signup_view),
    path("api/logout/", logout),
    path("api/", include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
