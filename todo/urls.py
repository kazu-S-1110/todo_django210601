from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path("list", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),  # pk(primary keyが必要となるため指定してあげる)
    path("create/", TodoCreate.as_view(), name="create"),  # nameを付与してreversed_lazyで指定可能にする
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"),

]
