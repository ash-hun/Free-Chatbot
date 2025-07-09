cd environments/ && docker compose down --rmi all
cd ../ && docker build --platform linux/amd64 -t free_chatbot:latest -f environments/Dockerfile .
cd environments/ && docker compose up
