from django.urls import path
from quora.views import home, question_detail, like_answer

urlpatterns = [
    path("", home, name="home"),
    path("question/<int:id>/", question_detail, name="question_detail"),
    path("like_answer/<int:answer_id>", like_answer, name="like_answer")
]
