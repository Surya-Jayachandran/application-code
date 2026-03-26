# Application Code

FastAPI + Docker DevOps Project

## Run locally
uvicorn main:app --reload

## Docker
docker build -t fastapi-app .
docker run -d -p 80:80 fastapi-app