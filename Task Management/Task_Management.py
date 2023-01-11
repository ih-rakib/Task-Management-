from datetime import datetime
import uuid

class TaskProperty :
    @staticmethod
    def get_time() : 
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time

    def __init__(self, name) : 
        self.name = name
        self.id = str(uuid.uuid1())
        self.created_time = self.get_time()
        self.completion_time = 'N/A'
        self.update_time = 'N/A'
        self.task_done = False

    def complete_task(self) : 
        self.task_done = True
        self.completion_time = self.get_time()

    def update_task(self, task) : 
        self.name = task
        self.update_time = self.get_time()
    
class TaskManagement : 
    def __init__(self) : 
        self.task_list = {}
        self.completed_task_list = {}
        self.incomplete_task_list = {}

    def add_task(self) : 
        name = input('ENTER NEW TASK NAME : ')
        task_name = TaskProperty(name)
        self.task_list[task_name.id] = task_name
        self.incomplete_task_list[task_name.id] = task_name
        print('Task added successfully!')

    def show_all_tasks(self) : 
        n = len(self.task_list)
        if n == 0 : 
            print('No available task!\n')
        else : 
            # show task information
            for i in self.task_list.keys() : 
                task_id = self.task_list[i]
                print(f'ID : {task_id.id}')
                print(f'TASK : {task_id.name}')
                print(f'CREATED TIME : {task_id.created_time}')
                print(f'COMPLETED TIME : {task_id.completion_time}')
                print('\n')
        
    def show_completed_tasks(self) : 
        n = len(self.completed_task_list)
        if n == 0 : 
            print('\nNo task left to complete!\n')
        else : 
            # show completed task information
            for i in self.completed_task_list.keys() : 
                task_id = self.completed_task_list[i]
                print(f'ID : {task_id.id}')
                print(f'TASK : {task_id.name}')
                print(f'CREATED TIME : {task_id.created_time}')
                print(f'COMPLETED TIME : {task_id.completion_time}')
                print('\n')

    def show_incomplete_tasks(self) : 
        n = len(self.incomplete_task_list)
        if n == 0 : 
            print('\nNo available incomplete task!\n')
        else : 
            # show incomplete task information
            for i in self.incomplete_task_list.keys() : 
                task_id = self.incomplete_task_list[i]
                print(f'ID : {task_id.id}')
                print(f'TASK : {task_id.name}')
                print(f'CREATED TIME : {task_id.created_time}')
                print(f'COMPLETED TIME : {task_id.completion_time}')
                print('\n')
    
    def update_task(self) : 
        n = len(self.incomplete_task_list)
        if n == 0 : 
            print('\nNo task available!\n')
        else : 
            print('\nSELECT TASK TO UPDATE : ')
            index = {}
            for idx, task_id in enumerate(self.incomplete_task_list) : 
                task = self.incomplete_task_list[task_id]
                index[idx+1] = task_id
                print(f'TASK NO. : {idx+1}')
                print(f'ID : {task.id}')
                print(f'TASK NAME : {task.name}')
                print(f'CREATED TIME : {task.created_time}')
                print(f'COMPLETION STATUS : {task.task_done}')
                print(f'UPDATED TIME : {task.update_time}')
                print(f'COMPLETION TIME : {task.completion_time}')

            task_no = int(input('\nENTER TASK NO. : '))
            task_id = index[task_no]
            update_task_name = input('ENTER NEW TASK NAME : ')
            self.task_list[task_id].update_task(update_task_name)
            self.incomplete_task_list[task_id].update_task(update_task_name)
            print(f'\nTASK NUMBER {task_no} UPDATED SUCCESSFULLY!\n')
        
    def mark_completed(self) : 
        n = len(self.incomplete_task_list)
        if n == 0 : 
            print('\nNo task available!\n')
        else : 
            print('\nSELECT TASK TO COMPLETE : ')
            index = {}
            for idx, task_id in enumerate(self.incomplete_task_list) : 
                task = self.incomplete_task_list[task_id]
                index[idx+1] = task_id
                print(f'TASK NO. : {idx+1}')
                print(f'ID : {task.id}')
                print(f'TASK NAME : {task.name}')
                print(f'CREATED TIME : {task.created_time}')
                print(f'COMPLETION STATUS : {task.task_done}')
                print(f'UPDATED TIME : {task.update_time}')
                print(f'COMPLETION TIME : {task.completion_time}')
            task_no = int(input('\nENTER TASK NO. : '))
            task_id = index[task_no]
            self.task_list[task_id].complete_task()
            self.completed_task_list[task_id] = self.task_list[task_id]
            del self.incomplete_task_list[task_id] 
            print(f'\nTASK NO {task_no} IS COMPLETED\n')


tasks = TaskManagement()

while(1) : 
    print('1. Add New Task') 
    print('2. Show All Task')
    print('3. Show Incomplete Tasks')
    print('4. Show Completed Tasks')
    print('5. Update Task')
    print('6. Mark A Task Completed')

    choice = int(input('\nEnter Option : '))
    if (choice == 1) : 
        # add a new task
        tasks.add_task()
    elif (choice == 2) : 
        # show all task
        tasks.show_all_tasks()
    elif (choice == 3) : 
        # show incomplete task
        tasks.show_incomplete_tasks()
    elif (choice == 4) : 
        # show completed task
        tasks.show_completed_tasks()
    elif (choice == 5) : 
        # update a task
        tasks.update_task()
    elif (choice == 6) : 
        # mark a task as completed
        tasks.mark_completed()
    else : 
        break