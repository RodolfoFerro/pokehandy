"""
Temporal file for testing things.
"""

# ============================================================================
# Display all cards
# images_list = ""

# for poke_info in pokemon_info:
#     set_to_look_up = poke_info.get("set")
#     num_to_look_up = poke_info.get("num")

#     sets = Set.where(q=f"ptcgoCode:{set_to_look_up}")
#     set_ = sets[0].id

#     card_to_look_up = set_ + "-" + num_to_look_up
#     card = Card.find(card_to_look_up)

#     img_url = card.images.small

#     images_list += f'<img src="{img_url}" alt="{card.name}" width="50px">\n'



# for poke_info in trainer_info:
#     set_to_look_up = poke_info.get("set")
#     num_to_look_up = poke_info.get("num")

#     sets = Set.where(q=f"ptcgoCode:{set_to_look_up}")
#     set_ = sets[0].id

#     card_to_look_up = set_ + "-" + num_to_look_up
#     card = Card.find(card_to_look_up)

#     img_url = card.images.small

#     images_list += f'<img src="{img_url}" alt="{card.name}" width="50px">\n'

# st.components.v1.html(images_list)

# ============================================================================
# Attributes to consider from cards:

# st.write(card.images.large)
# st.write(card.name)
# st.write(card.subtypes)
# st.write(card.number)
# st.write(card.supertype)
# st.write(card.set.name)
# st.write(card)

# ============================================================================
# Explorations (18/02/2022)


# if raw_deck != "":
#     pokemon_raw, trainer_raw, energy_raw = parse_deck_from_tcgo(raw_deck)

#     pokemon_info = parse_raw_to_info(pokemon_raw)
#     trainer_info = parse_raw_to_info(trainer_raw)
#     energy_info = parse_raw_to_info(energy_raw)


#     images_list = ""


#     for poke_info in pokemon_info:
#         set_to_look_up = poke_info.get("set")
#         num_to_look_up = poke_info.get("num")

#         sets = Set.where(q=f"ptcgoCode:{set_to_look_up}")
#         set_ = sets[0].id

#         card_to_look_up = set_ + "-" + num_to_look_up
#         card = Card.find(card_to_look_up)

#         handy_card = PokeCard(
#             card.supertype,
#             card.name,
#             card.subtypes,
#             card.number,
#             card.set.name,
#             card.set.id,
#             card.images
#         )

#         st.markdown(handy_card)

#         img_url = card.images.small

#         images_list += f'<img src="{img_url}" alt="{card.name}" width="80px">\n'
    
#     st.components.v1.html(images_list)