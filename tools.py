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

def parse_deck_from_tcgo(deck_string):
    raw_deck = deck_string.split("\n\n")

    pokemon_raw = raw_deck[2].split("\n")
    trainer_raw = raw_deck[4].split("\n")
    energy_raw = raw_deck[6].split("\n")

    return pokemon_raw, trainer_raw, energy_raw


def parse_raw_to_info(cards_string_list):
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