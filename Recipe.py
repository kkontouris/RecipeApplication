from typing import Optional, List

import Category
import Effort
import Step


class Recipe:
    def __init__(self):
        #αρχικα 0
        self.id: int = 0
        #όνομα της συνταγής είτε none
        self.name: Optional[str] = None
        #αντικείμενο της Category είτε None
        self.category: Optional[Category] = None
        #αντικείμενο της effort είτε None
        self.effort: Optional[Effort] = None
        #Υλικά είτε None
        self.Ingredients:Optional[str]=None
        #Λίστα απο βήματα είτε none
        self.steps: List[Step] = []
