# start with a base image
FROM python:3.9

# update working directories
ADD . .
WORKDIR .

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install keras pillow numpy streamlit
RUN pip3 install tensorflow

EXPOSE 8501
CMD ["streamlit","run" ,"main.py"]