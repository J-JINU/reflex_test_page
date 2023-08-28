"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import asyncio
from datetime import datetime
import json
import os
import requests

from rxconfig import config
import reflex as rx
import firebase_admin
from firebase_admin import auth, credentials, exceptions

for root, dirs, files in os.walk("./reflex_test_page"):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root, file)

cred = credentials.Certificate(path)
default_app = firebase_admin.initialize_app(cred)


login_welcome = """
Sign in to your account and unlock a world of possibilities.
"""

signup_welcome = """
Create an account today and discover a platform tailored to your interests,
where you can connect, explore, and engage with like-minded individulas.
"""

class MainState(rx.State):
    pass


class SignUpState(MainState):
    loadingText: str = ""
    pass
    

class LoginState(MainState):
    email: str = ""
    password: str = ""
    placeEmail: str = "Email"
    placePassword: str = "Password (min. 6char)"
    borderEmail: str = "" 
    borderPassword: str = ""
    btnName: str = "login"
    
    def get_login_email(self, email):
        self.email = email
    
    def get_login_password(self, password):
        self.password = password
    
    def restart_page(self):
        self.email = ""
        self.password = ""
        self.placeEmail = "Email"
        self.placePassword = "Password (min. 6char)"
        self.borderEmail = ""
        self.borderPassword = ""
        self.btnName = "login"
        


class CustomInputs(rx.Input):
    def __init__(
        self,
        placeholder: str,
        type_: str,
        value: rx.State,
        on_change: callable,
        border_color: rx.State
    ):
        super().__init__(
            placeholder=placeholder,
            typy=type_,
            value=value,
            on_change=on_change,
            border_color=border_color,
        )
        

class CustomButton(rx.Button):
    def __init__(
        self,
        children: list,
        is_loading: bool,
        is_disabled: bool,
        on_click: callable,
        loading_text: SignUpState.loadingText,
    ):
        super().__init__(
            children=children,
            is_loading=is_loading,
            is_disabled=is_disabled,
            on_click=on_click,
            loading_text=loading_text,
        )


class PageView:
    def __init__(self, components: list):
        self.components = components
        self.toggle_theme = rx.color_mode_button(rx.color_mode_icon())
        self.stack = rx.vstack(
            rx.box(
                self.toggle_theme,
                width="100%",
                height="5rem",
                display="flex",
                justify_content="center",
            ),
            width="100%",
            height="100vh",
            padding="2rem",
            display="flex",
            align_item="center",
            spacing="1rem",
        )
        super().__init__()
        
    def bulid(self):
        for component in self.components:
            self.stack.children.append(component)
            
        return self.stack


@rx.route("/signup")
def signup():
    return rx.text("hello world!")

@rx.route("/", on_load=LoginState.restart_page)
def login():
    components: list = [
        rx.heading("Reflex Login Form"),
        rx.container(rx.text(login_welcome)),
        rx.vstack(
            rx.spacer(),
            CustomInputs(
                LoginState.placeEmail,
                "text",
                LoginState.email,
                LoginState.get_login_email,
                LoginState.borderEmail,
            ),
            CustomInputs(
                LoginState.placePassword,
                "password",
                LoginState.password,
                LoginState.get_login_password,
                LoginState.borderPassword,
            ),
            CustomButton(
                
            ),
            # width="100%",
            height="15rem",
            justify_content="center",
            spacing="1.35rem",
        ),
    ]
    login = PageView(components)
    return login.bulid()

FONT = "Helvetica"
style = {
    rx.Text: {
        "font_size": ["100%", "115%", "130%", "135%", "125%"],
        "font_family": FONT,
        "transition" : "all 750ms ease",
        "text_align" : "center",
    },
    rx.Heading: {
        "font_size" : ["300%", "350%", "380%", "400%", "450%"],
        "text_align" : "center",
        "transition" : "all 750ms ease",
    },
    # CustomInputs: {
    #     "width": ["85%", "85%", "60%", "45%", "35%"],
    #     "height": "3.25rem",
    #     "transition": "all 550ms ease",
    #     "_hover": {"box_shadow": "0 3px 6px 0 rgba(90, 116, 148, 0.2)"},
    # },
    # CustumButton: {
    #     "width": ["85%", "85%", "60%", "45%", "35%"],
    #     "height": "4rem",
    #     "transition": "all 550ms ease",
    # },
}


# Add state and page to the app.
app = rx.App(state=MainState, style=style)
app.compile()
