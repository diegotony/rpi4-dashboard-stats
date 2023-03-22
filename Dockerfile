FROM python:slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD [  "gunicorn", "-w"," 4", "--bind" ,"0.0.0.0:8000","--access-logfile","-", "app:app" ]
