from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet
from persons.views import PersonViewSet,ProfileList
from resourses.views import ResouserViewSet

router = DefaultRouter()
router.register(r'user', PersonViewSet)
router.register(r'resources', ResouserViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
   # url(r'')
    path('admin/', admin.site.urls),
]

