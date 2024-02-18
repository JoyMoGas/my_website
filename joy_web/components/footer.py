import reflex as rx
import datetime
#import pjs.constants as const
from joy_web.styles.styles import Size as size
from joy_web.styles.colors import TextColor as ColorT
from joy_web.styles.colors import Color as Color

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="logo (3).png",
            height=size.XXXL.value,
            weight=size.XXXL.value,
            alt="Logotipo de JoyMoGas, Una \"jota\" entre paréntesis seguido de un punto y coma"
            ),
        rx.chakra.text("From Sonora to the World",
                font_size=size.MEDIUM.value,
                margin_top=size.ZERO.value,
                ), 
        rx.chakra.link(
                rx.chakra.span("Puedes ver el codigo de ésta página en mi ", color=ColorT.BODY.value,),
                rx.chakra.span("GitHub", color="#85C1E9"),
                href="https://github.com/JoyMoGas",
                is_external=True,
                font_size=size.MEDIUM.value
                ),
             
        rx.chakra.text(f"© 2022-{datetime.date.today().year}", 
                font_size=size.MEDIUM.value
                ),
        margin_bottom=size.BIG.value,
        padding_bottom=size.XL.value,
        padding_x=size.BIG.value,
        spacing=size.DEFAULT.value,
        color=ColorT.HEADER.value,
        #background=Color.BACKGROUND.value
    )