FROM python:3.11

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y libgl1 python3-tk

RUN pip install numpy pandas scikit-learn opencv-python matplotlib scipy

CMD ["python", "distance_classification.py"]
