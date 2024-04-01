FROM ubuntu:20.04

ENV BUILDKIT_STEP_LOG_MAX_SIZE=10000000
ENV BUILDKIT_STEP_LOG_MAX_SPEED=10000000

ENV OPEN_CV_VERSION=4.5.5
ENV MAKE_THREADS=12
ENV APP_DIR=/monitorauff/app/client

ENV DEBIAN_FRONTEND=noninteractive

# Atualização do sistema
RUN apt update

# Instalação do Python e dependências python
RUN apt install -y --no-install-recommends \
	python3 python3-pip python3-dev python3-opencv python3-numpy python3-psycopg2 && \
	pip3 install --upgrade pip

# Instalação de dependências de construção e de biblitecas
RUN apt install -y --no-install-recommends \
	cmake gcc g++ wget git ffmpeg build-essential unzip pkg-config gfortran ca-certificates \
	libavcodec-dev libavformat-dev libswscale-dev \
	libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev \
	libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev \
	libv4l-dev libxvidcore-dev libx264-dev libatlas-base-dev openexr \
	libtbb2 libtbb-dev libdc1394-22-dev

# Efetuando algumas limpezas
RUN apt clean autoclean && \
	apt autoremove --yes && \
	rm -rf /var/lib/{apt,dpkg,cache,log}/

# Download, instalação e configuração do OpenCV
RUN cd ~ && \
	wget -O opencv.zip https://github.com/opencv/opencv/archive/${OPEN_CV_VERSION}.zip && \
	unzip opencv.zip && \
	rm opencv.zip && \
	mv opencv-${OPEN_CV_VERSION} opencv && \
	wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${OPEN_CV_VERSION}.zip && \
	unzip opencv_contrib.zip && \
	rm opencv_contrib.zip && \
	mv opencv_contrib-${OPEN_CV_VERSION} opencv_contrib

RUN	cd ~/opencv && \
	mkdir build && \
	cd build && \
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
		-D INSTALL_PYTHON_EXAMPLES=OFF \
		-D INSTALL_C_EXAMPLES=OFF \
		-D OPENCV_ENABLE_NONFREE=ON \
		-D WITH_CUDA=ON \
		-D WITH_CUDNN=ON \
		-D OPENCV_DNN_CUDA=OFF \
		-D ENABLE_FAST_MATH=0 \
		-D CUDA_FAST_MATH=0 \
		-D WITH_CUBLAS=0 \
		-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
		-D HAVE_opencv_python3=ON \
		-D PYTHON_EXECUTABLE=$(which python3) \
		-D BUILD_EXAMPLES=OFF \
		-D BUILD_OPENCV_JAVA=OFF \
		-D BUILD_TESTS=OFF \
		-D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
		-D PYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")  \
		-D PYTHON_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")  \
		../ && \
	make -j${MAKE_THREADS} && \
	make install && \
	ldconfig && \
	rm -rf ~/opencv && \
	rm -rf ~/opencv_contrib && \
	mkdir -p ${APP_DIR} && \
	chmod 777 ${APP_DIR}

# Instalação do Tesseract
# TODO: Colocar comando no início do Dockerfile
ENV TESSERACT_VERSION=5.0.1

RUN cd ~ && \
	apt install -y automake libtool libleptonica-dev make \
	libicu-dev libpango1.0-dev libcairo2-dev && \
	wget -O tesseract.zip https://github.com/tesseract-ocr/tesseract/archive/${TESSERACT_VERSION}.zip && \
	unzip tesseract.zip && \
	rm tesseract.zip && \
	mv tesseract-${TESSERACT_VERSION} tesseract && \
	cd ~/tesseract && \
	./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig && \
    make training && \
    make training-install && \
	rm -rf ~/tesseract

RUN cd /usr/local/share/tessdata && \
	wget https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata && \
	wget https://github.com/tesseract-ocr/tessdata/blob/master/por.traineddata && \
	wget https://github.com/tesseract-ocr/tessdata/blob/master/osd.traineddata && \
	export TESSDATA_PREFIX=/usr/local/share/tessdata

# Instalação do OpenALPR

RUN cd ~/ && \
	apt install -y libopencv-dev libtesseract-dev \
	liblog4cplus-dev libcurl3-dev beanstalkd && \
	git clone https://github.com/openalpr/openalpr.git && \
	cd ~/openalpr/src && \
	mkdir build && \
	cd build && \
	cmake -D CMAKE_INSTALL_PREFIX:PATH=/usr \
		-D CMAKE_INSTALL_SYSCONFDIR:PATH=/etc \
		# Está dando erro
		# -D WITH_GPU_DETECTOR=ON \
		../ && \
	make && \
	make install && \
	cd ~/openalpr/src/bindings/python && \
	python3 setup.py install && \
	rm -rf ~/openalpr

# Instalação OpenSSH-Server
RUN apt install -y openssh-server

## MonitoraUFF

WORKDIR ${APP_DIR}

COPY requirements.txt ./

RUN pip3 install -r ./requirements.txt

COPY . ./

#RUN mv .ssh ~ \
#	&& touch ~/.ssh/authorized_keys \
#	&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
#	&& rm ~/.ssh/id_rsa.pub ~/.ssh/id_rsa

EXPOSE 22

ENTRYPOINT ["/bin/bash", "./start.sh"]
