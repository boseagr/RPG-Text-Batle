from classes.game import Person, bcolors, Imp, Enemy
from classes.spell import Spell
from classes.inventory import Item
import random


fire = Spell('Fire', 10, 60, 'black')
thunder = Spell('Thunder', 10, 60, 'black')
blizzard = Spell('Blizzard', 10, 60, 'black')
meteor = Spell('Meteor', 15, 70, 'black')
quake = Spell('Quake', 20, 80, 'black')
        
cure = Spell('Cure', 15, 40, 'white')
heal = Spell('Heal', 20, 45, 'white')

potion = Item('Potion', 'potion', 'Heal 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heal 100 HP', 100)
elixir = Item('Elixir', 'elixir', 'Fully heal HP/MP of one party member', 9999)
mega_elixir = Item('Mega Elixir', 'elixir', 'Fully heal HP/MP of all party member', 9999)
grenade = Item('Grenade', 'attack', 'Deal 100 damage', 100)

player1_items = [{'item' : potion, 'quantity' : 5}, 
                {'item' : hipotion, 'quantity' : 2}, 
                {'item' : elixir, 'quantity' : 1}, 
                {'item' : mega_elixir, 'quantity' : 1},
                {'item' : grenade, 'quantity' : 1}
                ]
                
player2_items = [{'item' : potion, 'quantity' : 5}, 
                {'item' : hipotion, 'quantity' : 2}, 
                {'item' : elixir, 'quantity' : 1}, 
                {'item' : mega_elixir, 'quantity' : 1},
                {'item' : grenade, 'quantity' : 1}
                ]
                
player3_items = [{'item' : potion, 'quantity' : 5}, 
                {'item' : hipotion, 'quantity' : 2}, 
                {'item' : elixir, 'quantity' : 1}, 
                {'item' : mega_elixir, 'quantity' : 1},
                {'item' : grenade, 'quantity' : 1}
                ]                
                

player1 = Person(name='Alos', hp=480, mp=60, atk=60, df=34, magic=[fire, thunder, blizzard, meteor, quake, cure, heal], items=player1_items)
player2 = Person(name='Lila', hp=400, mp=60, atk=60, df=34, magic=[fire, thunder, blizzard, meteor, quake, cure, heal], items=player2_items)
player3 = Person(name='The Fallentino rossi', hp=500, mp=60, atk=60, df=34, magic=[fire, thunder, blizzard, meteor, quake, cure, heal], items=player3_items)

jack = Enemy('Jack', 2000, 5, 45, 25, [], [])
imp1 = Imp('Imp', 800, 100, 20, 40, [heal], [])
imp2 = Imp('Imp', 800, 100, 20, 40, [heal], [])

players = [player1, player2, player3]
enemies = [jack, imp1, imp2]

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!!' +bcolors.ENDC)

