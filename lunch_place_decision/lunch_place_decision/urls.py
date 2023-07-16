from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from lunch.views import (
    RestaurantCreateView,
    MenuCreateView,
    EmployeeCreateView,
    CurrentDayMenuView,
    CurrentDayResultsView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/restaurant/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('api/menu/', MenuCreateView.as_view(), name='menu-create'),
    path('api/employee/', EmployeeCreateView.as_view(), name='employee-create'),
    path('api/menu/current/', CurrentDayMenuView.as_view(), name='current-day-menu'),
    path('api/results/current/', CurrentDayResultsView.as_view(), name='current-day-results'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
