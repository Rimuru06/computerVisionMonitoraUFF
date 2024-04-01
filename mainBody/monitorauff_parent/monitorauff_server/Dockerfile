FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV APP_DIR=/usr/src/monitorauff/server

WORKDIR ${APP_DIR}

# Atualização do sistema
RUN apt update \
	&& apt upgrade -y

# Instalação do Python e dependências python
RUN apt install -y --no-install-recommends python3 \
	&& apt install -y python3-pip python3-venv \
	&& pip3 install --upgrade pip \
	&& python3 -m pip install opencv-python \
	&& python3 -m pip install --upgrade pip

# Instalação do Redis
RUN apt install redis -y

COPY requirements.txt ./

RUN pip3 install -r ./requirements.txt

COPY . ./

EXPOSE 8000
EXPOSE 6379

CMD ["tail", "-f", "/dev/null"]