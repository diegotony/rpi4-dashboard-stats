from flask import Flask
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


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
