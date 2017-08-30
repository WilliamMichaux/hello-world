# -*- coding: utf-8 -*-

###############################################################################################
#Ce programme renomme les chansons d'un dossier de manière à les trier dans un ordre aléatoire#
###############################################################################################


"""Ce programme servira donc a renommmer les chansons d'un dossier. On pourra choisir le nombre de 'groupes' qu'il faut faire,
    par exemple si on veut séparer de la musique électro de musiques des années 80 on peut choisir différents groupes pour que
    les années 80 arrivent après.
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


def rename_music(path):
    """

    :param path: the path were the songs are and where we have to work (str)

    :return:
    """

    os.chdir(path)
    here=os.getcwd()
    songs=getSong(path)

    nbr_group = input('Combien de groupes ? ')

    pre_class_songs={}
    for i in range(nbr_group):
        pre_class_songs['group_' + str(i+1)]=[]

    for song in songs:
        group = input('Dans quel groupe mettre %s ? '%(song))
        pre_class_songs['group_' + str(group)].append(song)

    compteur=1
    for i in range(nbr_group):
        for song in pre_class_songs['group_' + str(i+1)]:
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
    

rename_music('/home/william/Bureau/musique_cle/')
