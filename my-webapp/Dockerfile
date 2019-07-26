FROM python:3.6

RUN pip install bottle

ADD my_webapp.py /my_webapp.py
ADD my_domain.py /my_domain.py

EXPOSE 8000
CMD ["python", "/my_webapp.py"]