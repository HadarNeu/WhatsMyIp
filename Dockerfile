FROM alpine

RUN apk update && \
    apk upgrade --available && \
	apk add --update python3 && \
        apk add curl && \
	apk add py3-pip

WORKDIR /ipapp

ENV PORT 80

RUN pip install --upgrade pip && \
	pip install Flask
	
COPY . /ipapp

ENTRYPOINT ["python3"]

CMD ["ipApp.py"]

