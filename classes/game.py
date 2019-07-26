import random
import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items= items
        self.actions = ['Attack', 'Magic', 'Item']
        
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
          
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
            
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
        
    def get_hp(self):
       return self.hp
       
    def get_maxhp(self):
       return self.maxhp    
       
    def get_mp(self):
       return self.mp
       
    def get_maxmp(self):
       return self.maxmp
       
    def reduce_mp(self, cost):
        self.mp -= cost
        
    def choose_action(self):
        print(bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + '    Action:' + bcolors.ENDC)
        for i, item in enumerate(self.actions):
            print('    ',str(i+1), ':', item)
            
    def choose_spell(self):
        print(bcolors.OKBLUE + bcolors.BOLD + '    Magic:' + bcolors.ENDC)
        for i, spell in enumerate(self.magic):
            print('       ' + str(i+1), ':', spell.name, '(cost :', str(spell.cost), 'mp)')
            
    def choose_item(self):
        print(bcolors.OKBLUE + bcolors.BOLD + '    Item:' + bcolors.ENDC)
        for i, item in enumerate(self.items):
            print('       ' + str(i+1), ':', item['item'].name, '-', str(item['item'].description) +' (x' + str(item['quantity']) +')')
    
    def choose_target(self, enemies):
        print(bcolors.FAIL + bcolors.BOLD + "    Target:" + bcolors.ENDC)
        for i, enemy in enumerate(enemies):
            print('       ' + str(i+1), ':', enemy.name)

    def get_stats(self):
        hp_blocks = '█'*math.ceil((self.hp/self.maxhp)*25)
        mp_blocks = '█'*math.ceil((self.mp/self.maxmp)*10)
        print('                          _________________________             __________ ')
        print(bcolors.BOLD + self.name[:15] + ' '*(15-len(self.name)) + 
              ' '*(9-len(str(self.hp) + '/' + str(self.maxhp))) + str(self.hp) + '/' + str(self.maxhp) + ' |' + bcolors.OKGREEN + str(hp_blocks) + bcolors.ENDC + ' '*(25 - len(hp_blocks)) + '|' +
              ' '*(10-len(str(self.mp) + '/' + str(self.maxmp))) + str(self.mp) + '/' + str(self.maxmp) + ' |' + bcolors.OKBLUE + str(mp_blocks) + bcolors.ENDC + ' '*(10 - len(mp_blocks)) + '|'  
              )
        
        
class Enemy(Person):
    def get_stats(self):
        hp_blocks = '█'*math.ceil((self.hp/self.maxhp)*30)
        mp_blocks = '█'*math.ceil((self.mp/self.maxmp)*15)
        print('                          ______________________________             _______________ ')
        print(bcolors.BOLD + bcolors.FAIL + self.name[:15] + ' '*(15-len(self.name)) + bcolors.ENDC + 
              ' '*(9-len(str(self.hp) + '/' + str(self.maxhp))) + str(self.hp) + '/' + str(self.maxhp) + ' |' + bcolors.FAIL + str(hp_blocks) + bcolors.ENDC + ' '*(30 - len(hp_blocks)) + '|' +
              ' '*(10-len(str(self.mp) + '/' + str(self.maxmp))) + str(self.mp) + '/' + str(self.maxmp) + ' |' + bcolors.OKBLUE + str(mp_blocks) + bcolors.ENDC + ' '*(15 - len(mp_blocks)) + '|'  
              )
       
       
class Imp(Enemy):
    
    def __init__(self, name, hp, mp, atk, df, magic, items):
        super().__init__(name, hp, mp, atk, df, magic, items)
        
        