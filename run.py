"""Start Server"""
from application import app
import os
import sys

if __name__ == '__main__':
    # app.run(ssl_context='adhoc', host="127.0.0.1", port=8000, debug=True)
    app.run(host=os.getenv("HOST"), port=8000, debug=True)
