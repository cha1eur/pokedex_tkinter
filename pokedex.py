#Program made by Javier Ewe
'''
Sample size of 10 Pokemon used
Pictures obtained from Bulbapedia
This is a Pokemon Encyclopedia made with Tkinter for Python, where one can
search for pokemon via the Pokedex number or through a drop down menu.
Note this program was made from a Windows Computer and WILL look different
when loaded on a Mac or Linux.
Please excuse any formatting errors as a result of non-Windows computers being
used to load this program.
Note for Tkinter to accept my .png files, please use Python 3.6 or newer on
Windows or Python 3.7(b) or later on Mac.
Thanks!
'''

from tkinter import *
from tkinter import messagebox


pokedex = {1: { "name": "Bulbasaur",
                "type": ["Grass", "Poison"],
                "h&w": [0.7, 6.9],
                "ability": "Overgrow",
                "hability": "Chlorophyll",
                "m1": "Petal Dance",
                "m2" : "Sludge Bomb",
                "m3" : "Synthesis",
                "m4" : "Toxic",
                },
           2 : { "name": "Ivysaur",
                "type": ["Grass", "Poison"],
                "h&w": [1.0, 13.0],
                "ability": "Overgrow",
                "hability": "Chlorophyll",
                "m1": "Synthesis",
                "m2" : "Sludge Bomb",
                "m3" : "Leech Seed",
                "m4" : "Petal Dance",
                },
           3 : { "name": "Venusaur",
                "type": ["Grass", "Poison"],
                "h&w": [2.0, 100.0],
                "ability": "Overgrow",
                "hability": "Chlorophyll",
                "m1": "Synthesis",
                "m2" : "Sludge Bomb",
                "m3" : "Petal Dance",
                "m4" : "Sleep Powder",
                },
           4 : { "name": "Charmander",
                "type": ["Fire"],
                "h&w": [0.6, 8.5],
                "ability": "Blaze",
                "hability": "Solar Power",
                "m1": "Outrage",
                "m2" : "Rock Slide",
                "m3" : "Crunch",
                "m4" : "Flare Blitz",
                },
           5 : { "name": "Charmeleon",
                "type": ["Fire"],
                "h&w": [1.1, 19.0],
                "ability": "Blaze",
                "hability": "Solar Power",
                "m1": "Rock Slide",
                "m2" : "Flare Blitz",
                "m3" : "Outrage",
                "m4" : "Aerial Ace",
                },
           6 : { "name": "Charizard",
                "type": ["Fire","Flying"],
                "h&w": [1.7, 90.5],
                "ability": "Blaze",
                "hability": "Solar Power",
                "m1": "Flare Blitz",
                "m2" : "Dragon Claw",
                "m3" : "Earthquake",
                "m4" : "Roost",
                },
           7 : { "name": "Squirtle",
                "type": ["Water"],
                "h&w": [0.5, 9.0],
                "ability": "Torrent",
                "hability": "Rain Dish",
                "m1": "Hydro Pump",
                "m2" : "Ice Beam",
                "m3" : "Aura Sphere",
                "m4" : "Rapid Spin",
                },
           8 : { "name": "Watortle",
                "type": ["Water"],
                "h&w": [1.0, 22.5],
                "ability": "Torrent",
                "hability": "Rain Dish",
                "m1": "Scald",
                "m2" : "Rapid Spin",
                "m3" : "Ice Beam",
                "m4" : "Toxic",
                },
           9 : { "name": "Blastoise",
                "type": ["Water"],
                "h&w": [1.6, 85.5],
                "ability": "Torrent",
                "hability": "Rain Dish",
                "m1": "Rapid Spin",
                "m2" : "Scald",
                "m3" : "Ice Beam",
                "m4" : "Aura Sphere",
                },
           10 : { "name": "Caterpie",
                "type": ["Bug"],
                "h&w": [0.3, 2.9],
                "ability": "Shield Dust",
                "hability": "Run Away",
                "m1": "Bug Bite",
                "m2" : "Electroweb",
                "m3" : "Snore",
                "m4" : "Tackle",
                },
        }

#######################################
pkmn_type_color = {'Grass': '#78C850',
                   'Poison': '#A040A0',
                   'Flying': '#A890F0',
                   'Fire': '#F08030',
                   'Dragon': '#7038F8',
                   
                    }
