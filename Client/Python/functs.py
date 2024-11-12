#-----------
#MARK: Setup
#-----------

import requests
import time
import random
from ui_tkinter import *
from settings import *
from search import mainearchforids as search
import learnmath

global first, second, third, fourth, mode_choice

#-------------------
#MARK: File Handling
#-------------------

def import_file(filename):#Loads the file filename into the lists 'first_part', 'second_part', 'third_part' and 'fourth_part' and returns them
    first_part = []
    second_part = []
    third_part = []
    fourth_part = []
    try:
        with open(filename, 'r') as file:
            log_if_debbuging(file)
            file_content = file.read()  # Read file content into a string
            file_content = strip_metadata_from_file(file_content)
            log_if_debbuging('Filecontent-Metadata: ')
            log_if_debbuging(file_content)
            file_list = file_content.splitlines()  # Split the file content into lines
            file_list = file_list[:-2]
            for line in file_list: 
                parts = line.split(';')
                log_if_debbuging(parts)
                first_part.append(parts[0])
                second_part.append(parts[1])
                third_part.append(int(parts[2]))  # Convert to integer
                fourth_part.append(int(parts[3].rstrip()))  # Convert to integer

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        if debug != 1:
            exit(1)
    except Exception as e:
        log_if_debbuging("An error occurred while reading the file:" + str(e))

    log_if_debbuging(first_part)
    log_if_debbuging(second_part)
    log_if_debbuging(third_part)
    log_if_debbuging(fourth_part)

    return first_part, second_part, third_part, fourth_part

def save_to_file(content, filename):#Saves 'content' to 'filename'
    log_if_debbuging(content)
    try:
        with open(filename, 'w') as file:
            file.write(content)
            if debug == 1:
                print(content)
        print("File saved successfully.")
    except Exception as e:
        log_if_debbuging("An error occurred while writing to the file:", e)

def save():#Saves 'first', 'second', 'third' and 'fourth' to data.txt
    output_filename = 'data.txt'
    data  = readd_metadata() + '\n'
    sem = ';'
    for i in first:
        data += first[i] + sem + second[i] + sem + third[i] + sem + fourth[i] + '\n'
    
    save_to_file(data, output_filename)
    if debug == 1:
        log_if_debbuging(f"Data saved to '{output_filename}'")

def downloadandload():#Asks the user witch id to use (with the askforid function), downloads the file with the id and takes the output of 'import_file' with data.txt and sets 'first', 'second', 'third', 'fourth' to it
    download_file(askforid())
    first, second, third, fourth = import_file('data.txt')

#------------------------
#MARK: Metadata Handeling
#------------------------
    
#NOTE  metadata not used. 

def strip_metadata_from_file(file_content):#takes out the metadata(first line), trigers 'metadata_explode' with the metadata and returns the stript filecontent
    global stript_filecontent, stript_metadata
    lines = file_content.split('\n')
    stript_metadata = lines[0]
    stript_filecontent = ''
    for i in range(len(lines) - 1):
        stript_filecontent += str(lines[i + 1]) + "\n"
    if debug == 1:
        log_if_debbuging("stript filecontent: " + stript_filecontent)
    metadata_explode(stript_metadata)
    return stript_filecontent

def metadata_explode(meta): #Splits meta into 'name', 'createtime' and 'id'
    global name, createtime, id
    main_thing = meta.split(';')
    if debug == 1:
        print("main_thing:", main_thing)

    if len(main_thing) >= 2:
        id = main_thing[1]
        createtime = main_thing[2]
        name = main_thing[3]
    else:
        log_if_debbuging("Metadata format error: Insufficient elements in main_thing")

def readd_metadata(): #returns formatet metadata
    return id + ';' + name + ';' + createtime

#---------------------
#MARK: API Interaction
#---------------------

def download_file(id_): #Doawnloads the file id from the server
    if online == 1:
        file_content = requests.get(url=api_folder + 'transalator_app.php',params={'id':id_}).text
    else:
        file_content = import_file('data.txt')
    
    if debug == 1:
        log_if_debbuging(file_content)
    
    save_to_file(str(file_content), 'data.txt')

#--------------------
#MARK: User Interface
#--------------------

def mode(): #Asks the user which mode to use
    mode_input = multiple_choice_2('please select a mode', '1 to 2', '2 to 1')
    if str(mode_input) not in ['1', '2']:
        print('Bad input: ' + mode_input)
        if debug != 1:
            exit(1)

    return mode_input

def ask(n, i): #Asks the user a question
    global mode_choice
    if mode_choice == '1':
        sol = input_question(proces_name + ' question number: ' + str(i), 'Translate: ' + first[n] + ' ')
        if sol == second[n]:
            respond_corect(second[n], sol)
            third[n] += 1
        else:
            respond_incorect(second[n], sol)
            fourth[n] += 1
    else:
        print()
        sol = input_question(proces_name + ' question number: ' + str(i), 'Translate: ' + second[n] + ' ')
        if sol == first[n]:
            respond_corect(first[n], sol)
            third[n] += 1
        else:
            respond_incorect(first[n], sol)
            fourth[n] += 1
    save()

def mainloop(i): #The main loop
    log_if_debbuging('Reached mainloop')
    item = algo_choice()
    ask(item, i)
    time.sleep(1)

def good_nogood_list(): #Does math for the 'algo_choiche'
    global fift
    fift = []
    log_if_debbuging(third)
    log_if_debbuging(' ')
    log_if_debbuging(fourth)
    for i in range(len(third)):
        fift.append(third[i] - fourth[i])

