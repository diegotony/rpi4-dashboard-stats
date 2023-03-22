docker_compose("./docker-compose.yml")
docker_build("rpi4-dashboard", context=".",dockerfile="Dockerfile",live_update=[sync("app.py", "/app/app.py"),sync("templates/", "/app/templates/")])
