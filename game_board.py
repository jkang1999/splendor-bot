"""
Obj that contains the current game board
Input: specific fields
Output: None
"""
# Class that takes information from 'board' field in JSON input and initializes the game board

{
  "active_player_id":1,
  "you":1,
  "move":1,
  "players":[
    {
      "id":1,
      "points":0,
      "gems":{"black":0,"blue":0,"green":0,"red":0,"white":0,"joker":0},
      "discounts":{"black":0,"blue":0,"green":0,"red":0,"white":0},
      "reserved_card_ids":[],
      "purchased_card_ids":[],
      "owned_noble_ids":[],
      "time_bank":20.0
    },
    {
      "id":2,
      "points":0,
      "gems":{"black":0,"blue":0,"green":0,"red":0,"white":0,"joker":0},
      "discounts":{"black":0,"blue":0,"green":0,"red":0,"white":0},
      "reserved_card_ids":[],
      "purchased_card_ids":[],
      "owned_noble_ids":[],
      "time_bank":20.0
    }
  ],
  "board":{
    "gems":{"black":4,"blue":4,"green":4,"red":4,"white":4,"joker":5},
    "face_up_cards":{
      "tier1":[29,13,16,27],
      "tier2":[41,69,44,62],
      "tier3":[87,84,76,90]
    },
    "nobles":[8,6,10]
  }
}