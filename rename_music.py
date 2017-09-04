# -*- coding: utf-8 -*-

###############################################################################################
#Ce programme renomme les chansons d'un dossier de manière à les trier dans un ordre aléatoire#
###############################################################################################


"""Ce programme servira donc a renommmer les chansons d'un dossier. On pourra choisir le nombre de 'groupes' qu'il faut faire,
    par exemple si on veut séparer de la musique électro de musiques des années 80 on peut choisir différents groupes pour que
    les années 80 arrivent après. coucou
"""

import os
import random

def getSong(path):
    """Get the songs in a folder and a list of it

    Parameters
    ----------
    path: the path where the songs are (str)

    Return
    ------
    songs: list of all song (list)

    """

    songs = os.listdir(path)
    return songs

def classSong(songs, pre_class_songs):
    """
    This function will class the songs in the differents pre-group
    :param songs: list/tuple with all songs
    :param pre_class_songs: dict with all songs sort by groups
    :return: pre_class_songs: dict with all songs sort by groups
    """

    for song in songs:
        group = input('Dans quel groupe mettre %s ? '%(song))
        pre_class_songs['group_' + str(group)].append(song)

def rename_music(path):
    """

    :param path: the path were the songs are and where we have to work (str)

    :return:
    """

    os.chdir(path)
    here=os.getcwd()
    songs=getSong(path)

    last_count=1
    pre_class_songs, nbr_group = creating_group()
    classSong(songs, pre_class_songs)
    for groups in range(nbr_group):
        sorte = input('\nDans quel mode voulez vous classer le groupe %d "%s"?\n\n\t1 : Automatique (vous n\'avez rien à faire)\n\t2 : Aléatoire (Pareil, rien à faire sauf que les chansons sont mises dans un ordre aléatoire)\n\t3 : Manuel (À vous de jouer)\n\nMode : ' %(groups+1, pre_class_songs[groups+1]))
        if sorte == 1:
            pre_class_songs, last_count = rename_auto(pre_class_songs,  groups,last_count)
        elif sorte ==2:
            pre_class_songs, last_count = rename_random(pre_class_songs,groups,last_count)
        elif sorte ==3:
            break

def creating_group():
    """
    Just creating the groups to class the songs
    :return:nbr_group : the number of groups (int)
    :return:pre_class_songs: empty dict for the songs
    """

    nbr_group = input('Combien de groupes ? ')
    pre_class_songs = {}
    for i in range(nbr_group):
        name = raw_input("Quel est le nom du %de groupe? " % (i+1))
        pre_class_songs['group_' + str(i + 1)] = []
        pre_class_songs[i+1] = name

    return pre_class_songs, nbr_group

def rename_random(pre_class_songs, num_group, last_count=1):
    """
    This function will rename the songs of a group with random number
    :param pre_class_songs: Dict with all songs pre classed by groups (dict)
    :param num_group: number of the group we have to class (int)
    :param last_count: This is the last number we use to class the songs (int)
    :return: pre_class_songs: idem && compteur : the count of songs
    """

    compteur= last_count
    thisGroup = pre_class_songs['group_' + str(num_group + 1)]

    while len(thisGroup) != 0:
        randomInt = random.randint(0, len(thisGroup)-1)

        if compteur <10:
            os.rename(thisGroup[randomInt], '00' + str(compteur) +'-'+ thisGroup[randomInt])
        elif compteur >10 and compteur < 100:
            os.rename(thisGroup[randomInt], '0' + str(compteur) + '-' + thisGroup[randomInt])
        else:
            os.rename(thisGroup[randomInt], str(compteur) + '-' + thisGroup[randomInt])

        thisGroup.remove(thisGroup[randomInt])
        compteur+=1

    return pre_class_songs, compteur

def rename_auto(pre_class_songs, num_group, last_count=1):
    """
    This function will class and rename the songs automaticaly, just taking the latest number and rename the songs with i+1 (sort by groups)
    :param pre_class_songs: Dict with all the songs pre classed by groups.
    :param nbr_group: number of the group we have to class (int)
    :param last_count: This is the last number we use to class the songs
    :return: compteur: count of songs && pre_class_songs : idem
    """

    compteur = last_count
    for song in pre_class_songs['group_' + str(num_group + 1)]:
        if compteur < 10:
            os.rename(song, '00' + str(compteur) + '-' + song)
        elif compteur >= 10 and compteur < 100:
            os.rename(song, '0' + str(compteur) + '-' + song)
        else:
            os.rename(song, str(compteur) + '-' + song)

        compteur += 1
    return pre_class_songs, compteur

def reset(path):
    """
    remet les musiques sans numéro devant
    :param path: the path were the songs are and where we have to work (str)
    :return:
    """

    songs=os.listdir(path)
    os.chdir(path)
    for music in songs:
        os.rename(music, music[4:])
    

rename_music('/home/william/Bureau/musique_cle2/')
