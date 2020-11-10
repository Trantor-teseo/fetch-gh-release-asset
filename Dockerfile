FROM alpine:latest

RUN	apk add --no-cache \
  bash \
  ca-certificates \
  curl \
  wget \
  jq \
  python3 \
  py3-pip

COPY get_release.py /get_release.py

ENTRYPOINT ["python3 get_release.py"]
