# 📝 Task Management System
<sub><b>Author: Ikramul Hasan Rakib</b></sub>

A Python-based Task Management System that allows users to add, update, view, and complete tasks. The system tracks task details like creation time, update time, and completion time, and organizes tasks into incomplete and completed categories.

---

## Features

### 🗂️ Task Management
- Add new tasks with names and track task ID, creation time, and completion status.
- Update existing tasks with new names and track update time.
- Mark tasks as completed and track completion time.

### 📅 View Tasks
- View all tasks, both completed and incomplete.
- See the task ID, name, creation time, and completion status.
  
### 📝 Task Completion
- Mark incomplete tasks as completed.
- Prevent duplicate task completions and track task status.

### 🔄 Task Updates
- Update the name of a task and track when the task was last updated.

---

## How It Works

1. **Add New Task**: Add a task by providing a task name. The system generates a unique task ID and logs the creation time.
2. **View All Tasks**: View all tasks (both completed and incomplete) with their details.
3. **View Incomplete Tasks**: View tasks that have not been completed yet.
4. **View Completed Tasks**: View tasks that have been marked as completed.
5. **Update Task**: Modify the name of an existing task.
6. **Complete Task**: Mark a task as completed, which moves it to the completed task list and records the completion time.

---

## Code Structure

### Classes

- **TaskProperty**: Manages the properties of each task, including ID, name, creation time, update time, and completion status.
- **TaskManagement**: Manages the overall task system, including adding, viewing, updating, and completing tasks.

---

## Example

```python
# Create an instance of TaskManagement
tasks = TaskManagement()

# Sample operations
while(1): 
    print('1. Add New Task') 
    print('2. Show All Tasks')
    print('3. Show Incomplete Tasks')
    print('4. Show Completed Tasks')
    print('5. Update Task')
    print('6. Mark A Task Completed')

    choice = int(input('\nEnter Option : '))
    
    if choice == 1: 
        tasks.add_task()  # Add new task
    elif choice == 2: 
        tasks.show_all_tasks()  # Show all tasks
    elif choice == 3: 
        tasks.show_incomplete_tasks()  # Show incomplete tasks
    elif choice == 4: 
        tasks.show_completed_tasks()  # Show completed tasks
    elif choice == 5: 
        tasks.update_task()  # Update a task
    elif choice == 6: 
        tasks.mark_completed()  # Mark a task as completed
    else: 
        break  # Exit the program
