import reflex as rx
from PythonWeb.views.header.header import header
from PythonWeb.views.link_button import link_button

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.hstack(
        rx.hover_card("Hola Reflex"),
        rx.button("texto2"),
        rx.spacer(),
        header(),
        rx.spacer(),
        link_button("mouredev", "https://youtube.com" )
       
    )


app = rx.App()

app.add_page(index)
app.compile
