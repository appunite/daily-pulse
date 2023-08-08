
"""Notion data to shortened text handler"""
from daily_pulse import app

def handleTransform(app):
    @app.route('/transform', methods=['POST'])
    def transform():
        return 'OK'
