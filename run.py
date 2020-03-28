"""Start Server"""
from application import app
import os
import sys

if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=8000, debug=True)
