import psutil
import os

class System_info:
    def get_memory_total():
        memory = psutil.virtual_memory()
        return {"total": memory.total, "active": memory.active, "inactive": memory.inactive, "cached": memory.cached, "shared": memory.shared, "used": memory.used, "free": memory.free, "available": memory.available, "percent": memory.percent,"buffers": memory.buffers}  

    def get_memory_usage():
        memory = psutil.virtual_memory()
        response = {"total": memory.total >> 30,"used": memory.used >> 30, "available": memory.available >> 30}  
        return response


    def get_swap_memory():
        swap_memory = psutil.swap_memory()
        return {"total": swap_memory.total >> 30,"used": swap_memory.used >> 30, "free": swap_memory.free >> 30}  

    def get_disk_usage():
        partitions  = psutil.disk_partitions(all=True)
        partitions_dict = {}
        for part in partitions:
            usage = psutil.disk_usage(part.mountpoint)
            partitions_dict[part.mountpoint] = {"total":usage.total >> 30, "used":usage.used >> 30, "free":usage.free >> 30}
        return partitions_dict

    def get_cpu():
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15/os.cpu_count()) * 100

        return {"cpu_percent": psutil.cpu_percent(5), "cpu_count": psutil.cpu_count(), "cpu_freq": {"current":psutil.cpu_freq().current,"min":psutil.cpu_freq().min,"max":psutil.cpu_freq().max}, "cpu_usage": cpu_usage}  

    def get_cpu_usage():
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15/os.cpu_count()) * 100
        percent = psutil.Process(os.getpid())

        return {"percent": psutil.cpu_percent(0), "cpu_count": psutil.cpu_count(), "cpu_freq": {"current":psutil.cpu_freq().current,"min":psutil.cpu_freq().min,"max":psutil.cpu_freq().max}, "cpu_usage": cpu_usage}  

    def get_info():
        return {"IS_LINUX":psutil.LINUX}

    def get_temp():
        return {"sensor_temperatures":psutil.sensors_temperatures(fahrenheit=False),  'sensor_fans': psutil.sensors_fans()}