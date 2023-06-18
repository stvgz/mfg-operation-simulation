from api.api import app

if __name__ == "__main__":

    import unicorn

    unicorn.run(app, host = '0.0.0.0', port = 8000)