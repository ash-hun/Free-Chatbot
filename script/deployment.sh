cd environments/ && docker compose down --rmi all
cd ../ && docker build -t free_chatbot:latest -f environments/Dockerfile .
cd environments/ && docker compose up
