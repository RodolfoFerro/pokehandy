# ============================================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# Script: Poké Card object.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ============================================================================

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PokeCard:

    def __init__(self, supertype, name, subtypes, number, set, api_set, images):
        self.supertype = supertype
        self.name = name
        self.subtypes = subtypes
        self.number = number
        self.set = set
        self.api_set = api_set
        self.images = images
    
    def __str__(self):

        _str = f"""
        #### [CARD INFO]\n
        - Name: {self.name}\n
        - Number: {self.number}\n
        - Set: {self.set}\n
        - Supertype: {self.supertype}\n
        - Subtype: {self.subtypes}\n
        - Images: 
            - {self.images.small}\n
            - {self.images.large}\n
        """

        return _str
    