from typing import Optional


class Step:
    def __init__(self):
        self.id: int = 0
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        self.required_time_seconds: float = 0.0
        self.ingredients: str = ""
