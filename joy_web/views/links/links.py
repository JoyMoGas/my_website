import reflex as rx
from joy_web.components.link_button import link_button, link__second_button
from joy_web.styles.styles import Size
from joy_web.components.title import title

def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Personal"),
        link_button(
            "Discord",
            "Mi nuevo servidor de Discord para desarrollo",
            "icons/discord.svg",
            "https://discord.com/channels/1206312336751722526/1206312336751722528"
        ),
        link_button(
            "Instagram",
            "Mi perfil personal de Instagram",
            "icons/instagram.svg",
            "https://www.instagram.com/josemogas.5?igsh=MTZjd3hkMTE0cm5qZQ=="
        ),
        link_button(
            "Instagram [professional]",
            "Mi perfil de Instagram dedicado al Desarrollo de Software",
            "icons/instagram.svg",
            "https://www.instagram.com/mogas.dev?igsh=NnRjZHMzazJ3eW0="
        ),
        link_button(
            "Facebook",
            "Mi perfil personal de Facebook",
            "icons/facebook-f.svg",
            "https://www.facebook.com/profile.php?id=100050645148804&mibextid=2JQ9oc"
        ),
        link__second_button(
            "Página Principal",
            "Echa un vistazo a mi página principal",
            "icons/pager-solid.svg",
        ),

        title("Recursos y más"),
        link_button(
            "Documentación REFLEX",
            "Comienza a crear páginas web en Python puro!",
            "icons/book-solid.svg",
            "https://reflex.dev/docs/getting-started/introduction"
        ),
        link__second_button(
            "Mi equipo de trabajo",
            "Algunos de los componentes que uso para mi trabajo",
            "icons/laptop-code-solid.svg",
        ),
        link_button(
            "Aprende gratis!",
            "Contenido educativo de programación de manera gratuita",
            "icons/code-solid.svg",
            "https://www.youtube.com/@mouredev"
        ),
        link__second_button(
            "Regalame un cafecito!",
            "¿Quieres ayudarme a seguir creando?",
            "icons/mug-hot-solid.svg",
        ),

        title("Contacto"),
        link_button(
            "Email",
            "mogas.contacto@gmail.com",
            "icons/envelope-solid.svg", 
            f"mailto:{'mogas.contacto@gmail.com'}"
        ),

        width="100%",
        spacing=Size.MEDIUM.value,
    )