def algo_choice(): #Picks an item for a question
    log_if_debbuging('Reached algo choiche')
    good_nogood_list()
    log_if_debbuging('completed good nogood list')
    log_if_debbuging(fift)
    choice_dict = {i: fift[i] for i in range(0, len(fift))}
    log_if_debbuging("choice_dict:" + str(choice_dict))
    
    if choice_dict:
        choice_index = sorted(choice_dict.keys())[random.randint(0, len(choice_dict.keys()) - 1)]
        return choice_index
    else:
        log_if_debbuging("Error: choice_dict is empty")
        return None

def mainloop_multipel_choiche(): #The main loop (for multipel choice)
    item = algo_choice()
    ask_mtp_c(item)
    time.sleep(1)

def ask_mtp_c(item): #asks the user a multipel choice question
    log_if_debbuging(type(item))
    print(item)
    thing = [1, 2, 3]
    thing2 = []
    thing3 = []
    random.shuffle(thing)
    log_if_debbuging(thing)
    if mode_choice == '1':
        thing2.append(f"Does " + first[int(item)] + " Translate to:")
        for i in range(0, 3):
            if thing[i] == 1:
                thing2.append(second[item])
                sol = i
                sol_str = second[item]
            elif thing[i] == 2:
                try:
                    thing2.append(second[item + 1])
                except IndexError:
                    thing2.append(second[0])
            elif thing[i] == 3:
                try:
                    thing2.append(second[item - 1])
                except IndexError:
                    thing2.append[second[-1]]
    else:
        thing2.append(f"Does " + second[int(item)] + " Translate to:")
        for i in range(0, 3):
            if thing[i] == 1:
                thing2.append(first[item])
                sol = i
                sol_str = second[item]
            elif thing[i] == 2:
                try:
                    thing2.append(first[item + 1])
                except IndexError:
                    thing2.append(first[0])
            elif thing[i] == 3:
                try:
                    thing2.append(first[item - 1])
                except IndexError:
                    thing2.append(first[-1])
    try:
        user_picked_sol = multiple_choice_3(thing2[0], thing2[1], thing2[2], thing2[3])
    except IndexError:
        print(thing2)
        exit()

    user_picked_sol_str = thing2[user_picked_sol]

    print('ups:')
    print(user_picked_sol)
    print('sol')
    print(sol)
    print('sol_str')
    print(sol_str)
    print('user_picked_sol_str')
    print(user_picked_sol_str)

    if int(user_picked_sol) == sol + 1:
        respond_corect(sol_str, user_picked_sol_str)
    else:
        respond_incorect(sol_str, user_picked_sol_str)

def askforid(): #Asks about the id to use and returns it
    md = multiple_choice('Please select one', ['Enter an id', 'Search for an id'])

    if md == 0:
        return input_question('Select an id', 'Please select an id. ')
    else:
        return search()

def indexcard_show(i):
    card = [first[i], second[i]]
    indexcards_ui(card)

def respond_corect(correct_sol, user_sol):
    popup_str = 'Your Solution: ' + user_sol + ' is...  CORECT🎉🎉'
    popup_main('Correct Solution', popup_str, time=1000)

def respond_incorect(correct_sol, user_sol):
    popup_str = 'Your Solution: ' + user_sol + ' but it shoud be: ' + correct_sol
    popup_main('Incorrect Solution', popup_str, time=1000)

#-----------------------
#MARK: Variable Handling
#-----------------------

def dododo(): #sets 'mode_choice' io 'mode()'
    global mode_choice
    mode_choice = mode()

def do_things_with_variables(): #Sets 'first', 'second', 'third' and 'fourth' to import_file
    global first, second, third, fourth
    first, second, third, fourth = import_file('data.txt')

def first_send(): #returns 'first'
    return first

def second_send(): #returns 'second'
    return second

def third_send(): #returns 'third'
    return third

def fourth_send(): #returns 'fourth'
    return fourth

def proces_name_send(): #returns 'settings.proces_name'
    return settings.proces_name

def chek_if_input_is_a_command(str): #checks if input is a command (nor realy necesary)
    if str == 'exit' or str == 'quit' or str == '':
        exit
    elif str == 'help' or str == '?':
        help()
    else:
        return str

#-----------
#MARK: Tools
#-----------
    
def last_item_remover(list): #Removes the last item ow 'list'
    out = []
    for i in range(0, len(list) - 1):
        out.append(list[i])

    return out

#--------------------
#MARK: Main Execution
#--------------------

def main(mode_main): #Main executabel
    log_if_debbuging('reached main')
    log_if_debbuging('Mode:')
    log_if_debbuging('mmmmmmmmmm')
    log_if_debbuging(str(mode_main))

    log_if_debbuging(first)
    log_if_debbuging(second)
    log_if_debbuging(third)
    log_if_debbuging(fourth)
    if str(mode_main) == '0':
        log_if_debbuging('succeeded if in main')
        dododo()
        log_if_debbuging('succeeded dododo')
        i = 0
        while True:
            i += 1
            time.sleep(0.5)
            mainloop(i)

    elif str(mode_main) == '1':
        log_if_debbuging('succeeded if in main')
        dododo()
        i = 0
        while True:
            i += 1
            print('Question number:', i)
            mainloop_multipel_choiche()
    elif str(mode_main) == '2':
        log_if_debbuging('succeeded if in main')
        dododo()
        i = 0
        while True:
            i += 1
            indexcard_show(i)
    else:
        learnmath.main()

#-------------
#MARK: Testing
#-------------
    
def log_if_debbuging(str): #Obvious (Logs if debug = 1)
    print(str)
    if debug == 1:
        popup_main('Debug', str)

def api_debug(): #Debug function for the api
    debug = requests.get(url=api_folder + 'transalator_app.php',params={'id':'debug'})
    print(debug.text)

if __name__ == '__main__': #Runs the code below for debuging
    print('debuging')