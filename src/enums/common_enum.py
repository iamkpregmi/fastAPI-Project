from enum import Enum

class BlogCategory(str, Enum):
    business = 'Business'
    fashin = 'Fashion'
    finance = 'Finance'
    food = 'Food'
    music = 'Music'
    politics = 'Politics'
    other = 'Other'


