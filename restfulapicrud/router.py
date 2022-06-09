from lipagas.viewsets import GasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('gas', GasViewSet)
