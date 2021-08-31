from django.urls import path
from .views import (
    SnackListView,
    SnackDetailsView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView
)

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailsView.as_view(), name='snack_detail'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='update_snack'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete_snack')
]
