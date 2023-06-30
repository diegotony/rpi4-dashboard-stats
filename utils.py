# from reactpy import component, html, run
# import system_info as si
# def memory_ram():
#     memory_ram = si.System_info.get_memory_usage()
#     print(memory_ram)
#     return html.p(
#             "Memory RAM",
#             html.br(),
#             "Total: " + str(memory_ram["total"]),
#             html.br(),
#             "Used: " + str(memory_ram["used"]),
#             html.br(),
#             "Available: "+ str(memory_ram["available"])

#     )


# def cpu():
#     cpu = si.System_info.get_cpu()
#     print(cpu)
#     return html.p(
#        "cpu_usage= "+str(int(cpu["cpu_usage"])),
#        " / cpu_percent= "+str(cpu["cpu_percent"]),
#        " / cpu_count= "+str(cpu["cpu_count"])
        
#     )


def head():
    return html.head(
        html.title("Holi"),
        html.meta({"charset":"utf-8"}),
        html.meta({"name":"viewport", "content":"width=device-width, initial-scale=1"}),
        # html.script({"src":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js","integrity":"sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz","crossorigin":"anonymous"}),
        
        # html.script({"src":"https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js","integrity":"sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz","crossorigin":"anonymous"}),


        # html.script({"src":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js","integrity":"sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS","crossorigin":"anonymous"}),
        
        # html.link({"rel": "stylesheet","href":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css", "integrity":"sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM","crossorigin":"anonymous"})

        html.script({"src":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"}),
        
        html.link({"rel": "stylesheet","href":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"})

    )

