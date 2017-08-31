# -*- coding: utf-8 -*-

###############################################################################################
#Ce programme renomme les chansons d'un dossier de manière à les trier dans un ordre aléatoire#
###############################################################################################


"""Ce programme servira donc a renommmer les chansons d'un dossier. On pourra choisir le nombre de 'groupes' qu'il faut faire,
    par exemple si on veut séparer de la musique électro de musiques des années 80 on peut choisir différents groupes pour que
    les années 80 arrivent après. coucou
"""

import os

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
    :param songs:
    :param pre_class_songs:
    :return:
    """

def rename_music(path):
    """

    :param path: the path were the songs are and where we have to work (str)

    :return:
    """

    os.chdir(path)
    here=os.getcwd()
    songs=getSong(path)

    for song in songs:
        group = input('Dans quel groupe mettre %s ? '%(song))
        pre_class_songs['group_' + str(group)].append(song)

def creating_group():
    """
    Just creating the groups to class the songs
    :return:nbr_group : the number of groups (int)
    :return:pre_class_songs: empty dict for the songs
    """

    nbr_group = input('Combien de groupes ? ')
    pre_class_songs = {}
    for i in range(nbr_group):
        name = raw_input("Quel est le nom du %de groupe" % i)
        pre_class_songs['group_' + str(i + 1)] = []
        pre_class_songs[i] = name


def rename(pre_class_songs, nbr_group):
    """
    This function will class and rename the songs
    :param pre_class_songs: Dict with all the songs pre classed by groups.
    :return: /
    """

    compteur = 1
    for i in range(nbr_group):
        for song in pre_class_songs['group_' + str(i + 1)]:
            if compteur < 10:
                os.rename(song, '00' + str(compteur) + '-' + song)
            elif compteur >= 10 and compteur < 100:
                os.rename(song, '0' + str(compteur) + '-' + song)
            else:
                os.rename(song, str(compteur) + '-' + song)

            compteur += 1

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
    

reset('/home/william/Bureau/musique_cle/')
