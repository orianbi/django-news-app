from django.urls import path

# import semua class View untuk modul Category

from .views import CategoryListView, CategoryDetailView, NewsListView, NewsDetailView, NewsCreateCommentView


urlpatterns = [
    # membuat route untu API endpoint Category
    path('category/', CategoryListView.as_view(), name='api-category-list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name="api-category-detail"),
    # membuat route untuk API endpoint News
    path('news/', NewsListView.as_view(), name='api-news-list'),
    path('news/<int:pk>/comment', NewsCreateCommentView.as_view(), name="api-news-create-comment"),
    path('news/<int:pk>', NewsDetailView.as_view(), name="api-news-detail"),
]
