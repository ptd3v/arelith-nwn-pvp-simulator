#Import UI elements
#Amount of classes = 12?
#Race = (Human, Elf, Half-Elf, Gnome, Firbolg, Half-Giant, Frost Half-Giant, Fire Half-Giant, Stone Half-Giant, Drow, Minotaur, Halfling)
#Barbarian, RDDSorc, Fighter, Weapon Master, Wizards, w

#Select Class, 
select class = (input.read)

class = fighter
fighter_level = 30
fighter_hp = CON * 1d10
AC = 48
AB = 52 - 5 * 4
APR = 4
crit_range = 10 - 20
damage = 1d8 #Fighter Only
spell_damage = 0 #Wizard Only
will_save = 30
reflex_save = 30
fortitude _save = 40
str = 40
dex = 12
con = 32

#Create Player 1 (Fighter)
player1 = Character(char_class="Fighter", hp_die=10, level=30, ac=25, ab=15,
                    apr=4, damage_die=12, spell_damage_die=0, will_save=8,
                    reflex_save=8, fortitude_save=12, strength=20, dexterity=14,
                    constitution=18)

#Create Player 2
class = wizard
wizard_hp = CON * 
wizard_level = 30
AC = 0
AB = 0
APR = 3
damage = 0 #Fighter Only
spell_damage = 0 #Wizard Only
will_save = 0
reflex_save = 0
fortitude _save = 0
str = 0
dex = 0
con = 0

#Create Player 2 (Wizard)
player2 = Character(char_class="Wizard", hp_die=4, level=30, ac=15, ab=8,
                    apr=3, damage_die=4, spell_damage_die=6, will_save=12,
                    reflex_save=8, fortitude_save=5, strength=10, dexterity=12,
                    constitution=14)

#Dice Roll
dice_roll = 1d20
