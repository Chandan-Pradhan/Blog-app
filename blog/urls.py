from django.urls import path

from .views import BolgListView, BlogDetailview

urlpatterns = [
    path('post/<int:pk>/', BlogDetailview.as_view(), name='post_detail'),
    path('', BolgListView.as_view(), name='home'),                          #urlconf
]
