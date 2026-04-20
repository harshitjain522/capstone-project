from ecommerce_assistant.graph import run_agent

def test_bot():
    res = run_agent("What is return policy?")
    assert "return" in res["answer"].lower()