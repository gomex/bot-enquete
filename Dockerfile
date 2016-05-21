FROM python
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD ./ /app
WORKDIR /app
CMD ["python","vota-selenium.py"]
