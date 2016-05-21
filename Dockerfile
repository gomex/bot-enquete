FROM python
ADD requirements.txt requirements.txt
pip install -r requirements.txt
ADD ./ /app
WORKDIR /app
CMD ["python","vota-selenium.py"]
