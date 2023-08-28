"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import asyncio
from datetime import datetime
import json
import os
import requests

from rxconfig import configj
import reflex as rx
import firebase_admin
from firebase_admin import auth, credentials, exceptions



default_app = firebase_admin.initialize_app()

cred = credentials.RefreshToken('path/to/refreshToken.json')
default_app = firebase_admin.initialize_app(cred)


class State(rx.State):
    pass

@rx.page(route="/", title="python firebase login")
def index():
    return  rx.text("helloworld")



# Add state and page to the app.
app = rx.App()
app.compile()
