
from django.shortcuts import render, redirect
from .models import Todo

# =================================== VIEWS HERE =========================

def home(request):    
    return render(request, "home.html")
def rights(request):
    return render(request,'rights.html')
def about(request):
    return render(request,'about.html')

# ====================================== TODO =========================================

def todo(request):
    
    todos = Todo.objects.all()
    
    parameters = {
        "todos": todos,
    }
    
    return render(request, "todo.html", parameters)

# ===================================== ADD TODO =======================================

def add_todo(request):
    
    if request.method == "POST":
        
        # Template s view m data la rha hu
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        # View vala data model m save kr rha hu
        new_todo = Todo(
            task=user_task, 
            created_at=user_created_at
            )
        new_todo.save()
        
        return redirect("todo")
        
    return render(request, "add_todo.html")

# ================================== DELETE TODO ===================================

def delete_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    todo.delete()

    return redirect("todo")

# ================================== UPDATE TODO ==========================

def update_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        todo.task = user_task
        todo.created_at = user_created_at
        
        todo.save()
        
        return redirect("todo")
    
    parameters = {
        'todo': todo
    }
    
    return render(request, "update_todo.html", parameters)

# ================================== MARK COMPLETE ================================

def mark_complete(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    
    todo.is_completed = True
    todo.save()
    
    return redirect("todo")
    
