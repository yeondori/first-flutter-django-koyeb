import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializers

# Create your views here.
@api_view(['GET'])
def helloAPI(requist):
    return Response("hellow world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializers(randomQuizs, many=True)
    return Response(serializer.data)