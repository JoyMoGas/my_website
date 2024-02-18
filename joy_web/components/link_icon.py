import reflex as rx
from joy_web.styles.styles import Size as Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=image,
            width=Size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True,
    )

# ** AÑADIR METODO DE ICONO DE HEADERDEL DRAWER

def body_icon(image: str) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.image(
            src=image,
            width=Size.LARGE.value,
        ),
        rx.chakra.text(
            "Trabajando en ello!"
        )
    )
        