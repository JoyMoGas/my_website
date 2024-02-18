import reflex as rx
#import pjs.styles.styles as styles
from joy_web.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=imagen,
            height=Size.LOGOS_SIZE.value,
            widht="auto",
            alt=alt
        ),  
        href=url,
        is_external=True
    )