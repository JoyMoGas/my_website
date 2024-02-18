import reflex as rx
from joy_web.components.link_icon import link_icon
from joy_web.components.info_text import info_text
from joy_web.styles.styles import Size as Size
from joy_web.styles.colors import Color as Color
from joy_web.styles.colors import TextColor as ColorT


def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name="Jose Montaño", 
                size="xl",
                src="avatar.jpeg",
                color=ColorT.BODY.value,
                bg = Color.CONTENT.value,
                #bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.CONTENT.value
                ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "José Montaño", 
                    size="lg",
                    color=ColorT.HEADER.value
                    ),
                rx.chakra.text(
                    "@joymogas",
                    margin_top=Size.ZERO.value,
                    color=ColorT.HEADER.value
                    ),
                rx.chakra.hstack(
                        link_icon(
                            "icons/x-twitter.svg",
                            "https://x.com/DevMogas",
                            "Twitter"
                            
                            ),
                        link_icon(
                            "icons/github.svg",
                            "https://github.com/JoyMoGas",
                            "GitHub"
                            ),
                        link_icon(
                            "icons/tiktok.svg",
                            "https://www.tiktok.com/@joymogas",
                            "TikTok"
                            ),
                        link_icon(
                            "icons/spotify.svg",
                            "https://open.spotify.com/playlist/27GiYRb1jzw38yyYu8tAT6?si=fc860dc82b6b4bc7",
                            "Spotify"
                            ),
                        link_icon(
                            "icons/linkedin-in.svg",
                            "https://www.linkedin.com/in/josé-montaño-gastélum-527426270/",
                            "LinkedIn"
                            ),
                            spacing=Size.LARGE.value,
                    ),
                    
                    align_items="start",
            ),  
            spacing=Size.DEFAULT.value,
            #padding_y=Size.LITLE.value,
        ),
        rx.chakra.flex(
                info_text("+3", " años de experiencia"),
                rx.chakra.spacer(),
                info_text("+3", " proyectos creados"),
                rx.chakra.spacer(),
                info_text("+130", " seguidores"),
                width="100%",
                color= ColorT.BODY.value
        ),
        rx.chakra.text(
                """Como estudiante de Ingeniería en Sistemas de Información,
                me dedico a explorar diversas tecnologías. Mi meta es enfrentar 
                desafíos, aprender constantemente y aportar al campo tecnológico. 
                A través de mi aprendizaje, busco innovar y crear soluciones que 
                impacten positivamente en nuestra sociedad.""",
        font_size=Size.X_MEDIUM.value,
        color= ColorT.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start",
    )
