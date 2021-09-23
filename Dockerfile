FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    wget \
    curl \
    python3-dev \
    nginx \
    ca-certificates \
    libgomp1 \
    gcc \
    unzip \
    && rm -rf /var/lib/apt/lists/* \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/local/bin/pip pip /usr/local/bin/pip3 1

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

RUN pip3 install -i https://pypi.doubanio.com/simple boto3 numpy scipy scikit-learn pandas flask gevent gunicorn lightgbm

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/app:${PATH}"



COPY docker_code /app
WORKDIR /app
RUN chmod +x cmd.sh
