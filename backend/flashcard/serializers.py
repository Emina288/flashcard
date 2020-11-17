from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flashcard
    fields = ('id', 'question', 'answer', 'learned', 'author', 'category')