FROM ubuntu:18.04

########## ROOT WORKS ##########
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
RUN apt-get install -y libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libmysqlclient-dev
RUN apt-get install -y git curl g++ make openssh-server vim build-essential
RUN apt-get install -y libmagic-mgc libmagic1 libmpdec2 libpython3-dev libpython3-stdlib libpython3.6 libpython3.6-dev libpython3.6-minimal libpython3.6-stdlib mime-support python3 python3-distutils python3-lib2to3 python3-minimal python3.6 python3.6-dev python3.6-minimal xz-utils
RUN apt-get install -y python python-dev
RUN apt-get install -y language-pack-ja-base language-pack-ja
RUN apt-get install -y sl
RUN locale-gen ja_JP.UTF-8

# local dir mount
RUN mkdir -p /share
ADD ./ /share
ADD frontend /share/frontend
WORKDIR /share

# python tools install
RUN python3 ./tools/get-pip.py
RUN pip install -r ./tools/requirements.txt

# vue tools install
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v12.14.0
RUN mkdir -p $NVM_DIR

RUN git clone http://github.com/creationix/nvm.git $NVM_DIR
RUN chmod -R 777 $NVM_DIR
RUN bash $NVM_DIR/install.sh
RUN bash -i -c "nvm install $NODE_VERSION"
RUN bash -i -c "nvm alias default $NODE_VERSION"
RUN bash -i -c "nvm use default"
RUN bash -i -c "npm install -g npm"

# setting port
EXPOSE 3000
EXPOSE 3306
EXPOSE 8080

# make data
WORKDIR /share/

