from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm,NewTodoForm
from django.views.decorators.http import require_POST
# Create your views here.
# first part is displaying database data to html form
# second part is saving data to the database
def index(request):
	todo_list= Todo.objects.order_by('id')
	#form=TodoForm()
	newtodoform=NewTodoForm()

	#context={'todo_list':todo_list,'form':form}
	context={'todo_list':todo_list,'form':newtodoform}
	return render (request,'todo/index.html',context)
@require_POST
def add(request):
		#form = TodoForm(request.POST)
		#targetting specific field
		'''
		todo_31=Todo.objects.get(pk=31)
		newtodoform=NewTodoForm(request.POST,instance=todo_31)
		'''
		newtodoform =NewTodoForm(request.POST)
		if newtodoform.is_valid():
			new_todo=newtodoform.save()
		'''
		if form.is_valid():
			new_todo =Todo(text=request.POST['text'])
			new_todo.save()
		'''

		return redirect(index)		

def complete(request,todo_id):
	cmpl =Todo.objects.get(pk=todo_id)
	cmpl.completed= True
	cmpl.save()

	return redirect(index)	

def deleteAll(request):
	allTodos =Todo.objects.all()
	for obj in allTodos:
		print(obj.text)
	allTodos.delete()
	return redirect(index)

def deleteCompleted(request):
	completedTodos =Todo.objects.filter(completed='True')
	completedTodos.delete()
	return redirect(index)
	
