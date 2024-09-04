from tiger import Tiger
from lion import Lion
from cheetah import Cheetah
from keeper import Keeper
from vet import Vet
from caretaker import Caretaker
class Zoo:
    def __init__(self,name,budget:int,animal_capacity:int,workers_capacity:int):
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []
    
    def add_animal(self,animal,price):
        if price <= self.__budget and len(self.animals) <= self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif price > self.__budget:
            return f'Not enough budget'
        elif  sum(self.animals) > self.__animal_capacity:
            return f'Not enough capacity'
        else:
            return f'The animal can be added'
    def hire_worker(self,worker):
        if len(self.workers)  <= self.__worker_capacity:
            self.workers.append(worker)
            return f"{worker} the {worker.__class__.__name__} hired successfully"
        else:
            return 'Not enough space for workers'
    def fire_worker(self,worker_name:str):
        for worker in self.workers:
            if worker_name == str(worker.name):
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
            
        return f'There is no {worker_name} in the zoo'
    def pay_workers(self):
        total_salaries = int(sum(worker.salary for worker in self.workers))
        if self.__budget >= total_salaries:
            self.__budget = self.__budget - total_salaries
            return f'You payed your workers.They are happy. Budget left: {self.__budget}'
        else:
            return "You have no budget to pay your workers. They are unhappy"
    def tend_animals(self):
        total_needs = int(sum(animal.get_needs() for animal in self.animals))
        if self.__budget >= total_needs:
            self.__budget = self.__budget - total_needs
            return f'You tended all the animals.They are happy.Budget left {self.__budget}'
    def profit(self,amount):
        self.__budget += amount
        return self.__budget
    def animals_status(self):
        status = f"You have {len(self.animals)} animals\n"
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        
        status += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            status += f"{lion}\n"
        
        status += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            status += f"{tiger}\n"
        
        status += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            status += f"{cheetah}\n"
        
        return status.strip()
    def workers_status(self):
        status = f"You have {len(self.workers)} workers\n"
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]
        
        status += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            status += f"{keeper}\n"
        
        status += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            status += f"{caretaker}\n"
        
        status += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            status += f"{vet}\n"
        
        return status.strip()

    
    

     


