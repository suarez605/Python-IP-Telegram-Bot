FROM python:3.10-alpine

ADD ./main.py /
ADD ./requirements.txt /

RUN pip install -r ./requirements.txt

CMD ["python3", "main.py"]