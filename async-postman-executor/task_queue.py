from abc import ABC, abstractmethod
class ITaskQueue(ABC):
    @abstractmethod
    def enqueue(self, task) -> str: 
        pass
    
    @abstractmethod
    def dequeue(self, task) -> object:
        pass
    
    @abstractmethod
    def get_task_status(self, task_id: str) -> str:
        pass

class TaskQueue(ITaskQueue):
    def __init__(self, executor) -> None:
        self.executor = executor

    def enqueue(self, task) -> str:
        task_id = self.executor.submit(task)
        return task_id
    
    def dequeue(self, task) -> object:
        popped_task = self.executor.remove()
        return popped_task
    
    def get_task_status(self, task_id: str) -> str:
        return self.executor.get_task_status(task_id)
    
        