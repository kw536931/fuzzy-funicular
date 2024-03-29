FROM ubuntu:jammy

RUN apt-get update && \
    apt-get -y install git \
        clangd clang-format clang-tidy cmake g++ gdb make \
        python3 python3-pip python3-venv
RUN pip3 install autopep8 build pylint pytest
