from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_nested import routers
from .users.views import UserViewSet, UserCreateViewSet
from .towns.views import TownViewSet, AssistantMayorViewSet

router = DefaultRouter()
nested_router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
nested_router.register(r'users', UserCreateViewSet)
nested_router.register(r'towns', TownViewSet)
# router.register(r'assistant-mayor', AssistantMayorViewSet)
towns_router = routers.NestedSimpleRouter(nested_router, r'towns', lookup='town')
towns_router.register(r'assistant-mayors', AssistantMayorViewSet) #, basename='towns-assistant-mayors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(nested_router.urls)),
    path('api/v1/', include(towns_router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include('dj_rest_auth.urls')),
    # path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
