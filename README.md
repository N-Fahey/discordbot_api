# discordbot_api


```
docker run -d \
  -e "DB_USER=user" \
  -e "DB_PASSWORD=password" \
  -e "DB_HOST=host" \
  -e "DB_PORT=port" \
  -e "DB_NAME=db_name" \
  -p 127.0.0.1:8000:8000 \
  discordbot-api:latest
```

```
docker run -d \
  -e "DB_USER=bot_api_test" \
  -e "DB_PASSWORD=changeme" \
  -e "DB_HOST=203.28.238.188" \
  -e "DB_PORT=3306" \
  -e "DB_NAME=bot_api_test" \
  -h localhost \
  -p 127.0.0.1:8000:8000 \
  discordbot-api:latest
```

uvicorn app:main --log-config log_settings.yaml --log-level info