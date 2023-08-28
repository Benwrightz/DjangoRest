from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppBarViewSet, PortellViewSet, LandingViewSet, BodyViewSet, ContactViewSet, MessageViewSet, Home

router = DefaultRouter()
router.register(r'appbar', AppBarViewSet)
router.register(r'portell', PortellViewSet)
router.register(r'landing', LandingViewSet)
router.register(r'body', BodyViewSet)
router.register(r'message', MessageViewSet)
router.register(r'contact', ContactViewSet) 
urlpatterns = [
   #path("api/", include(router.urls)),
   
   
]
try:
    urlpatterns += [
        path('', Home),
        path("api/", include(router.urls)),
     
    ]
except Exception as e:
    print("An error occurred while adding URL patterns:", e)
