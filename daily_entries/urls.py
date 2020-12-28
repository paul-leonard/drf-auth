from django.urls import path
from .views import EntryListCreate

urlpatterns = [
  path('', EntryListCreate.as_view(), name='entry_list_create'),
]