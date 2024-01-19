import os
from langchain.llms import OpenAI
from langchain import LLMChain

from daily_pulse.utils.prompts.summarize import (
    SUMMARIZE_SINGLE_LONG_PROMPT,
    SUMMARIZE_SINGLE_SHORT_PROMPT,
    SUMMARIZE_CTA_DAY_PROMPT,
    SUMMARIZE_NO_DOCUMENTS_CTA_PROMPT,
)
from daily_pulse.config import config

llm = OpenAI(temperature=int(config["LLM_TEMP"]), model_name="gpt-3.5-turbo")
llm_creative = OpenAI(
    temperature=int(config["LLM_CREATIVE_TEMP"]), model_name="gpt-3.5-turbo"
)

summarize_individual_long_chain = LLMChain(llm=llm, prompt=SUMMARIZE_SINGLE_LONG_PROMPT)
summarize_individual_short_chain = LLMChain(
    llm=llm, prompt=SUMMARIZE_SINGLE_SHORT_PROMPT
)
summarize_cta_day_chain = LLMChain(llm=llm_creative, prompt=SUMMARIZE_CTA_DAY_PROMPT)
summarize_no_documents_chain = LLMChain(
    llm=llm_creative, prompt=SUMMARIZE_NO_DOCUMENTS_CTA_PROMPT
)
