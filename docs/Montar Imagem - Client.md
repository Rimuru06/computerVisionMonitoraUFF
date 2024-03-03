# Como montar a imagem do container

1. Executar os comandos:

    1. `docker run -i -d --name ubuntu ubuntu:18.04`;
    2. Entrar no bash do Ubuntu usando `docker exec -it <CONTAINER_ID> bash`
    3. `apt update && apt upgrade -y && apt install -y` para atualizações
    4. `apt install -y wget` para instalar o wget (precisaremos dele mais tarde)
    5. `apt install libopencv-dev python3-opencv -y` para instalar o OpenCV. Esse comando possui interações.  
        1. `python3 -c "import cv2; print(cv2.__version__)"` para verificar a versão.

        _FONTE: https://vitux.com/opencv_ubuntu/_

    6. `apt install -y tesseract-ocr tesseract-ocr-por`
    7. `apt install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev` para instalar o openalpr.

        Precisaremos testar a intalação, mas antes precisamos copiar o arquivo de treinamento para evitar um erro.

        1. `cd /usr/share/openalpr/runtime_data/ocr/tessdata`  
        2. `cp lus.traineddata ..`
        3. `cd ~/..`
        4. `wget http://plates.openalpr.com/ea7the.jpg`
        5. `alpr -c us ea7the.jpg`
        6. `rm ea7the.jpg`

        _FONTE: https://vitux.com/opencv_ubuntu/_

## Fazer o Build

TODO