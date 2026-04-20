from ecommerce_assistant.tools import get_time
from ecommerce_assistant.llm import llm

FAITHFULNESS_THRESHOLD = 0.7
MAX_EVAL_RETRIES = 2


def memory_node(state):
    msgs = state.get("messages", [])
    msgs.append(f"User: {state['question']}")
    return {"messages": msgs[-6:]}


# 🔥 LLM ROUTER
def router_node(state):
    prompt = f"""
Decide the route for this question.

Routes:
- retrieve → for FAQ / policies
- tool → for date/time/calculation
- skip → for memory/chat

Question: {state['question']}

Answer ONLY one word: retrieve / tool / skip
"""

    route = llm.invoke(prompt).content.strip().lower()

    if route not in ["retrieve", "tool", "skip"]:
        route = "retrieve"

    return {"route": route}


def retrieval_node(state, collection, model):
    emb = model.encode([state["question"]]).tolist()
    results = collection.query(query_embeddings=emb, n_results=3)

    context = ""
    sources = []

    for i, doc in enumerate(results["documents"][0]):
        topic = results["metadatas"][0][i]["topic"]
        context += f"[{topic}] {doc}\n"
        sources.append(topic)

    return {"retrieved": context, "sources": sources}


def skip_retrieval_node(state):
    return {"retrieved": "", "sources": []}


def tool_node(state):
    return {"tool_result": get_time()}


# 🔥 LLM ANSWER NODE
def answer_node(state):
    system_prompt = f"""
You are an E-commerce FAQ assistant.

STRICT RULES:
- Answer ONLY from provided context
- If answer not in context → say "I don't know"
- Do NOT hallucinate

Context:
{state.get('retrieved', '')}

Tool Result:
{state.get('tool_result', '')}

Conversation:
{state.get('messages', [])}
"""

    user_prompt = f"Question: {state['question']}"

    response = llm.invoke(system_prompt + "\n" + user_prompt)

    return {"answer": response.content}


# 🔥 LLM EVAL NODE
def eval_node(state):
    if state["retrieved"] == "":
        return {"faithfulness": 1.0, "eval_retries": 0}

    prompt = f"""
Rate how faithful the answer is to the context.

Context:
{state['retrieved']}

Answer:
{state['answer']}

Score between 0 and 1 ONLY.
"""

    try:
        score = float(llm.invoke(prompt).content.strip())
    except:
        score = 0.5

    retries = state.get("eval_retries", 0) + 1

    return {
        "faithfulness": score,
        "eval_retries": retries
    }


def save_node(state):
    msgs = state.get("messages", [])
    msgs.append(f"Bot: {state['answer']}")
    return {"messages": msgs}