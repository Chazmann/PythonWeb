import reflex as rx
from PythonWeb.views.header.header import header
from PythonWeb.views.link_button import link_button


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="RC", variant="solid", high_contrast=True),
            rx.hover_card("Hola Reflex"),
            rx.spacer(),
            rx.button("texto2"),
        ),
        rx.flex(
            rx.avatar(src="/logo.jpg", fallback="LC", size="9"),
            rx.text("Leandro Chaz", weight="bold", size="4"),
            rx.text("@reflexuser", color_scheme="gray"),
            rx.button("Edit Profile",
                      color_scheme="indigo",
                      variant="solid",
                      ),
            direction="column",
            spacing="1",
        ),

        rx.spacer(),
        header(),
        rx.spacer(),
        link_button("mouredev", "https://youtube.com")

    )


app = rx.App()

app.add_page(index)
app.compile
