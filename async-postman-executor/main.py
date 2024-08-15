from executor import TaskExecutor
from task_queue import TaskQueue
import asyncio

async def main():
    lambda1 = lambda : print("Addition Operation")
    lambda2 = lambda : print("Multiplication Operation")
    task_executor = TaskExecutor()
    task_queue = TaskQueue(task_executor)
    task_id1 = task_queue.enqueue(lambda1)
    print(f"Task id for first task is {task_id1}")
    task_id2 = task_queue.enqueue(lambda2)
    print(f"Task id for first task is {task_id2}")
    print(f"Task status for first task is {task_queue.get_task_status(task_id=task_id1)}")
    print(f"Task status for second task is {task_queue.get_task_status(task_id=task_id2)}")
    await asyncio.sleep(4)
    print(f"Task status for first task is {task_queue.get_task_status(task_id=task_id1)}")
    print(f"Task status for second task is {task_queue.get_task_status(task_id=task_id2)}")
    
asyncio.run(main())
    
    