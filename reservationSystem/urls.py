from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet
from persons.views import PersonViewSet
from resourses.views import ResouserViewSet

router = DefaultRouter()
router.register(r'resources', ResouserViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),

]