#######################################
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# to be used for future versions (color coding pokemon types) #


dropdownmenu_items = []
for i in range(1, len(pokedex)+1):
    dropdownmenu_items.append(str(i).zfill(3) + " : " + pokedex[i]["name"])

#####################
# NON-GUI FUNCTIONS #
#####################



def kg_to_lb(x):
    return x / 0.45359237 

def lb_to_kg(x):
    return  x * 0.45359237 

def m_to_ft(x):
    fi = x * 3.28084
    ft = int(fi)
    i = fi - ft
    i = i * 12
    return str(ft) + "' " + str(int(round(i, 0))) + '"'
    
    
def ft_to_m(ft,i):
    i /= 0.39370
    ft /= 0.032808
    return round((i + ft) / 100 , 2)


#################
# GUI FUNCTIONS #
#################
def update_info(dex_search):
    lb_pokemon_name.configure(text = pokedex[int(dex_search)]["name"])

    img_dir = 'img/' + str(dex_search).zfill(3) + '.png'
    new_img = PhotoImage(file = img_dir)
    lb_img.image = PhotoImage(file = img_dir)
    lb_img.configure(image = new_img)
    win.img = new_img

    txt_type = ''
    pokemon_type = pokedex[int(dex_search)]['type']
    for poke_type in pokedex[int(dex_search)]['type']:
        txt_type += poke_type + ", "
    #To remove the ending ", " irregardless number of type
    lb_type.configure(text = txt_type.rstrip(", "))

    lb_ability.configure(text = pokedex[int(dex_search)]["ability"])
    
    lb_hability.configure(text = pokedex[int(dex_search)]["hability"])

    lb_height.configure(text = str(pokedex[int(dex_search)]["h&w"][0]) + " m")

    lb_m1.configure(text = pokedex[int(dex_search)]["m1"])

    lb_m2.configure(text = pokedex[int(dex_search)]["m2"])

    lb_m3.configure(text = pokedex[int(dex_search)]["m3"])

    lb_m4.configure(text = pokedex[int(dex_search)]["m4"])

    if bn_hconvert.cget("text") == "m":
        curr_pkmn_height = float(str(pokedex[int(dex_search)]["h&w"][0]))
        converted_height = m_to_ft(curr_pkmn_height)
        lb_height.configure(text = converted_height)
        bn_hconvert.configure(text = "m")
    elif bn_wconvert.cget("text") == "ft":
        weight_str = str(pokedex[int(dex_search)]["h&w"][0])
        lb_height.configure(text = height_str + " m")

    if bn_wconvert.cget("text") == "kg":
        weight_str = str(round(kg_to_lb(pokedex[int(dex_search)]["h&w"][1]), 1))
        lb_weight.configure(text = weight_str + " lb")
    elif bn_wconvert.cget("text") == "lb":
        weight_str = str(pokedex[int(dex_search)]["h&w"][1])
        lb_weight.configure(text = weight_str + " kg")

    


def txt_retrieve_pokemon():
    dex_search = txt_dex_num.get()
    txt_dex_num.delete(0,END)
    if dex_search.isdigit() and int(dex_search) <= 10:
        update_info(int(dex_search))
  
    else:
        messagebox.showwarning("Search Error", "Please enter a number from 1 to 10")


def ddm_retrieve_pokemon(*args):
    '''
    This function will be triggered whenever the drop down list is changed.
    It will update the Pokemon data and image based on the new pokemon selected.
    '''
    dex_search = menu_str.get()[:3]
    update_info(int(dex_search))

def wconvert():
    if bn_wconvert.cget("text") == "kg":
        curr_pkmn_weight = float(lb_weight.cget("text").rstrip(" lb"))
        converted_weight = round(lb_to_kg(curr_pkmn_weight),1)
        lb_weight.configure(text = str(converted_weight) + " kg")
        bn_wconvert.configure(text = "lb")
    elif bn_wconvert.cget("text") == "lb":
        curr_pkmn_weight = float(lb_weight.cget("text").rstrip(" kg"))
        converted_weight = round(kg_to_lb(curr_pkmn_weight),1)
        lb_weight.configure(text = str(converted_weight) + " lb")
        bn_wconvert.configure(text = "kg")

