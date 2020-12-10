FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libuv1.dev \
    python3 \
    python3-pip \
    vim \
    zsh \
    net-tools \
    iputils-ping \
    build-essential \
    wget \
    gdb \
    netcat \
    git \
    unzip \
    gcc-multilib \
    ruby \
    ruby-bundler \
    ruby-dev \
    gcc \
    g++ \
    bsdmainutils \
    patchelf

RUN wget https://github.com/radareorg/radare2/releases/download/4.4.0/radare2_4.4.0_amd64.deb && \
    dpkg -i radare2_4.4.0_amd64.deb && rm radare2_4.4.0_amd64.deb

RUN wget https://github.com/downloads/0vercl0k/rp/rp-lin-x86 -O /usr/local/bin/rp-lin-x86
RUN wget https://github.com/downloads/0vercl0k/rp/rp-lin-x64 -O /usr/local/bin/rp-lin-x64
RUN chmod +x /usr/local/bin/rp-lin-x86 /usr/local/bin/rp-lin-x64

RUN python3 -m pip install -U pip && \
    python3 -m pip install --no-cache-dir \
    pwntools

RUN gem install one_gadget

RUN git clone https://github.com/longld/peda.git ~/peda
RUN echo "source ~/peda/peda.py" >> ~/.gdbinit
RUN echo "pset option autosave 'off'" >> ~/.gdbinit

RUN git clone https://github.com/rupa/z.git ~/z

RUN git clone https://github.com/david942j/one_gadget.git ~/one_gadget
RUN rm ~/one_gadget/Gemfile.lock

WORKDIR /ctf/work/

ADD ./vimrc /root/.vimrc
ADD ./bashrc /root/bashrc

RUN cat /root/bashrc >> /root/.bashrc

RUN echo 'set completion-ignore-case on' >> /etc/inputrc

ENV LANG "C.UTF-8"

