from typing import Optional, List

import Category
import Effort
import Step


class Recipe:
    def __init__(self):
        self.id: int = 0
        self.name: Optional[str] = None
        self.category: Optional[Category] = None
        self.effort: Optional[Effort] = None
        self.Ingredients:Optional[str]=None
        self.steps: List[Step] = []
