from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Entry
from .serializers import EntrySerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class EntryListCreate(ListCreateAPIView):
  queryset = Entry.objects.all()
  serializer_class = EntrySerializer

class EntryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Entry.objects.all()
  serializer_class = EntrySerializer
  permission_classes = (IsAuthorOrReadOnly,)