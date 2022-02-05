# ============================================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# Script: Main app. [WIP - Work In Progress]
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ============================================================================

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import streamlit as st
from pokemontcgsdk import RestClient
from pokemontcgsdk import Set
from pokemontcgsdk import Card

from tools import parse_deck_from_tcgo
from tools import parse_raw_to_info



# ============================================================================
# Pokémon TCG SDK Config
# ============================================================================
API_KEY = "YOUR_API_KEY"
RestClient.configure(API_KEY)


# ============================================================================
# Sidebar
# ============================================================================
raw_deck = st.sidebar.text_area(
    "Introduce your deck as exported from Pokémon TCGO:", 
    height=300
)
st.sidebar.button("Simulate")


# ============================================================================
# Main View
# ============================================================================
st.markdown("""
# Pokéhandy – Pokémon Hand Simulator

This application aims to simulate the hand of a Pokémon TCG player.
""")

pokemon_raw, trainer_raw, energy_raw = parse_deck_from_tcgo(raw_deck)

pokemon_info = parse_raw_to_info(pokemon_raw)
trainer_info = parse_raw_to_info(trainer_raw)
energy_info = parse_raw_to_info(energy_raw)


# ============================================================================
# Display all cards
images_list = ""

for poke_info in pokemon_info:
    set_to_look_up = poke_info.get("set")
    num_to_look_up = poke_info.get("num")

    sets = Set.where(q=f"ptcgoCode:{set_to_look_up}")
    set_ = sets[0].id

    card_to_look_up = set_ + "-" + num_to_look_up
    card = Card.find(card_to_look_up)

    img_url = card.images.small

    images_list += f'<img src="{img_url}" alt="{card.name}" width="50px">\n'



for poke_info in trainer_info:
    set_to_look_up = poke_info.get("set")
    num_to_look_up = poke_info.get("num")

    sets = Set.where(q=f"ptcgoCode:{set_to_look_up}")
    set_ = sets[0].id

    card_to_look_up = set_ + "-" + num_to_look_up
    card = Card.find(card_to_look_up)

    img_url = card.images.small

    images_list += f'<img src="{img_url}" alt="{card.name}" width="50px">\n'

st.components.v1.html(images_list)

# ============================================================================
# Attributes to consider from cards:

# st.write(card.images.large)
# st.write(card.name)
# st.write(card.subtypes)
# st.write(card.number)
# st.write(card.supertype)
# st.write(card.set.name)
# st.write(card)


