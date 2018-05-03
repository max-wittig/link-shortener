FROM python:3

WORKDIR /opt/link_shortener
RUN useradd -ms /bin/sh link_shortener
RUN python3 -m venv venv
RUN chown -R link_shortener:link_shortener venv/

COPY requirements.txt .
RUN venv/bin/pip install --require-hashes -r requirements.txt

COPY . .
RUN chown -R link_shortener:link_shortener .

USER link_shortener
EXPOSE 5000
ENTRYPOINT ["venv/bin/python3", "__main__.py"]
