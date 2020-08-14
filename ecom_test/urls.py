from django.urls import path
from .views import ProdListView, ProdCreateView, ProdDeleteView, ProdDetailView, ProdUpdateView
from . import views

urlpatterns = [
    path('', ProdListView.as_view(), name='home'),
    path('product/<int:pk>/', ProdDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', ProdUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProdDeleteView.as_view(), name='product-delete'),
    path('product/new/', ProdCreateView.as_view(), name='product-create')
]
