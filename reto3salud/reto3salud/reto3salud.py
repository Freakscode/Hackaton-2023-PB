"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Bienvenido a DATA-HRI", font_size="2em"),
            rx.box("HOLA", rx.code(filename, font_size="1em")),
            rx.image(src="visual/DATA-HRI.png",  width="100px",
                    height="auto",
                    border_radius="100px 50px",
                    border="5px solid #555",
                    box_shadow="lg"),
            rx.box(" ", rx.code(filename, font_size="1em")),
            rx.hstack(
                    rx.input(placeholder="Ingresa Tú Nombre"),
                    rx.button("Nombre")),
            rx.link(
                "¡Revisa Nuestra Guía Completa!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )



# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
