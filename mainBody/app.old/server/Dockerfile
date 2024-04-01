FROM zoneminderhq/zoneminder:latest-ubuntu18.04

ENV LANGUAGE="UTF-8" LANG="UTF-8" LC_ALL="UTF-8" LC_CTYPE="UTF-8"

WORKDIR /usr/src/monitorauff/app/server

# Atualizações
RUN apt-get update && apt-get upgrade -y && apt-get install -y

# Instalação do Python e pacotes
RUN apt install python3.10 -y \
	&& apt install python3-pip -y \
	&& pip3 install --upgrade pip

# Instalação do Redis
RUN apt install redis -y

COPY requirements.txt ./

RUN pip3 install -r ./requirements.txt

COPY . ./

EXPOSE 22 
EXPOSE 80
EXPOSE 8000
EXPOSE 6379