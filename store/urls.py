from django.urls import path , include
# from . import views
from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet, CollectionViewSet, home
from . import views
from rest_framework_nested import routers

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('product/', views.products_List.as_view()),
#     path('product/<id>/', views.products_details),
#     path('collection/',views.getCollectionss.as_view()),
# ]



router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')

products_router=routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')



urlpatterns = [
    path('', views.home, name='home'),  # tu gardes ta vue Django normale
    path('', include(router.urls)),  # router prend le reste
    path('', include(products_router.urls)),
]