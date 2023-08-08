
"""App main handler"""

from daily_pulse.handler.transform import handleTransform

def handler(app):
    handleTransform(app)