FROM hypriot/rpi-alpine
MAINTAINER zepptron <https://github.com/zepptron>

COPY main.py /main.py
RUN apk update && \
    apk add ca-certificates && \
    apk add --no-cache python

CMD python main.py