while running:   
    print('-----------------------------')
    print('NAME                      HP                                    MP         ')
    print(bcolors.BOLD + bcolors.OKGREEN + 'PARTY' + bcolors.ENDC)
    for player in players:
        player.get_stats()
    print('\n')
    print(bcolors.BOLD + bcolors.FAIL + 'ENEMY' + bcolors.ENDC)
    for enemy in enemies:
        enemy.get_stats()
        
    total_party = len(players)
    defeated_party = 0        
    all_party_defeated = False
    
    for player in players:
        defeated_enemy = 0
        
        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemy += 1
                
        if defeated_enemy == len(enemies):
            break    
        
        if player.get_hp() == 0:
            print(bcolors.BOLD + player.name + bcolors.ENDC + bcolors.FAIL + " is dying and can't continue fight!" + bcolors.ENDC)
            defeated_party += 1
            continue
            
        print('\n')    
        player.choose_action()
        choice = input('    Choose action: ')
        index = int(choice) - 1
        
        if choice == '1':
            player.choose_target(enemies)
            player_target = input('    Choose target:')
            target_index = int(player_target) - 1
            enemy = enemies[target_index]
            
            while enemy.get_hp() == 0:
                print(bcolors.BOLD + enemy.name + bcolors.ENDC + bcolors.OKGREEN + " is already die and can't fight anymore, choose another target" +bcolors.ENDC)
                player_target = input('    Choose other target:')
                target_index = int(player_target) - 1
                enemy = enemies[target_index]
                
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(player.name, 'attacked', enemy.name ,'for', dmg, 'points of damage. Enemy HP:', enemy.get_hp())
            
        elif choice == '2':
            player.choose_spell()
            magic_choice = input('    Choose your magic :')
            magic_index = int(magic_choice) - 1      
            spell = player.magic[magic_index]
            magic_dmg = spell.generate_damage()
            cost = spell.cost

            current_mp = player.get_mp()
            if cost > current_mp:
                print(bcolors.FAIL + '\nNot enough MP\n' + bcolors.ENDC)
                continue
                
            player.reduce_mp(cost)
            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name,  'heal for ', magic_dmg, 'points of HP.' + bcolors.ENDC + player.name +' HP:', player.get_hp())
            elif spell.type == 'black':
                player.choose_target(enemies)
                player_target = input('    Choose target:')
                target_index = int(player_target) - 1
                
                enemy = enemies[target_index]      
                while enemy.get_hp() == 0:
                    print(bcolors.BOLD + enemy.name + bcolors.ENDC + bcolors.OKGREEN + " is already die and can't fight anymore, choose another target" +bcolors.ENDC)
                    player_target = input('    Choose other target:')
                    target_index = int(player_target) - 1
                    enemy = enemies[target_index]                
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name,  'deals ', magic_dmg, 'points of damage to', enemy.name, '.' + bcolors.ENDC +' Enemy HP:', enemy.get_hp())
        
        elif choice == '3':
            if player.items == []:
                print(bcolors.FAIL + player.name + ' have no item' + bcolors.ENDC)    
                continue
                
            player.choose_item()
            item_choice = input('Choose your Item :')
            item_index = int(item_choice) - 1
            item = player.items[item_index]['item']
            player.items[item_index]['quantity'] -=  1        
            
            if player.items[item_index]['quantity'] == 0:
                del player.items[item_index]
            
            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name,  'heal for ', item.prop, 'points of HP.' + bcolors.ENDC +' Your HP:', player.get_hp())
            
            elif item.type == 'elixir':
                if item.name == 'Mega Elixir':
                    for party in players:
                        party.hp = party.maxhp
                        party.mp = party.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + '\n' + item.name,  'Fully heal HP and MP.' + bcolors.ENDC )
            
            elif item.type == 'attack':
                player.choose_target(enemies)
                player_target = input('    Choose target:')
                target_index = int(player_target) - 1
                
                enemy = enemies[target_index]       
                while enemy.get_hp() == 0:
                    print(bcolors.BOLD + enemy.name + bcolors.ENDC + bcolors.OKGREEN + " is already die and can't fight anymore, choose another target" +bcolors.ENDC)
                    player_target = input('    Choose other target:')
                    target_index = int(player_target) - 1
                    enemy = enemies[target_index]                
                enemy.take_damage(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name,  'deals ', item.prop, 'points of damage to', enemy.name, '.' + bcolors.ENDC +' Enemy HP:', enemy.get_hp())
          
    total_enemy = len(enemies)
    defeated_enemy = 0
    for enemy in enemies:
       if enemy.get_hp() == 0:
           defeated_enemy += 1
           
    if total_enemy == defeated_enemy:
        print(bcolors.OKGREEN + 'You Win' + bcolors.ENDC)
        running = False

    elif total_party == defeated_party:
        print(bcolors.FAIL + 'Your Enemy defeated you' + bcolors.ENDC)
        running = False
        
    for enemy in enemies:
        enemy_choice = '1'
        enemy_target = random.randrange(0, len(players))
        target = players[enemy_target]
           
        if enemy.get_hp() <= 0:
            continue
        
        elif target.get_hp() == 0:
            player_checked = 0
            while target.get_hp () == 0:
                if enemy_target < len(players) -1:
                    enemy_target += 1
                else:
                    enemy_target = 0
                target = players[enemy_target]
                player_checked += 1
                if player_checked == total_party:
                   all_party_defeated = True
                   break
                   
        if all_party_defeated:
            continue
            
        elif enemy_choice == '1':
            enemy_dmg = enemy.generate_damage()
            target.take_damage(enemy_dmg)
            print(enemy.name + bcolors.FAIL + ' attacked ' + bcolors.ENDC + bcolors.BOLD + target.name + bcolors.ENDC + bcolors.FAIL + ' for', enemy_dmg, 'points of damage. ' + target.name + ' HP:', str(target.get_hp()) + bcolors.ENDC)    

