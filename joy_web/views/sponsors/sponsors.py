import reflex as rx
#import pjs.constansts as const
from joy_web.components.title import title
from joy_web.styles.styles import Size as size
from joy_web.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "/isi.png",
                "http://web.isi.uson.mx",
                "Logotipo de ISI Unison"
            ),
            link_sponsor(
                "/unison.png",
                "https://www.unison.mx",
                "Logotipo de Unison"
            ),
            spacing=size.XXL.value,
            columns=[1,2]
        ),
        width="100%",
        align_items="start"
    )