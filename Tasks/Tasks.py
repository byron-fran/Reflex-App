
from rxconfig import config
from .pages import form
import reflex as rx



class State(rx.State):
    """The app state."""

    pass




@rx.page(route='form')
def form_page():
    return form.form()

@rx.page()
def about():
    return rx.text("About Reflex!")

@rx.page(route='/pagina')
def pagina():
    return rx.container(
        rx.text('Pagina'),
        rx.link(
            'form',
            href='/form',
            color='#4f45e1'
        )
    )



def qa(question : str, answe : str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align='right'),
        rx.box(answe, text_align='left'),
        margin_y='1em'
    )



def chat() -> rx.Component:
    qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What is Reflex?", "A way to build web apps in pure Python!"),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for(question, answer) in qa_pairs
        ]
    )

def index() -> rx.Component:
    return rx.container(chat())


# Add state and page to the app.
app = rx.App()
app.add_page(index)

