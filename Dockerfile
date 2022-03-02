FROM node:13-alpine

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PASSWORD=password
    
RUN mkdir /home/devopsnode/

COPY ./devopsnode /home/devopsnode/

CMD ["node", "/home/devopsnode/server.js"]
