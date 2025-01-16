FROM python:3.12.8-slim-bullseye

ARG UID=1000
ARG GID=1000
ENV TZ Asia/Tokyo

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends \
  software-properties-common \
  curl 
rm -rf /var/lib/apt/lists/*

curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 - 
ln -s /etc/poetry/bin/poetry /usr/local/bin/poetry
EOF

COPY --chmod=700 ./entrypoint.sh /

WORKDIR /app
COPY --chmod=700 . /app
ENV USER tech
ENV GROUP tech
RUN groupadd tech && \ 
  useradd -u 1000 -m -d /home/${USER} -g ${GROUP} ${USER} && \
  chown -R ${USER}:${GROUP} /home/${USER} && \
  chown -R ${USER}:${GROUP} /app && \
  chown ${USER}:${GROUP} /entrypoint.sh

USER ${USER}

RUN <<EOF
poetry config virtualenvs.in-project true
poetry config virtualenvs.create true
EOF

ENTRYPOINT [ "/entrypoint.sh" ]
