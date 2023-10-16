# Dockerizing an app

## Usefull docker compose commands:

```sh
docker compose up # starts the container
docker compose up -d # starts the container in the daemon (background) mode
docker compose ls # Image names, status and origin file
docker compose exec api bash # Like using ssh, executes bash inside the running container
docker compose run api bash # Starts the contianer, and run the command inside
```