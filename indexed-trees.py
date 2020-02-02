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
    
def ask_section():
    """
    """

    print("Insert: section_type @ section_number @ section_name (separated by @)")
    section = input("> ").split("@")

    return section


def ask_contents():
    """
    """

    tree_contents = {}
    
    print("Insert: block name (if not, leave blank)")
    tree_contents['block'] = input("> ")
    
    print("Insert: files path @ file extension (if not, leave blank)")
    tree_contents['files'] = input("> ").split("@")

    return tree_contents

    
def ask_printing_data():
    """
    """

    print("Insert: number of iterations @ depth (separated by @)")
    number_iterations, depth = input("> ").split("@")
    dim = 1

    return number_iterations, depth, dim


# ==============================
# Functions making string models
# ==============================

def make_heading(section):
    """
    """

    heading = "%s %s - %s\n" % tuple(section)
    return heading


def make_content(content_type, content_data, section):
    """
    """

    content = ''
    dim = 0

    if content_type == 'block':
        content += '+begin_%i\n+end_%i\n' % (content_data, content_data)
        dim += 1

    if content_type == 'files':
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
        

def make_tree_model(section, tree_contents, label):
    """
    """

    iterator = "%i"
    dim = 1
    
    tree_model = "%s %s.%s\n" % (label, section[1], iterator)

    # This forces inserting the block at the very beginning (if there is), then
    # the others.
    content_types = tree_contents.keys()
    if 'block' in content_types:
        content, content_dim = make_content('block', tree_contents['block'], section)
        tree_model += content
        dim += content_dim

    content_types.remove('block')
    for t in content_types:
        content, content_dim += make_content(t, tree_contents[t], section)
        tree_model += content
        dim += content_dim

    return tree_model, dim


# ===========================
# Functions generating values
# ===========================

def make_exercise_values(number_exercises, dim):
    """
    """

    values = []
    for i in range(1, number_exercises + 1):
        values.append( (i,) * dim )

    return values


# ========================
# Functions printing stuff
# ========================

def print_heading(heading, depth):
    """
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

    for v in values:
        print(tree_model % v)

        
# ===================
# Functions for cases
# ===================

def print_exercise_tree():
    """
    """

    # Asks data to user
    section = ask_section() # section_type, section_number, section_name
    tree_contents = ask_contents # Blocks, links, etc.
    number_exercises, depth, dim_1 = ask_printing_data()

    # Makes string models
    heading = make_heading(section)
    # tree_heading, dim_2 = make_tree_heading('Exercise', section[1])
    tree_model, dim_c = make_tree_model(section, tree_contents, 'Exercise')
    dim = dim_c + dim_p

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
