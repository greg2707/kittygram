from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet


router = SimpleRouter()

router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно


urlpatterns = [
   path('', include(router.urls)),
]
