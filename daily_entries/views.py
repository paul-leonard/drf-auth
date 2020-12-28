from rest_framework.generics import ListCreateAPIView
from .models import Entry
from .serializers import EntrySerializer

# Create your views here.

class EntryListCreate(ListCreateAPIView):
  queryset = Entry.objects.all()
  serializer_class = EntrySerializer