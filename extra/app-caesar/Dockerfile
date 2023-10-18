FROM alpine:latest

ENV CRON_SCHEDULE="* * * * *"
ENV LUDUS_ENDPOINT=http://localhost:8081

RUN apk --no-cache add curl

RUN echo "$CRON_SCHEDULE curl -sS -X POST -H 'Content-Type: application/json' $LUDUS_ENDPOINT/duels/resolve/random" >> /var/spool/cron/crontabs/root
RUN chmod 0644 /var/spool/cron/crontabs/root

ENTRYPOINT ["crond", "-f", "-L", "/dev/stdout"]