from django.urls import path
from .views import EntryListCreate, EntryRetrieveUpdateDestroy

urlpatterns = [
  path('', EntryListCreate.as_view(), name='entry_list_create'),
  path('<int:pk>/', EntryRetrieveUpdateDestroy.as_view(), name='entry_retrieve_update_destroy'),
]