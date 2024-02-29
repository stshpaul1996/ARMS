from arms.viewsets import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users',SampleViewset, basename= 'users')
router.register(r'role',roleViewSet, basename= 'Role')
router.register(r'trip',tripViewSet,basename= 'Trip')
router.register(r'member',memberViewSet,basename= 'Member')
router.register(r'expenses',expensesViewSet,basename= 'Expenses')
router.register(r'permission',PermissionViewSet,basename= 'Permission')
router.register(r'api',ApiViewSet,basename= 'Api')
# router.register(r'sam',SamView,basename= 'Sam')


urlpatterns = [
    # path('bunny',SampleViewset.as_view()),
    path('trip/expense/<int:pid>',TripExpenseView.as_view()),
    
]+ router.urls