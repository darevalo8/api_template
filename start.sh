#!/bin/sh

# Ejecuta el primer entrypoint
sh entrypoint.sh &

# Ejecuta el segundo entrypoint
#sh entrypoint_celery.sh &

# Espera a que ambos procesos terminen
wait
