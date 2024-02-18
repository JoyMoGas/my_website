import reflex as rx
from enum import Enum
from joy_web.styles.colors import Color as Color
from joy_web.styles.colors import TextColor as ColorT
from joy_web.styles.fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"

# Fonts
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    #"/css/styles.css"
]

# Sizes
class Size(Enum):
    ZERO = "0px !important",
    LITLE="0.3"
    SMALL="0.5em"
    MEDIUM="0.8em"
    X_MEDIUM="0.9em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    XL="3em"
    XXL="4em"
    XXXL="7em"
    XXXXL="10em"
    LOGOS_SIZE="11.5em"

# Styles
    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,

    rx.chakra.Heading:{
        "color": ColorT.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },

    rx.chakra.Button:{
        "width": "100%",
        "height": "100%",
        #"display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": ColorT.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
        },
        rx.chakra.Link: {
            "text_decoration":"none",
            "_hover": {}
        }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,    
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color= ColorT.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    color= ColorT.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_weight=FontWeight.LIGHT.value,
    color= ColorT.BODY.value,
)
