# **Como subir o servidor**

Possuindo o docker instalado e o clone do projeto siga os seguintes passos:

## **Passo 01**

Abra o terminal

## **Passo 02**

Navegue até a pasta do projeto e navegue até a pasta 'server'

monitorauff/app/server

## **Passo 03**

Execute o comando

`docker-compose up -d`

Esse passo levantará dois contêineres. O container do banco de dados e o container do servidor que contém o tanto o ZoneMinder quanto o servidor Django do MonitoraUFF.

O Zoneminder é iniciado automaticamente. O servidor Django precisa de mais alguns passos.

## **Passo 04**

Acessar o terminal do contêiner do servidor. Para isso siga os seguintes passos:

- **Passo 4.1**
  
  No seu terminal execute o comando `docker ps` para listar os contêineres execução. Vamos precisar do ID do contêiner do Zoneminder.

- **Passo 4.2**
  
  Execute o comando `docker exec -it <CONTEINER_ID> bash`. Substituindo o <CONTEINER_ID> pelo ID do contêiner desejado, no caso o do Zoneminder. Isso executará o bash do linux do contêiner.

  Uma vez dentro do bash do contêiner, verifique se você se encontra dentro do caminho correto. Algo semelhante a `/usr/src/monitorauff/app/server#`.

## **Passo 05**

Se for a primeira vez rodando o container rode em sequência os comandos a seguir, caso contrário vá para o passo 06.

`python3 manage.py migrate monitor`

`export LC_CTYPE="UTF-8"`

`python3 manage.py createsuperuser`

## **Passo 06**

Execute o comando `python3 manage.py runserver 0.0.0.0:8000` para rodar o servidor de desenvolvimento do Django.

O servidor
