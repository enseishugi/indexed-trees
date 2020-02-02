 #!/usr/bin/python3
# -*- coding: utf-8 -*-
# numbered-trees.py

"""Questo script genera un albero per org-mode che corrisponde alla lista di
esercizi di un sectioning specificato dall'utente. Quanti esercizi siano, il
titolo della sezione, il numero della sezione, eccetera, sono indicate
dall'utente.

"""


def sequential_string(s, times, a, b):
    """Stampa la stringa 's' assumendo che ci siano 'times' istanze dello stesso
    indice intero che va da 'a' a 'b'.

    """

    # Costruisce la stringa "s % (i, ..., i)" che contiene 'times' volte 'i'.
    t = "s % (i" + ", i" * (times-1) + ")"

    # Qui è essenziale che 'i' sia l'indice nel ciclo for o dà errore 'eval(t)'
    # perché manca la variabile 'i'.
    for i in range(a, b+1):
        print(eval(t))
        

def print_exercise_tree(sectioning, section_number, section_name, n_exercises, depth, files):
    """Stampa l'albero:
    1. Stampa il titolo : "sectioning" "section_number" - "section_name"
    2. Stampa la stringa modello per ogni esercizio da 1 a 'n_exercises' : Exercise "section_number".%i (+ "blocco exercise")
    3. Se 'files=True', stampa anche i percorsi a file associati all'esercizio.

    >>> Esempio di albero <<<
    
    I dati vengono combinati tipo nell'esempio seguente:
    1. sectioning = "Chapter"
    2. section_number = "V"
    3. section_name = "Simplicial homology"
    4. n_exercises = 3

    *** Stampa ***
    Chapter V - Simplicial homology
    * Exercise V.1
    * Exercise V.2
    * Exercise V.3

    e in ciascun albero dell'esercizio è inserito un blocco "exercise" di
    org-mode.

    """

    # Stringa del titolo dell'albero degli esercizi, aggiustata con la
    # profondità indicata in depth.
    prefix = '*' * depth
    title = "%s %s %s - %s" % (prefix, sectioning, section_number, section_name)

    # Scrive nella variabile 's' la "stringa modello", che è una stringa che
    # contiene un '%i' al suo interno. Questo viene chiamato "iteratore". La
    # stringa viene stampata 'n_exercises' (int > 0) volte e ogni volta al posto
    # di iterator viene inserito un numero (partendo da 1 fino a 'n_exercises').
    # La variabile 'iterator_instances' indica il numero di iteratori
    # all'interno della stringa modello 's'. Questa informazione serve per poter
    # dire alla funzione 'sequential_strings' quante volte compare l'iterator
    # nella stringa modello.

    iterator_instances = 1 # Numero di istanze degli iteratori. A priori abbiamo solo un'istanza.
    
    prefix += '*' # Aggiunge una profondità a quella dichiarata in 'depth'.
    
    iterator = "%i"
    s = ("%s Exercise %s." % (prefix, section_number)) + iterator + "\n"
    s += "#+begin_exercise\n\n#+end_exercise\n"

    # Se è richiesto di creare anche la stringa coi link ai file per gli
    # esercizi (e.g. se sono esercizi di informatica).
    if files:
        file_name = section_name.translate({ord(c): None for c in ',;.:'}).lower().replace(' ', '-') # Rimuovo eventuale punteggiatura
        iterator_instances += 1 # Aggiunge un'altra istanza dell'iteratore
        s += ("\nLo script è file:~/informatica/linguaggi/python/think-python/exercise-%s-" % section_number.lower()) + iterator + ".py\n"
        s += ("Soluzione: file:~/informatica/linguaggi/python/think-python/%s-%s-%s/\n" % (sectioning.lower(), section_number.lower(), section_name.lower()))

    # Stampa il titolo dell'albero
    print(title)

    # Stampa la stringa modello 's' sostituendo l'iterator per ogni intero da
    # 'begin' (default è 1) a 'n_exercises'.
    begin = 1
    sequential_string(s, iterator_instances, begin, n_exercises)
        
    
def make_exercise_tree():
    """Prompt per chiedere:
    1. Sectioning (i.e. chapter/appendix/section/subsection)
    2. Numero del capitolo
    3. Nome del capitolo
    4. Numero esercizi
    5. Profondità dell'albero
    6. Se deve inserire percorsi a file dedicati agli esercizi 

    Usando le informazioni, chiama 'print_exercise_tree' per stampare l'albero.

    """

    print("Insert 'c'/'a'/'s'/'ss' for chapter/appendix/section/subsection (default is 'c')")
    print("Insert chapter/appendix/section/subsection number")
    print("Insert name of the chapter/appendix/section/subsection")
    print("Insert number of exercises")
    print("Insert depth")
    print("Create files (y/n)")
    print("(Each information separted by spaces)\n")

    sectioning_dict = {'c': 'Chapter', 'a': 'Appendix', 's': 'Section', 'ss': 'Subsection'}
    files_dict = {'y': True, 'n': False}
    
    query = input("> ")
    data = query.split()

    sectioning = sectioning_dict[data[0]]
    section_number = data[1]
    section_name = ' '.join(data[2:-3])
    exercises = data[-3]
    depth = data[-2]
    files = data[-1]

    print_exercise_tree(sectioning, section_number, section_name, int(exercises), int(depth), files_dict[files])


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
            make_exercise_tree()
        elif query in "string":
            
        
    print("Goodbye.")
    

# ======
# Script
# ======

prompt_command()

