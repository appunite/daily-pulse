"""Instances package"""

from daily_pulse.utils.instances.bitly import initBitLy
from daily_pulse.utils.instances.llm import initLLM

def instances(app):
    initLLM(app)
    initBitLy(app)
    