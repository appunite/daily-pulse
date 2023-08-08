"""Instances package"""

from daily_pulse.utils.instances.bitly import initBitLy
from daily_pulse.utils.instances.slack import initSlack
from daily_pulse.utils.instances.llm import initLLM

def instances(app):
    initLLM(app)
    initSlack(app)
    initBitLy(app)
    