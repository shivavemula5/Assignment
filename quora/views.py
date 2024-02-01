from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from quora.models import Question, Answer, Like
from quora.forms import QuestionForm, AnswerForm

# Hello this is comment one !

@login_required
def home(request):
    form = QuestionForm()
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            return redirect('home')
    return render(request, "../templates/home.html", {"form": form, "questions": questions})


def question_detail(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=id)
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user = request.user
            form_obj = form.save(commit=False)
            form_obj.user = user
            form_obj.question = question
            form_obj.save()
            url = reverse('question_detail', kwargs={'id': id})
            return redirect(url)
    return render(request, "../templates/question_detail.html", {"question": question, "answers": answers, "form":form})


@login_required
def like_answer(request, answer_id):
    user = request.user
    answer = Answer.objects.get(id=answer_id)
    question_id = answer.question.id
    Like.objects.create(user=user, answer=answer)
    url = reverse('question_detail', kwargs={"id": question_id})
    return redirect(url)


def greet(request):
    return "hello"

