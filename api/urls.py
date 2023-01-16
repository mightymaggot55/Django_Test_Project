from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ticket', views.TicketViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'asset', views.AssetViewSet)
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
