import reflex as rx
import joy_web.styles.styles as styles
from joy_web.styles.styles import Size as size
from joy_web.styles.colors import TextColor as ColorT
from joy_web.styles.colors import Color as Color
from joy_web.styles.fonts import Font, FontWeight

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.span("JOY", color=ColorT.BODY.value,),
            rx.chakra.span("MOGAS", color=ColorT.FOOTER.value,),
            style=styles.navbar_title_style,
            ),
           
           position="sticky",   
           bg = Color.CONTENT.value,
           padding_x=size.BIG.value,
           padding_y=size.DEFAULT.value,
           z_index="999",
           top="0"
    )