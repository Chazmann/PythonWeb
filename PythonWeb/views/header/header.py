import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.accordion.root(
            rx.accordion.item(
                header="Órdenes",
                content="Creación de nueva órden",
                font_size="3em",
               
            ),
            rx.accordion.item(
                header="Recetas",
                content="Generar nueva receta",
                font_size="3em",
            ))


    )
