# start with a base image
FROM python:3.9

# update working directories
ADD . .
WORKDIR .

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install keras pillow numpy streamlit
RUN python -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl

EXPOSE 8501
CMD ["streamlit","run" ,"main.py"]