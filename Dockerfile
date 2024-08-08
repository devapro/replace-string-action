FROM python:3.12-slim@sha256:a3e58f9399353be051735f09be0316bfdeab571a5c6a24fd78b92df85bcb2d85

WORKDIR /action/workspace
COPY requirements.txt *.py /action/workspace/

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["/action/workspace/replace_string.py"]
ENTRYPOINT ["python3"]