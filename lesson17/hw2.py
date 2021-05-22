class magician:
    def __init__(self,attack,super_attack,sewn):
        self.attack = attack
        self.super_attack = super_attack
        self.sewn = sewn

    def attacks(self):
        return self.attack

    def super_attac(self):
        return self.super_attack

    def sewns(self):
        return self.sewn

class archer:
    def __init__(self,attack,super_attack,sewn):
        self.attack = attack
        self.super_attack = super_attack
        self.sewn = sewn

    def attacks(self):
        return self.attack

    def super_attac(self):
        return self.super_attack

    def sewns(self):
        return self.sewn
    

firs=magician('fire','big fireball','metal shot')
first=archer('arrow','big arrow','metal shot')
print(firs.attacks())
print(first.sewns())
print(first.attacks())
print(firs.sewns())
print(first.super_attac())
print(firs.super_attac())
print('explosion')