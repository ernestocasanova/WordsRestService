from rest_framework.viewsets import ModelViewSet
from app.api.serializers import WordsSerializer
from app.api.models import Words

class WordsViewSet(ModelViewSet):
    """
    API endpoint that allows words to be viewed or edited - full crud.
    """
    queryset = Words.objects.all().order_by('-created')
    serializer_class = WordsSerializer