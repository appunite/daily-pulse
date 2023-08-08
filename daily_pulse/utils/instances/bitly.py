bitly_token = None

def initBitLy(app):
    global bitly_token

    bitly_token = app.config.get("BITLY_TOKEN")
