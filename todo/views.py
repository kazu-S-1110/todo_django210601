from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel


class TodoList(ListView):
    template_name = "list.html"  # htmlファイルを指定する
    model = TodoModel  # modelを指定する（このクラスが呼び出すデータベースを指定している感じ）


class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel
