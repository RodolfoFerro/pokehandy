# ============================================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# Script: Tools script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ============================================================================

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def parse_deck_from_tcgo(deck_string):
    """Parse a deck string from TCGO format.
    
    Parameters
    ----------
    deck_string : str
        Deck string in TCGO format.
        
    Returns
    -------
    pokemon_raw : list
        List of Pokémon cards in the deck in raw format.
    trainer_raw : list
        List of Trainer cards in the deck in raw format.
    energy_raw : list
        List of Energy cards in the deck in raw format.
    """

    raw_deck = deck_string.split("\n\n")

    pokemon_raw = raw_deck[2].split("\n")
    trainer_raw = raw_deck[4].split("\n")
    energy_raw = raw_deck[6].split("\n")

    return pokemon_raw, trainer_raw, energy_raw


def parse_raw_to_info(cards_string_list):
    """Parse a list of cards in raw format to a list of cards in
    processable info.

    Parameters
    ----------
    cards_string_list : list
        List of cards in raw format.
    
    Returns
    -------
    cards_info : list
        List of cards in processable format.
    """

    cards_info = []

    for card in cards_string_list:
        card_info = card.split(" ")
        qty_ = card_info[1]
        set_ = card_info[-2]
        num_ = card_info[-1]

        cards_info.append({
            "qty": qty_,
            "set": set_,
            "num": num_
        })
    
    return cards_info


def durstenfeld(cards_list):
    """The Modern version of Fisher-Yates shuffling algorithm.
    
    Parameters
    ----------
    cards_list : list
        List of cards to shuffle.
    
    Returns
    -------
    shuffled_cards : list
        Shuffled list of cards.
    """
    
    shuffled_list = cards_list.copy()

    n = len(shuffled_list)

    for i in range(n - 1, 0, -1):
        j = randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    
    return shuffled_list