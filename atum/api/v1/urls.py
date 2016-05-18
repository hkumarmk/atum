from django.conf.urls import url, include
from . import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'datacenters', views.DatacenterViewSet, base_name='datacenter')
dc_router = routers.NestedSimpleRouter(router, r'datacenters', lookup='dc')
dc_router.register(r'flavors', views.FlavorViewSet, base_name='flavor')
dc_router.register(r'images', views.ImageViewSet, base_name='image')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(dc_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
