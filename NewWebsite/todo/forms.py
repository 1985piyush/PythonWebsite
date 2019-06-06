from django import forms
from .models import Todo
class TodoForm(forms.Form):
	text=forms.CharField(max_length=20,
		widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Enter todo ", 
			'aria-label':"Todo", 'aria-describedby':"add-btn"}))

#Another method of handling form data,saving form data to database
#default display of fields is ugly, thats why using widgets
#specify for which field you want to add widget for using dictionary

class NewTodoForm(forms.ModelForm):
	class Meta:
		model =Todo
		fields=['text']
		widgets={
				'text':forms.TextInput(attrs={'class':"form-control", 'placeholder':"Enter todo ", 
			'aria-label':"Todo", 'aria-describedby':"add-btn"})
		}