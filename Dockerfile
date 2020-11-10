FROM alpine:latest

RUN	apk add --no-cache \
  bash \
  ca-certificates \
  curl \
  wget \
  jq \
  python3 \
  py3-pip
RUN pip3 install requests

COPY get_release.py /get_release.py

#ENTRYPOINT ["python /get_release.py"]
CMD ["python3", "/get_release.py"]
#ENTRYPOINT ["python3"]
