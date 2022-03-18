from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'publisher', views.PublisherViewSet)
router.register(r'imageObject', views.ImageObjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token-auth/', TokenObtainPairView.as_view())
]
