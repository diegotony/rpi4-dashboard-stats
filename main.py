from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
import utils as util

@component
def HomePage():
    # return html.h1("Hello, world!")
    return html.div(
        util.memory_ram(),
        util.get_cpu()
    )




app = FastAPI()
configure(app, HomePage)