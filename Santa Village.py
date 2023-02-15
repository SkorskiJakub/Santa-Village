import random

class Village:
    residents_number = 0
    def __init__(self, name, residents_number):
        self.name = name
    def add_residents(self):
        Village.residents_number += 1
    
    def __str__(self):
        return f" In the{self.name} is living {self.residents_number} residents now."
    def create():
        
class SantaHouse(Village):
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Factory(Village):
    def __init__(self, name, level):
        self.name = name
        self.level = level

class ElfHouse(Village):
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Stable(Village):
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Residents(Village):
    def __init__ (self, name, position):
        self.name = name
        self.position = position
        super().add_residents()

    def speak(self):
        return f" My name is {self.name}. I work as {self.position}."


class Santa(Residents):
    def __init__(self, name, position):
        super().(name, position)

    def __str__(self):
        return f" My name is {self.name}. This is my village."


class Elfs(Residents):
    position_dict = {"worker": worker, "engineer": engineer, "administration": administration, "Santa right hand":Santa right hand}
    def __init__(self, name, position):
        super().(name, position)
        
    def create_elfs():
        name = input("Please write Elf name: ")
        position_value = random.choice(list(position_dict()))
        position = Elfs(position_value)
        
    def speak(self):
        super().speak()


class SantaWife(Residents):
    def __init__(self, name, position):
        super().(name, position)
    def __str__(self):
        return f" My name is {self.name}. I an Santa's wife."


class Reindeeer(Residents):
    def __init__(self, name, position):
        super().(name, position)
    def speak(self):
        super().speak()


class ProductionWorker(Elfs):
    worker_num = 0
    def add_worker(self):
        for position in Elfs:
            if position == "worker":
                ProductionWorker.worker_num += 1
        return f" At this moment we have {worker_num} Production workers in Santa Village."
            

class Engineer(Elfs):
    engineer_num = 0
    def add_engineer(self):
        for position in Elfs:
            if position == "engineer":
                Engineer.engineer_num += 1
        return f" At this moment we have {engineer_num} Engineers in Santa Village."

class Administration(ELfs):
    admin_num = 0
    def add_admin(self):
        for position in Elfs:
            if position == "administration":
                Administration.admin_num += 1
        return f" At this moment we have {admin_num} administration workers in Santa Village."

class SantaRightHand(Elfs):
    righthand_num = 0
    def add_right_hand(self):
        for position in Elfs:
            if position == "Santa right hand":
                 SantaRightHand.righthand_num += 1
        return f" At this moment we have {righthand_num} Santa's Right Hand in Village."



