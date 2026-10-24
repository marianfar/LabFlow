import json
from src.llm_client import build_llm_request

def test_build_llm_request():
    instruction = "Transfer 50 µL from well A1 to well B1."
    request_json = build_llm_request(instruction)
    request = json.loads(request_json) #convert JSON string back to dictionary for testing

    assert request["instruction"] == instruction
    assert request["requirements"]["action"] == "transfer_liquid"
    assert "source" in request["requirements"]["required_fields"]
    assert "destination" in request["requirements"]["required_fields"]
    assert "volume_ul" in request["requirements"]["required_fields"]
    assert request["requirements"]["allowed_wells"] == ["A1", "A2", "B1", "B2"]
    assert request["requirements"]["max_volume_ul"] == 200
    assert request["requirements"]["output_format"] == "json"


#testthe response parser
from src.llm_client import parse_llm_response


def test_parse_valid_llm_response():
    response_text = (
        '{"action": "transfer_liquid", '
        '"source": "A1", '
        '"destination": "B1", '
        '"volume_ul": 50}'
    )

    result = parse_llm_response(response_text)

    assert result["source"] == "A1"
    assert result["destination"] == "B1"
    assert result["volume_ul"] == 50


def test_reject_malformed_llm_response():
    response_text = "This is not valid JSON"

    result = parse_llm_response(response_text)

    assert result is None
