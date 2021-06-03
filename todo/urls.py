from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path("list", TodoList.as_view()),
    path("detail/<int:pk>", TodoDetail.as_view()),  # pk(primary keyが必要となるため指定してあげる)
    path("create/", TodoCreate.as_view()),
]
