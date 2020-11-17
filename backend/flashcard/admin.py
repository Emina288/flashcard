from django.contrib import admin
from .models import Flashcard 

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "learned", "author", "category")


admin.site.register(Flashcard, FlashcardAdmin)
