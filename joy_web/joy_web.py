import reflex as rx
from joy_web.components.navbar import navbar
from joy_web.components.footer import footer
from joy_web.views.header.header import header
from joy_web.views.links.links import links
from joy_web.views.sponsors.sponsors import sponsors
import joy_web.styles.styles as styles
from joy_web.styles.styles import Size as size

# CTRL+MAYUS-P (ABRIR BARRA DE BUSQUEDA)

def index() -> rx.Component:
    #return rx.chakra.button("Hola Reflex!", variant="outline", color_scheme="red")
    #return rx.chakra.text("Hola Reflex!")
    return rx.chakra.box(
        navbar(), # BARRA ARRIBA -FIJA
        rx.chakra.center(
            rx.chakra.vstack(
                header(), # TEXTO
                links(), # BTONES
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=size.XL.value,# MARGEN AFUERA DEL CONTENEDOR
                padding=size.BIG.value 
            )
        ),
        footer(),# BARRA ABAJO
        padding="2px"
    )

    


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
    )       
app.add_page(
    index,
    title= "JoyMoGas | Software Developer",
    description="Hola, mi nombre es José Montaño. Soy Software Developer, aprendiendo desarrollo web con Python Reflex!",
    image="logo (3).png"
    )


# .venv\Scripts\activate     PWSH
# Activar entorno, 
# commit,
# reflex init
# reflex run
# sh build.sh
# ./build.sh
# source .venv/bin/activate

# ** TOMAR EN CUENTA COMPONENTE COMMENT/ALERT