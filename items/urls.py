from django.urls import path

from items.views import BaseViewSet

urlpatterns = [
    path('latest/', BaseViewSet.latest_news),
    path('top/', BaseViewSet.top_news),
    path('top/detail/<id>', BaseViewSet.top_news_detail_by_id),
    path('create/', BaseViewSet.create_news),
    path('update/<id>/', BaseViewSet.update_news_by_id),
    path('delete/<id>/', BaseViewSet.delete_news_by_id)
]
