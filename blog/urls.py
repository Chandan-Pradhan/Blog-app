from django.urls import path

from .views import BolgListView, BlogDetailview, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailview.as_view(), name='post_detail'),
    path('', BolgListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete')
]
