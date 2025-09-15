from rest_framework.viewsets import ModelViewSet

from polls.models import Question

from .serializers import PollsSerializer


class PollsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = PollsSerializer