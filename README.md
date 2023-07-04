# rpi4-dashboard-stats
API REST to Get stats with psutil
## Run

```bash
make install
source env/bin/activate
uvicorn main:app --reload
```

## Output
```json
{
"cpu": {
"percent": 0.0,
"cpu_count": 12,
"cpu_freq": {
"current": 4199.898,
"min": 0.0,
"max": 0.0
},
"cpu_usage": 3.25
},
"ram": {
"total": 11,
"used": 3,
"available": 8
},
"storage": {
"/mnt/wsl": {
"total": 5,
"used": 0,
"free": 5
},
"/usr/lib/wsl/drivers": {
"total": 930,
"used": 347,
"free": 583
},
"/usr/lib/wsl/lib": {
"total": 5,
"used": 0,
"free": 5
},
"/": {
"total": 250,
"used": 32,
"free": 205
},
"/sys/fs/cgroup/blkio": {
"total": 0,
"used": 0,
"free": 0
},
"/sys/fs/cgroup/memory": {
"total": 0,
"used": 0,
"free": 0
},
"/mnt/wslg/versions.txt": {
"total": 5,
"used": 0,
"free": 5
},
"/mnt/c": {
"total": 930,
"used": 347,
"free": 583
},
"/mnt/d": {
"total": 931,
"used": 510,
"free": 420
},
"/Docker/host": {
"total": 930,
"used": 347,
"free": 583
}
}
}
```