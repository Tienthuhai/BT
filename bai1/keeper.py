class Keeper:
    def __init__(self,name:str,age:int,salary:str):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self) -> str:
        return f'Name:{self.name},Age:{self.age},Salary:{self.salary}'
    