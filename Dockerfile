FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run app.py --server.address 0.0.0.0 --server.port $PORT