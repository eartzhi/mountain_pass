from rest_framework import routers
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *


router = routers.DefaultRouter()
router.register(r'author', AuthorViewset)
router.register(r'coords', CoordsViewset)
router.register(r'images', PerevalImagesViewset)
router.register(r'level', LevelViewset)
router.register(r'perevaladd', PerevalAddedViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                             namespace='rest_framework')),
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url': 'openapi-schema'}
    # ), name='swagger-ui'),
]