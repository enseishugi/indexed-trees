#!/usr/bin/python3
# -*- coding: utf-8 -*-
# indexed-trees.py
# Python 3.7.5 

"""Questo script genera un albero per org-mode che corrisponde alla lista di
esercizi di un sectioning specificato dall'utente. Quanti esercizi siano, il
titolo della sezione, il numero della sezione, eccetera, sono indicate
dall'utente.

"""

# ====================
# Functons asking data
# ====================

def list_strip(l, s):
    """Returns a string whose values are the '*.strip(s)' of the values in 'l'.

    l: list containing only strings.

    """
    
    newlist = []
    
    for i in l:
        newlist.append(i.strip(s))

    return newlist


def list_int(l):
    """Returns a string whose values are the 'int(*)' of the values in 'l'.

    l: list containing only strings compatible to 'int' function.

    """

    newlist = []

    for i in l:
        newlist.append(int(i))

    return newlist

    
def ask_section():
    """Returns a list 'section' whose values are section_type, section_number,
    section_name.

    """

    print("Insert: section_type @ section_number @ section_name (separated by @)")
    section = list_strip(input("> ").split("@"), ' ')

    return section


def ask_contents():
    """Returns a dictionary whose keys are content_types and values are
    content_data.

    """

    tree_contents = {}
    
    print("Insert: block name (if not, leave blank)")
    block = input("> ")
    if block == '':
        tree_contents['block'] = None
    else:
        tree_contents['block'] = block.strip()
    
    print("Insert: files path @ file extension (if not, leave blank)")
    files = input("> ")
    if files == '':
        tree_contents['files'] = None
    else:
        tree_contents['files'] = list_strip(files.split("@"), ' ')

    return tree_contents

    
def ask_printing_data():
    """ Returns two positive integers.
    
    """

    print("Insert: number of iterations @ depth (separated by @)")
    data = list_strip(input("> ").split("@"), ' ')
    number_iterations, depth = list_int(data)

    return number_iterations, depth


# ==============================
# Functions making string models
# ==============================

def make_heading(section):
    """Returns a string 'heading', built using 'section'.

    section: list containing section_type, section_number, section_name

    """

    heading = "%s %s - %s\n" % tuple(section)
    return heading


def make_content(content_type, content_data, section):
    """Returns a string 'content' and an integer 'dim'.

    The string 'content' is a model string to be added to 'tree_model', and it's
    built using 'content_type', 'content_data' and 'section'.

    The integer 'dim' is the number of instances of iterators '%i' in
    'content'.

    content_type: string
    content_data: string
    section: list containing section_type, section_number, section_name

    """

    content = ''
    dim = 0

    if content_type == 'block' and content_data != None:
        content += '+begin_%s\n+end_%s\n' % (content_data, content_data)

    if content_type == 'files' and content_data != None:
        path = content_data[0]
        extension = content_data[1]
        
        # Makes section name lowercase, deletes punctuation, and replaces spaces by em dashes
        section_type = section[0].lower()
        section_number = section[1].lower()
        section_name = section[2].translate({ord(c): None for c in ',;.:'}).lower().replace(' ', '-')
        iterator = '%i'

        exercise_filename = 'exercise-%s-%s.%s' % (section_number, iterator, extension)
        solution_folder = '%s-%s-%s/' % (section_type, section_number, section_name)

        exercise_path = 'Exercise: file:%s%s.%s\n' % (path, exercise_filename, extension)
        solution_path = 'Solution: file:%s/\n' % solution_folder
        
        content += "%s%s" % (exercise_content, solution_content)
        dim += 1

    return content, dim


def make_tree_heading(section, label):
    """
    """

    iterator = '%i'
    dim = 1

    tree_heading = "%s %s.%s\n" % (label, section[1], iterator)

    return tree_heading, dim
        

def make_tree_model(section, tree_contents, label):
    """Returns a string 'tree_model' and an integer 'dim'.

    The string 'tree_model' is the tree model, built using 'section'
    informations and 'tree_contents'; each tree heading is labeled with 'label'.

    The integer 'dim' is the number of instances of iterators '%i' in
    'tree_model'.

    section: list containing section_type, section_number, section_name
    tree_contents: dictionary containing contents
    label: string

    """

    tree_model, dim = make_tree_heading(section, label)

    # This forces inserting the block at the very beginning (if there is), then
    # the others.
    content_types = list(tree_contents.keys())
    if 'block' in content_types:
        content, content_dim = make_content('block', tree_contents['block'], section)
        tree_model += content
        dim += content_dim

    content_types.remove('block')
    for t in content_types:
        content, content_dim = make_content(t, tree_contents[t], section)
        tree_model += content
        dim += content_dim

    return tree_model, dim


# ===========================
# Functions generating values
# ===========================

def make_exercise_values(number_exercises, dim):
    """Returns a list of tuples, each tuple contains the same number 'dim'
    times. Numbers vary from 1 to 'number_exercises'.

    number_exercises: positive integer
    dim: positive integer

    """

    values = []
    for i in range(1, number_exercises + 1):
        values.append( (i,) * dim )

    return values


# ========================
# Functions printing stuff
# ========================

def print_heading(heading, depth):
    """Prints 'heading' with given 'depth.

    heading: string
    depth: positive integer
    
    """

    prefix = depth * '*'
    print('%s %s' % (prefix, heading))

    
def print_trees(tree_model, values, depth):
    """Prints 'tree_model' replacing its "variables" traversing every value in
    'values'.

    tree_model: string
    values: tuple containing values replacing the "variables" in 'tree_model'
    depth: positive integer

    """

    prefix = (depth + 1) * '*'
    string_model = '%s %s' % (prefix, tree_model)

    for v in values:
        print(string_model % v)

        
# ===================
# Functions for cases
# ===================

def print_exercise_tree():
    """Asks for sections, blocks and files to print a list of trees for exercises.

    """

    # Asks data to user
    section = ask_section() # section_type, section_number, section_name
    tree_contents = ask_contents() # Blocks, links, etc.
    number_exercises, depth = ask_printing_data()

    # Makes string models
    heading = make_heading(section)
    # tree_heading, dim_2 = make_tree_heading('Exercise', section[1])
    tree_model, dim = make_tree_model(section, tree_contents, 'Exercise')

    # Prints tree
    values = make_exercise_values(number_exercises, dim)
    print_heading(heading, depth)
    print_trees(tree_model, values, depth)


# def print_numbered_string():
#     """
#     """

#     # Asks data to user
#     string_model = 
    

#     print_trees(tree_model, values, depth)


# ====================
# Function asking case
# ====================

def prompt_command():
    """Fa il prompt di un comando.

    Supporta il "substring" (scrivere una sottostringa anziché l'intera stringa
    del comando). Per ora è anche case sensitive.

    Comandi supportati:
    1. 'exercise' per stampare l'albero degli esercizi per org-mode.
    1. 'string' per stampare una lista di sottoalberi (solo headings).

    Per terminare la sessione, dare 'Invio' (stringa vuota) al prompt.

    """

    print("Insert command:")

    while True:
        query = input("> ")

        if query == '':
            break
        elif query in "exercise":
            print_exercise_tree()
        elif query in "string":
            pass

    print("Goodbye.")
        

# ======
# Script
# ======

prompt_command()
