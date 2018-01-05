FROM hypriot/rpi-alpine
MAINTAINER zepptron <https://github.com/zepptron>

COPY main.py /main.py
RUN apk update && \
    apk add --no-cache python

ENTRYPOINT [ "/usr/bin/python /main.py" ]