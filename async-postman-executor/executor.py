from abc import ABC, abstractmethod
from enums import TaskStatus
import uuid
import time
import asyncio

class ITaskExecutor(ABC):
    @abstractmethod
    def submit(self, task) -> str: 
        pass
    
    @abstractmethod
    def remove(self, task) -> str: 
        pass
    
    @abstractmethod
    def get_task_status(self, task_id:str) -> str: 
        pass
    
class TaskExecutor(ITaskExecutor):
    def __init__(self) -> None:
        self.queue = []
        super().__init__()
    
    def submit(self, task) -> str:
        task_id = str(uuid.uuid4())
        self.queue.append(
            {
                "task_id": task_id,
                "task": task,
                "result": None,
                "status": TaskStatus.NOT_STARTED.value
            }
        )
        asyncio.create_task(self._execute(task_id, task))
        return task_id
        
    async def _execute(self, task_id, task) -> (str, object, str):
        try:
            result = task()
        except Exception as e:
            print(f"Task Failed with error: {e}")
            self._update_task(task_id, None, TaskStatus.FAILED.value)
        self._update_task(task_id, result, TaskStatus.SUCCESS.value)
            
    def get_task_status(self, task_id: str) -> str:
        for task in self.queue:
            if task.get("task_id") == task_id:
                return task.get("status")
        
    def _update_task(self, task_id, result, status):
        for task in self.queue:
            if task.get("task_id") == task_id:
                task["result"] = result
                task["status"] = status
    
    def remove(self, task) -> object:
        return self.queue.pop()