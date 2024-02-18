import reflex as rx
import joy_web.styles.styles as styles
from joy_web.styles.styles import Size as Size
from joy_web.components.link_icon import body_icon
from joy_web.styles.styles import Color as Color


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    #is_external = False if (title != "Mi equipo de trabajo" or title != "Regalame un cafecito!") else True
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.chakra.vstack(
                    rx.chakra.text(
                        title, 
                        style=styles.button_title_style
                    ),
                    rx.chakra.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%",
            ),
            
        ),
        is_external=True,
        href=url,
        width="100%",
    )

class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def link__second_button(title: str, body: str, image: str) -> rx.Component:
    #is_external = False if (title != "Mi equipo de trabajo" or title != "Regalame un cafecito!") else True
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.chakra.vstack(
                    rx.chakra.text(
                        title, 
                        style=styles.button_title_style
                    ),
                    rx.chakra.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                
                width="100%",

            ),
            on_click=DrawerState.top,
        ),
        rx.chakra.drawer(
        rx.chakra.drawer_overlay(
            rx.chakra.drawer_content(
                rx.chakra.drawer_header("PRÓXIMAMENTE..."),
                    rx.chakra.drawer_body(
                        body_icon(
                            "icons/gears-solid.svg"
                        ),
                    ),
                 
                rx.chakra.drawer_footer(
                    rx.chakra.button(
                        "Aceptar", on_click=DrawerState.top
                    )
                ),
            )
        ),
        placement="top",
        is_open=DrawerState.show_top,
    ),
        
        is_external=False,
        width="100%",
    )