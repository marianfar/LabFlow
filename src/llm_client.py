'''
Prepare a request for an LLM.
'''

import json


def build_llm_request(instruction):
    """Build a structured request for an LLM to interpret a transfer instruction."""

    request = {
        "instruction": instruction,
        "requirements": {
            "action": "transfer_liquid",
            "required_fields": [
                "action",
                "source",
                "destination",
                "volume_ul",
            ],
            "allowed_wells": ["A1", "A2", "B1", "B2"],
            "max_volume_ul": 200,
            "output_format": "json",
        },
    }

    return json.dumps(request, indent=2)

#Function safely converts a model's JSON response into a Python dictionary
def parse_llm_response(response_text):
    """Parse a model's JSON response into a Python dictionary."""
    try:
        response = json.loads(response_text) #parse the JSON string into a Python dictionary
    except (json.JSONDecodeError, TypeError): #prevents malformed JSON from crashing the program
        return None

    if not isinstance(response, dict): #if the parsed response is not a dictionary, return None
        return None

    return response

