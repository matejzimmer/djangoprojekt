from django.urls import path
from .views import CtenarDetailView, CtenarListView, KnihovnaListView, KnihovnaDetailView, index

urlpatterns = [
    path('', index, name='index'),
    path('ctenari/', CtenarListView.as_view(), name='ctenari_list'),
    path('ctenari/<int:pk>/', CtenarDetailView.as_view(), name='ctenari_detail'),
    path('knihovny/', KnihovnaListView.as_view(), name='knihovny_list'),
    path('knihovny/<int:pk>/', KnihovnaDetailView.as_view(), name='knihovna_detail')

]
