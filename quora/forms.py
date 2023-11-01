from django import forms
from .models import Question, Answer


class CustomTextareaForQuestion(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(CustomTextareaForQuestion, self).__init__(*args, **kwargs)
        self.attrs.update({'style': 'height: 75px;', 'placeholder': 'what do you think today ?'})


class CustomTextareaForAnswer(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(CustomTextareaForAnswer, self).__init__(*args, **kwargs)
        self.attrs.update({'style': 'height: 75px;', 'placeholder': 'Enter your answer here '})


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = CustomTextareaForQuestion()
        self.fields['text'].label = ''


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = CustomTextareaForAnswer()
        self.fields['text'].label = ''