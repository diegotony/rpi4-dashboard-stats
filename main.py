from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
import system_info as si
import utils as util

@component
def HomePage():
    # return html.h1("Hello, world!")
    return html.div(
        html.p("IS LINUX? "+str(si.System_info.get_info()["IS_LINUX"])),
        html.table(
            html.tr(
            html.th("            "),
            html.th("USED"),
            html.th("AVAILABLE"),
            html.th("TOTAL")
            
            ),
            html.tr(
                html.td("MEMORY RAM"),
                html.td(si.System_info.get_memory_usage()["used"]),
                html.td(si.System_info.get_memory_usage()["available"]),
                html.td(si.System_info.get_memory_usage()["total"])
            )
        ),
        html.table(
            html.tr(
            html.th(""),
            html.th("PERCENT"),
            html.th("USAGE"),
            html.th("COUNT"),
            # html.th("MIN")
            
            ),
            html.tr(
                html.td("CPU"),
                html.td(si.System_info.get_cpu_usage()["percent"]),
                html.td(si.System_info.get_cpu_usage()["cpu_usage"]),
                html.td(si.System_info.get_cpu_usage()["cpu_count"]),
                # html.td(si.System_info.get_cpu_usage()["min"])
            ),
        )
    )


app = FastAPI()
configure(app, HomePage)