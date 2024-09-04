
class Toppings:
    def __init__(self, topping_type: str, weight: float):
        self.__topping_type = topping_type
        self.__weight = weight

   
    def get_topping_type(self):
        return self.__topping_type

   
    def get_weight(self):
        return self.__weight

   
    def set_topping_type(self, topping_type: str):
        self.__topping_type = topping_type

    
    def set_weight(self, weight: float):
        self.__weight = weight



class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

   
    def get_flour_type(self):
        return self.__flour_type

    
    def get_baking_technique(self):
        return self.__baking_technique

   
    def get_weight(self):
        return self.__weight

   
    def set_flour_type(self, flour_type: str):
        self.__flour_type = flour_type

   
    def set_baking_technique(self, baking_technique: str):
        self.__baking_technique = baking_technique

   
    def set_weight(self, weight: float):
        self.__weight = weight



class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

   
    def get_name(self):
        return self.__name

  
    def get_dough(self):
        return self.__dough

    
    def get_toppings(self):
        return self.__toppings

   
    def get_toppings_capacity(self):
        return self.__toppings_capacity

   
    def set_name(self, name: str):
        self.__name = name

   
    def set_dough(self, dough: Dough):
        self.__dough = dough

 
    def set_toppings_capacity(self, toppings_capacity: int):
        self.__toppings_capacity = toppings_capacity

 
    def add_topping(self, topping: Toppings):
        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Không đủ chỗ cho topping mới")
        
        if topping.get_topping_type() in self.__toppings:
            self.__toppings[topping.get_topping_type()] += topping.get_weight()
        else:
            self.__toppings[topping.get_topping_type()] = topping.get_weight()


    def calculate_total_weight(self):
        total_weight = self.__dough.get_weight() + sum(self.__toppings.values())
        return total_weight



pepperoni = Toppings("Pepperoni", 50)  
mushrooms = Toppings("Mushrooms", 30)  
cheese = Toppings("Cheese", 80)  


thin_crust = Dough("Wheat", "Thin Crust", 200)  


pizza = Pizza("Pepperoni Pizza", thin_crust, 3)


pizza.add_topping(pepperoni)
pizza.add_topping(mushrooms)
pizza.add_topping(cheese)


total_weight = pizza.calculate_total_weight()


print(f"Tên pizza: {pizza.get_name()}")
print(f"Bột: {pizza.get_dough().get_flour_type()} - {pizza.get_dough().get_baking_technique()} - {pizza.get_dough().get_weight()} grams")
print("Các topping:")
for topping_type, weight in pizza.get_toppings().items():
    print(f"- {topping_type}: {weight} grams")
print(f"Tổng trọng lượng của pizza: {total_weight} grams")
