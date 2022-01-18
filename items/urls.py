from django.urls import path

from .views import BaseViewSet

urlpatterns = [
    path('latest/', BaseViewSet.latest_news),
    path('top', BaseViewSet.top_news),
    path('create/', BaseViewSet.create_news),
    path('update/<id>/', BaseViewSet.update_news_by_id),
    path('delete/<id>/', BaseViewSet.delete_news_by_id)
]
