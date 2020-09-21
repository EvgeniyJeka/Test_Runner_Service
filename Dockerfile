FROM python

WORKDIR var/www/html

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "pytest", "-v", "test_sanity.py::TestSanity"]