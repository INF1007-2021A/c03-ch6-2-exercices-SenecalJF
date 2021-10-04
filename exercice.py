#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames
import time

def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    # dict_nouv = {}
    # for item in some_list:
    #     # dict_nouv.update({some_list.index(item): item})
    #     dict_nouv[some_list.index(item)] = item
    
    return {item: some_list.index(item) for item in some_list}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    # lst_color = []
    # for color in colors:
    #     hex = cnames.get(color)
    #     lst_color.append((color, hex))
    return [(color, cnames.get(color)) for color in colors]



def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    # lst_nbent = []
    # start = time.perf_counter()
    # for i in range(10001):
    #     if not( i >= 15 and i <= 350):
    #          lst_nbent.append(i)
    # end = time.perf_counter()
    # print(end - start)
          
    
    return [i for i in range(10001) if not( i >= 15 and i <= 350)]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    dict_nouv = {}
    for key, value in model_dict.items():
        sum_err = 0
        
        for val in value:
            sum_err += (val[0] - val[1])**2
            
        dict_nouv.update({key: sum_err/len(value)})
        
    return dict_nouv


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    # print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
