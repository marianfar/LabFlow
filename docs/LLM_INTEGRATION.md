
# Future LLM Integration

## Status

LLM integration is planned but not currently active. LabFlow currently uses a rule-based interpreter. The request builder and JSON response parser are implemented and tested, but no external model is called.

## Intended workflow

1. Receive a natural-language liquid-transfer instruction.
2. Build a request containing the instruction and project requirements.
3. Send the request to an LLM using an API client.
4. Parse the model's JSON response.
5. Validate the resulting transfer with `validate_transfer_all()`.
6. Simulate the transfer only if validation succeeds.

## Example API client

If API access becomes available, install the official OpenAI Python SDK:

```bash
python -m pip install openai
```

Configure the API key and a currently supported model name as environment variables. Never commit API keys to GitHub.

On macOS or Linux, for example:

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_MODEL="your_supported_model_name"
```

The following example illustrates the future API call. It is not currently used by LabFlow.

```python
import os

from openai import OpenAI

from src.llm_client import (
    build_llm_request,
    parse_llm_response,
)


def interpret_with_llm(instruction):
    """Send an instruction to an LLM and parse its response."""

    request_json = build_llm_request(instruction)

    client = OpenAI()

    response = client.responses.create(
        model=os.environ["OPENAI_MODEL"],
        instructions=(
            "Convert the supplied laboratory transfer instruction "
            "into a JSON object with the fields action, source, "
            "destination, and volume_ul. Return only the JSON object. "
            "Do not invent missing information."
        ),
        input=request_json,
    )

    return parse_llm_response(response.output_text)
```

## Connecting the API client to the pipeline

The pipeline could call `interpret_with_llm()` instead of the current rule-based `interpret_instruction()`.

The parsed response must still pass through the existing simulator and validator:

```python
transfer = interpret_with_llm(instruction)

if transfer is None:
    return False, "Could not interpret instruction."

return simulate_transfer(transfer)
```

This is illustrative code for a future change, not a replacement for the current working pipeline.

## Validation and limitations

- A valid JSON response is not necessarily a valid transfer instruction.
- The validator must independently check required fields, types, allowed wells, volume limits, and source/destination constraints.
- API errors, missing responses, malformed JSON, and model refusals must be handled safely.
- Model-generated instructions must never directly control physical laboratory equipment.
- Prompt instructions alone do not guarantee structured or correct output. A future implementation could use the provider's structured-output features and still retain independent validation.

## References

- OpenAI Python SDK: https://developers.openai.com/api/reference/python
- OpenAI Structured Outputs: https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses
- OpenAI API quickstart: https://developers.openai.com/api/docs/quickstart
