FROM python:3.11

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y libgl1 python3-tk

RUN pip install numpy pandas scikit-learn opencv-python jupyter nbconvert matplotlib scipy wandb

CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "Lab_5_Spring_2025.ipynb", "--output", "Lab_5_Spring_2025_executed.ipynb"]
