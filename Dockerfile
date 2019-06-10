FROM python:3.7

WORKDIR /opt/link_shortener

COPY Pipfile Pipfile.lock ./
RUN pip3 install pipenv && pipenv install --deploy

COPY . .

EXPOSE 5000

ENTRYPOINT ["pipenv", "run"]
CMD ["web"]
