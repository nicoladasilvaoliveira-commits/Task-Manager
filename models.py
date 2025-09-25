from abc import ABC, abstractmethod
from typing import List, Optional
import db

class TaskBase(ABC):
    def __init__(self, title: str, description: str = "", priority: int = 1):
        self._title = title
        self._description = description
        self._priority = priority
        self._status = "todo"
    @property
    def title(self) -> str:
        return self._title
    @property
    def description(self) -> str:
        return self._description
    @property
    def priority(self) -> int:
        return self._priority
    @property
    def status(self) -> str:
        return self._status
    @status.setter
    def status(self, new_status: str):
        if new_status not in ("todo", "in_progress", "done"):
            raise ValueError("Status inválido")
        self._status = new_status
    @abstractmethod
    def task_type(self) -> str:
        pass
    def to_dict(self) -> dict:
        return {
            "title": self._title,
            "description": self._description,
            "priority": self._priority,
            "status": self._status,
            "type": self.task_type()
        }

class BugTask(TaskBase):
    def __init__(self, title: str, description: str = "", priority: int = 2, severity: str = "medium"):
        super().__init__(title, description, priority)
        self.severity = severity
    def task_type(self) -> str:
        return "bug"

class FeatureTask(TaskBase):
    def __init__(self, title: str, description: str = "", priority: int = 1, story_points: int = 3):
        super().__init__(title, description, priority)
        self.story_points = story_points
    def task_type(self) -> str:
        return "feature"

class TaskManager:
    def __init__(self):
        db.init_db()
    def create_task(self, task: TaskBase) -> int:
        data = task.to_dict()
        task_id = db.insert_task(
            title=data["title"],
            description=data["description"],
            status=data["status"],
            priority=data["priority"],
            type_name=data["type"]
        )
        return task_id
    def list_tasks(self) -> List[dict]:
        rows = db.fetch_all_tasks()
        result = []
        for r in rows:
            result.append({
                "id": r["id"],
                "title": r["title"],
                "description": r["description"],
                "status": r["status"],
                "priority": r["priority"],
                "type": r["type"]
            })
        return result
    def set_status(self, task_id: int, status: str) -> None:
        db.update_task_status(task_id, status)
    def delete(self, task_id: int) -> None:
        db.delete_task(task_id)
    def get(self, task_id: int) -> Optional[dict]:
        r = db.fetch_task_by_id(task_id)
        if r:
            return dict(r)
        return None
