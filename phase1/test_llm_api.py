import pytest
from llm_client import call_llm

# ── Test 1: Response structure is valid ──────────────────────────────
def test_response_has_expected_keys():
    response = call_llm("What is 2 + 2?")
    assert "text" in response
    assert "input_tokens" in response
    assert "output_tokens" in response
    assert "stop_reason" in response

# ── Test 2: Response is non-empty ────────────────────────────────────
def test_response_text_is_not_empty():
    response = call_llm("Name one planet in our solar system.")
    assert isinstance(response["text"], str)
    assert len(response["text"].strip()) > 0

# ── Test 3: Token usage is positive ──────────────────────────────────
def test_token_usage_is_positive():
    response = call_llm("Say hello.")
    assert response["input_tokens"] > 0
    assert response["output_tokens"] > 0

# ── Test 4: Stop reason is STOP for a normal prompt ──────────────────
def test_stop_reason_is_stop():
    response = call_llm("What colour is the sky?")
    assert response["stop_reason"] == "stop"  # Gemini uses STOP, Claude uses end_turn

# ── Test 5: Factual correctness check ────────────────────────────────
def test_factual_response_contains_expected_keyword():
    response = call_llm("What is the capital of France? Reply in one word.")
    assert "Paris" in response["text"]