def hconvert():
    if bn_hconvert.cget("text") == "m":
        ft = int(lb_height.cget("text").split("' ")[0])
        inches = int(lb_height.cget("text").split("'")[-1].rstrip('"'))
        converted_height = str(ft_to_m(ft, inches))
        lb_height.configure(text = converted_height + " m")
        bn_hconvert.configure(text = "ft")
    elif bn_hconvert.cget("text") == "ft":
        curr_pkmn_height = float(lb_height.cget("text").rstrip(" m"))
        converted_height = m_to_ft(curr_pkmn_height)
        lb_height.configure(text = converted_height)
        bn_hconvert.configure(text = "m")

#############
# GUI ITEMS #
#############

win = Tk()
win.title("Pokédex")
win.geometry("800x600")

lb_dexnumber = Label(win, text = "#", font=("Arial",28))
lb_dexnumber.place(x = 40, y = 40)

txt_dex_num = Entry(win, bd = 3, width = 5)
txt_dex_num.place(x= 75, y = 53)

bn_search = Button(win, text = "Search", command = txt_retrieve_pokemon)
bn_search.place(x=120, y = 53)

bn_hconvert = Button(win, text = "ft", command = hconvert)
bn_hconvert.place(x=712, y = 335)

bn_wconvert = Button(win, text = "lb", command = wconvert)
bn_wconvert.place(x=712, y = 362)

lb_pokemon_name = Label(win, text = pokedex[1]["name"], font = ("Verdana", 32))
lb_pokemon_name.place(x = 100 , y = 100)

lb_pretype = Label(win, text = "TYPE: ", font = ("Verdana", 13, "bold"))
lb_pretype.place(x = 60, y = 200)

lb_type = Label(win, text = "Grass, Poison", font = ("Verdana", 13))
lb_type.place(x = 120, y = 200)

lb_ability = Label(win, text = pokedex[1]["ability"])
lb_ability.place(x = 185, y = 252)

lb_hability = Label(win, text = pokedex[1]["hability"])
lb_hability.place(x = 185, y = 272)

lb_preability = Label(win, text = "Ability: ", font = ("Verdana", 11, "bold"))
lb_preability.place(x = 121, y = 250)

lb_prehability = Label(win, text = "Hidden Ability: ", font = ("Verdana", 11, "bold"))
lb_prehability.place(x = 60, y = 270)

lb_height = Label(win, text = "0.7 m", font = ("Verdana", 13))
lb_height.place(x = 630, y = 335)

lb_weight = Label(win, text = "6.9 kg", font = ("Verdana", 13))
lb_weight.place(x = 630, y = 360)

lb_preheight = Label(win, text = "Height:", font = ("Verdana", 11, "bold"))
lb_preheight.place(x = 566, y = 337)

lb_preweight = Label(win, text = "Weight:", font = ("Verdana", 11, "bold"))
lb_preweight.place(x = 562, y = 362)

lb_moveset = Label(win, text = "Competitive moveset", font = ("Verdana", 13))
lb_moveset.place(x = 140, y = 350)

lb_m1 = Label(win, text = "Celebrate", font = ("Verdana", 15))
lb_m1.place(x = 75, y = 410)

lb_m2 = Label(win, text = "Sludge Bomb", font = ("Verdana", 15))
lb_m2.place(x = 280, y = 410)

lb_m3 = Label(win, text = "Giga Drain", font = ("Verdana", 15))
lb_m3.place(x = 75, y = 460)

lb_m4 = Label(win, text = "Sleep Powder", font = ("Verdana", 15))
lb_m4.place(x = 280, y = 460)




####### IMAGE STUFF #######

#pkmn_img = PhotoImage(file='img/001.png')
pkmn_img = PhotoImage(file='img/001.png')

lb_img = Label(win, image = pkmn_img,
               width = 500)
lb_img.place(x = 380, y = 50)



####### DROP DOWN MENU #######

#Declare variable for drop down list
menu_str = StringVar(win)
#default value
menu_str.set(dropdownmenu_items[0])

#Drop down list syntax
#Option_Menu(Tk namw, var_for_selected-value, seq_of_values)
#If seq_of_value is a variable name, add an asterisk

menu = OptionMenu(win, menu_str, *dropdownmenu_items)
menu.place(x = 300, y =50)
menu_str.trace('w', ddm_retrieve_pokemon)

