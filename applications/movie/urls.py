from rest_framework.routers import DefaultRouter
from applications.movie.views import *

router = DefaultRouter()
router.register('category', GenreApiView)
router.register('comment', ReviewApiView)
router.register('actor', ActorApiView)
router.register('', MovieApiView)

urlpatterns = router.urls
