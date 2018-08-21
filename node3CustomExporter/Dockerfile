FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "simpleRestExporter.py"]
EXPOSE 9100