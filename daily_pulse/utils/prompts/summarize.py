from langchain.prompts import PromptTemplate

SUMMARIZE_SINGLE_LONG_PROMPT_TEMPLATE = """Summarize text below in points. Provide important information.

Summarize Title
Summarize "Context"
Summarize "What problems do we aim to solve"
Summarize "Hypothesis"
Summarize "Implementation plan"
Summarize "Why the owner(s) should make this decision"

{text}
"""

SUMMARIZE_SINGLE_SHORT_PROMPT_TEMPLATE = """
Summarize the following information in a short, catchy, engaging sentence in English.

Examples (DO NOT USE THEM):
- Our health industry client in the USA is proving to be a bit difficult with their lack of openness and strange demands. Plus, they won't even review our NDA template. Can we really trust them?
- We're migrating to GA4 and creating a Slack channel to keep things organized. Efficiency, baby!
- Our improved exit interview process will give us valuable feedback and keep the team running smoothly.
- We're launching a new product next month and our team is working tirelessly to make it a success. Buckle up, it's going to be a wild ride!
- We're expanding our team and hiring for several positions. Know anyone who would be a perfect fit? Let us know!

Write ONLY IN ENGLISH:

{text}
"""

SUMMARIZE_CTA_DAY_PROMPT_TEMPLATE = """
Write a catchy sentence ending a summary of decisions from yesterday. Use emojis.


"""

SUMMARIZE_NO_DOCUMENTS_CTA_TEMPLATE = """
Write a catchy sentence informing that there were no decisions yesterday and engaging to write some. Use emojis


"""

SUMMARIZE_SINGLE_LONG_PROMPT = PromptTemplate(
    template=SUMMARIZE_SINGLE_LONG_PROMPT_TEMPLATE, input_variables=["text"]
)
SUMMARIZE_SINGLE_SHORT_PROMPT = PromptTemplate(
    template=SUMMARIZE_SINGLE_SHORT_PROMPT_TEMPLATE, input_variables=["text"]
)
SUMMARIZE_CTA_DAY_PROMPT = PromptTemplate(
    template=SUMMARIZE_CTA_DAY_PROMPT_TEMPLATE, input_variables=[]
)
SUMMARIZE_NO_DOCUMENTS_CTA_PROMPT = PromptTemplate(
    template=SUMMARIZE_NO_DOCUMENTS_CTA_TEMPLATE, input_variables=[]
)
