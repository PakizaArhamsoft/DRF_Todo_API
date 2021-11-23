from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Employee CRUD API",
      default_version='v1',
      description="Todo app test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('api/logout /', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('accounts/logout/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('accounts/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]