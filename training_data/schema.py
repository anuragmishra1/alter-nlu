# training data json schema

intent_data_schema = {
    "type": "object",
    "properties": {
      "text": {
        "type": "string",
        "minLength": 1
      },
      "intent": {
        "type": "string",
        "minLength": 1
      },
      "entities": {
        "type": "array",
        "blank": True,
        "items": {
          "type": "object",
          "properties": {
            "start": {
              "type": "integer"
            },
            "end": {
              "type": "integer"
            },
            "value": {
              "type": "string",
              "minLength": 1
            },
            "entity": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "start",
            "end",
            "value",
            "entity"
          ]
        }
      }
    },
    "required": [
      "text",
      "intent",
      "entities"
    ]
  }
  
entity_data_schema = {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "minLength": 1
      },
      "data": {
        "type": "array",
        "minItems": 1,
        "items": {
          "type": "object",
          "properties": {
            "value": {
              "type": "string",
              "minLength": 1
            },
            "synonyms": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "string",
                "minLength": 1
              }
            },
          },
          "required": [
            "value",
            "synonyms"
          ]
        }
      }
    },
    "required": [
      "name",
      "data"
    ]
  }

botName = {
  "type": "string",
  "minLength": 1
  }
