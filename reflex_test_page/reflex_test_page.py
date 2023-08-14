"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import asyncio
from datetime import datetime

from rxconfig import config



import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    x_data = []
    y_data = []
    
    update_status: bool = False
    
    async def update_data(self):
        await asyncio.sleep(1)
        if self.update_status:
            return self.update_data


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.box(
                rx.text("hello")
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="5%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
