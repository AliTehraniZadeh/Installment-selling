from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


router.register('user_api/', views.UserView )
router.register('shop_api/', views.ShopView)
router.register('branch_api/', views.BranchView)
router.register('product_api/', views.ProductView)
router.register('check_api/', views.CheckView)
router.register('installment_api/', views.InstallmentViews)

urlpatterns = [
    path('api/', include(router.urls))
]