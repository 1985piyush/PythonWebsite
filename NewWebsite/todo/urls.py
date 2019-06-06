from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('complete/<todo_id>',views.complete,name='complete'),
    path('delall/',views.deleteAll,name='delall'),
    path('delcmp/',views.deleteCompleted,name='delcmp')
]
