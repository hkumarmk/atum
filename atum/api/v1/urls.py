from django.conf.urls import url, include
from . import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'datacenters', views.DatacenterViewSet, base_name='datacenter')
dc_router = routers.NestedSimpleRouter(router, r'datacenters', lookup='dc')
dc_router.register(r'flavors', views.FlavorViewSet, base_name='flavor')
dc_router.register(r'images', views.ImageViewSet, base_name='image')
dc_router.register(r'regions', views.RegionViewSet, base_name='region')
dc_router.register(r'sshkeys', views.SSHKeyViewSet, base_name='sshkey')
dc_router.register(r'floatingips', views.FloatingIPViewSet, base_name='floatingip')
dc_router.register(r'tags', views.TagViewSet, base_name='tag')
dc_router.register(r'domains', views.DomainViewSet, base_name='domain')
dc_router.register(r'servers', views.ServerViewSet, base_name='server')

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^', include(router.urls)),
    url(r'^', include(dc_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
