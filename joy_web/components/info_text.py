import reflex as rx
from joy_web.styles.styles import Size as Size
from joy_web.styles.colors import Color as Color
from joy_web.styles.colors import TextColor as ColorT

def info_text(title: str, body:str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title, font_weight="bold", 
            #color=Color.PRIMARY.value, 
            color="#FDFEFE",
            font_size="0.9em"
        ),
        f"{body}", font_size="0.9em",
        color= ColorT.BODY.value
    )