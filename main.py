from fastapi import FastAPI
import system_info as si

app = FastAPI()


@app.get("/")
async def root():
    return {"cpu":  si.System_info.get_cpu_usage(), "ram": si.System_info.get_memory_usage(), "storage": si.System_info.get_disk_usage()}


