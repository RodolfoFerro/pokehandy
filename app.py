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
from tools import durstenfeld
from card import PokeCard



# ============================================================================
# Pokémon TCG SDK Config
# ============================================================================
API_KEY = "c2ed168e-f9bf-4c75-b975-d66fdc28c404"
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

st.markdown("""
### Card shuffling simulation for A-Z cards.
""")

cards_list = [chr(i) for i in range(65, 91)]
st.markdown(f"""
#### Ordered cards

{cards_list}
""")

shuffled_cards = durstenfeld(cards_list)
st.markdown(f"""
#### Shuffled cards

{shuffled_cards}
""")
