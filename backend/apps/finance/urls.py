from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, basename='accounts')
router.register('categories', CategoryViewSet, basename='categories')
router.register('transactions', TransactionViewSet, basename='transactions')

urlpatterns = router.urls