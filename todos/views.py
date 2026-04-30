from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm
# Display all todos
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/list.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todos = context['todos']
        completed_count = todos.filter(completed=True).count()
        pending_count = todos.filter(completed=False).count()
        context.update({
            'total_tasks': todos.count(),
            'completed_count': completed_count,
            'pending_count': pending_count,
        })
        return context
# Create a new todo
class TodoCreateView(CreateView):
 model = Todo
 form_class = TodoForm
 template_name = 'todos/todo_form.html'
 success_url = reverse_lazy('todo_list')
# Delete a todo
class TodoDeleteView(DeleteView):
 model = Todo
 template_name = 'todos/todo_confirm_delete.html'
 success_url = reverse_lazy('todo_list')
# Mark todo as complete/incomplete
def toggle_todo(request, pk):
 todo = get_object_or_404(Todo, pk=pk)
 todo.completed = not todo.completed
 todo.save()
 return redirect('todo_list')
