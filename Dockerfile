FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /brain-games/

WORKDIR /brain-games

RUN apt-get update && apt-get install make

RUN make install

RUN make build

RUN make docker-package-install

CMD ["bash"]
