# discordbot_api
API for use with [discordbot](github.com/N-Fahey/discordbot).  
*This bot is built for a specific server and not intended for general use*


### Installation (Docker)
1. Build image:  
  `docker build -t discordbot-api:latest .`
2. Run container:  
    ```
    docker run -d \
      -e "DB_USER=user" \
      -e "DB_PASSWORD=password" \
      -e "DB_HOST=host" \
      -e "DB_PORT=port" \
      -e "DB_NAME=db_name" \
      -p 8000:8000 \
      discordbot-api:latest
    ```

### Installation (Docker Compose)
1. Create docker.env & enter database details  
  `cp docker.env.default docker.env`
1. Build image  
  `docker compose -f docker_compose.yaml build`
2. Launch container  
  `docker compose -f docker_compose.yaml up --detach`

### Installation (Standard)

1. Create venv  
  `python3 -m venv .venv`
2. Activate env  
  `source .venv/bin/activate`
2. Download uv  
  `pip3 install uv`
3. Sync dependancies  
  `uv sync --frozen`
4. Launch using uvicorn  
  `uvicorn app:app --host localhost --port 8000 --log-config log_settings.yaml --log-level info`