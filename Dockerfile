FROM nginx
WORKDIR /app

RUN apt update -y && apt install -y python3 && apt install -y pip
RUN pip install python-nginx 
CMD [ "/bin/bash"]
