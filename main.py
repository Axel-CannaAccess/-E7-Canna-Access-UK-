import os

from langchain.retrievers.you import YouRetriever
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


os.environ["YDC_API_KEY"] = "YOUR YOU.COM API KEY"
os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"
yr = YouRetriever()
model = "gpt-3.5-turbo-16k"
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model=model), chain_type="stuff", retriever=yr)

qa.run("how was the New York City pinball ban lifted?")

import requests

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": os.environ["AUTH_KEY"]}
    results = requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        headers=headers,
    ).json()

    # We return many text snippets for each search hit so
    # we need to explode both levels
    return "\n".join(["\n".join(hit["snippets"]) for hit in results["hits"]])


def get_cohere_prompt(query, context):
    return f"""given a question and a bunch of snippets context try to answer the question using the context. If you can't please say 'Sorry hooman, no dice'.
question: {query}
context: {context}
answer: """

def ask_cohere(query, context):
    try:
        return cohere_client.generate(prompt=get_cohere_prompt(query, context))[
            0
        ].text
    except Exception as e:
        print(
            "Cohere call failed for query {} and context {}".format(query, context)
        )
        print(e)
        return "Sorry hooman, no dice"


