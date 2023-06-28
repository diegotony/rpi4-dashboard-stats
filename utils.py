from reactpy import component, html, run
import system_info as si
def memory_ram():
    memory_ram = si.System_info.get_memory_usage()
    print(memory_ram)
    return html.div(
        html.h3("RAM"),
        
        html.div(
            html.h4("total"),
            html.p(memory_ram["total"])
        ),
        html.div(
            html.h4("used"),
            html.p(memory_ram["used"])
        ),
        html.div(
            html.h4("available"),
            html.p(memory_ram["available"])
        )
    )


def get_cpu():
    cpu = si.System_info.get_cpu()
    print(cpu)
    return html.div(
        html.h3("CPU"),
        html.div(
            html.h4("cpu_usage"),
            html.p(cpu["cpu_usage"])
        ),
        html.div(
            html.h4("cpu_percent"),
            html.p(cpu["cpu_percent"])
        ),
        html.div(
            html.h4("cpu_count"),
            html.p(cpu["cpu_count"])
        )
    )
