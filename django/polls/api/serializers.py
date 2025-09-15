from rest_framework.serializers import ModelSerializer

from polls.models import Question


class PollsSerializer(ModelSerializer):
   class Meta:
       model = Question
       fields = ['id', 'question_text', 'pub_date']