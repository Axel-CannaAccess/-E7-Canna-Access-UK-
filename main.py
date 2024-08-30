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

