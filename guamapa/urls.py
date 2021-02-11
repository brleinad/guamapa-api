from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_nested import routers
from .users.views import UserViewSet, UserCreateViewSet
from .towns.views import TownViewSet, AssistantMayorViewSet, SurveyAnswerViewSet, SurveyQuestionViewSet, NestedSurveyAnswerViewSet

router = DefaultRouter()
nested_router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'towns', TownViewSet)
router.register(r'assistant-mayors', AssistantMayorViewSet)
router.register(r'survey-questions', SurveyQuestionViewSet)
router.register(r'survey-answers', SurveyAnswerViewSet)

nested_router.register(r'towns', TownViewSet)
towns_router = routers.NestedSimpleRouter(nested_router, r'towns', lookup='town')
towns_router.register(r'survey-answers', NestedSurveyAnswerViewSet) #, basename='towns-assistant-mayors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('api/v1/', include(nested_router.urls)),
    path('api/v1/', include(towns_router.urls)),
    # path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
