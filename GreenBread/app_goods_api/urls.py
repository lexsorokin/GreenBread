from django.urls import path
from app_categories.views import GoodList, GoodDetail

urlpatterns = [
    path('goods_list/', GoodList.as_view()),
    path('goods_list/<int:pk>', GoodDetail.as_view())
]