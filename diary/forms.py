from django import forms
from diary.models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['goal', 'feelgood', 'productivity', 'metime', 'fftime', 'notes', 'date', 'image',]