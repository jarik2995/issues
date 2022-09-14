FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip3 install flask pyyaml
RUN echo "server1:\n ip: issues-ssh1\nserver2:\n ip: issues-ssh2\n" > /tmp/servers_inventory.yaml
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]
