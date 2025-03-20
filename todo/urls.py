from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  TodoDetailApiView,BookViewSet


router=DefaultRouter()
router.register(r'book',BookViewSet,basename='books')



urlpatterns = [
    path('', include(router.urls)),
    path('tododetail/<int:id>/', TodoDetailApiView.as_view),
]