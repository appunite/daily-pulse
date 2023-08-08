import os
from langchain.llms import OpenAI

llm = None
llm_creative = None

def initLLM(app):
    global llm, llm_creative

    llm = OpenAI(temperature=int(app.config.get("LLM_TEMP")))
    llm_creative = OpenAI(temperature=int(app.config.get("LLM_CREATIVE_TEMP")))
