from flask import Flask, render_template, redirect, url_for
from flask_restful import Resource, Api
import psutil

app = Flask(__name__)
api = Api(app)


class PiData(Resource):
    def get(self):
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        system_info_data = {
            'cpu_percent': psutil.cpu_percent(1),
            'cpu_count': psutil.cpu_count(),
            'cpu_freq': psutil.cpu_freq(),
            'cpu_mem_total': memory.total,
            'cpu_mem_avail': memory.available,
            'cpu_mem_used': memory.used,
            'cpu_mem_free': memory.free,
            'disk_usage_total': disk.total,
            'disk_usage_used': disk.used,
            'disk_usage_free': disk.free,
            'disk_usage_percent': disk.percent,
            'sensor_temperatures': psutil.sensors_temperatures(),
            'sensor_fans': psutil.sensors_fans()

        }

        return system_info_data

api.add_resource(PiData, "/get-stats")

@app.route("/")
def home():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    widget_ids = ["widget1", "widget2", "widget3"]
    system_info_data = {
        'cpu_percent': str(psutil.cpu_percent(1)),
        'cpu_count': str(psutil.cpu_count()),
        'cpu_freq': str(psutil.cpu_freq()),
        'cpu_mem_total': str(memory.total),
        'cpu_mem_avail': str(memory.available),
        'cpu_mem_used': str(memory.used),
        'cpu_mem_free': str(memory.free),
        'disk_usage_total': str(disk.total),
        'disk_usage_used': str(disk.used),
        'disk_usage_free': str(disk.free),
        'disk_usage_percent': str(disk.percent),
        'sensor_temperatures': str(psutil.sensors_temperatures()),
        'sensor_fans': str(psutil.sensors_fans()
        )
    }
    return render_template("index.html", 
                           title="rpi-stats", 
                           data=system_info_data,
                           test=str(psutil.cpu_percent(1)),
                           disk_usage=psutil.disk_usage('/'),
                           cpu_percent=str(psutil.cpu_percent(1)),
                           cpu_num_logic=str(psutil.cpu_count()),
                           cpu_num_no_logical=str(psutil.cpu_count(logical=False)),
                           cpu_mem_total= str(memory.total),
                           cpu_mem_avail= str(memory.available),
                           cpu_mem_used=str(memory.used),
                           cpu_mem_free= str(memory.free),
                           widget_ids=widget_ids
                        #    data=system_info_data,
                        #    data=system_info_data,
                        #    data=system_info_data,
                        #    data=system_info_data,
                        #    data=system_info_data,
                        #    data=system_info_data,           
                           )


if __name__ == '__main__':
    app.run(debug=True)
