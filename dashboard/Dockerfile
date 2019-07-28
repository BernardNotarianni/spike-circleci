FROM python:3.6

RUN pip install bottle
RUN pip install kubernetes

ADD dashboard.py /dashboard.py
ADD dashboard.tpl.html /dashboard.tpl.html
ADD kubeconfig.yml /kubeconfig.yml
ADD gcp-key.json /gcp-key.json

ENV KUBECONFIG /kubeconfig.yml
ENV GOOGLE_APPLICATION_CREDENTIALS /gcp-key.json

EXPOSE 8000
CMD ["python", "/dashboard.py"]