# ============================================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# Script: Error replication script.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ============================================================================

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pokemontcgsdk import RestClient
from pokemontcgsdk import Set
from pokemontcgsdk import Card


API_KEY = "YOUR_API_KEY"
RestClient.configure(API_KEY)

# ============================================================================
#  ERROR REPLICATION OF PROMO CARDS
# ============================================================================

# Original card:
#  * 1 Crobat V PR-SW 98
set_from_ptcgo = "PR-SW"
card_number = "98"

sets = Set.where(q=f"ptcgoCode:{set_from_ptcgo}")
set_ = sets[0].id

card_id = set_ + "-" + card_number
print(card_id)
# swshp-98

card = Card.find(card_id)
print(card)
# The previous line returns the following:
"""
Traceback (most recent call last):
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/site-packages/pokemontcgsdk/restclient.py", line 36, in get
    response = json.loads(urlopen(req).read().decode("utf-8"))
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 531, in open
    response = meth(req, response)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 640, in http_response
    response = self.parent.error(
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 569, in error
    return self._call_chain(*args)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 502, in _call_chain
    result = func(*args)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/urllib/request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "find_error.py", line 22, in <module>
    card = Card.find(card_id)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/site-packages/pokemontcgsdk/card.py", line 50, in find
    return QueryBuilder(Card, Card.transform).find(id)
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/site-packages/pokemontcgsdk/querybuilder.py", line 21, in find
    response = RestClient.get(url)['data']
  File "/Users/rodolfoferro/miniforge3/envs/streamlit/lib/python3.8/site-packages/pokemontcgsdk/restclient.py", line 40, in get
    raise PokemonTcgException(err.read())
pokemontcgsdk.restclient.PokemonTcgException: <exception str() failed>
"""