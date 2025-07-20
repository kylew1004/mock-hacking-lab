# 1) Svelte 빌드
FROM node:20-slim AS builder
WORKDIR /app

COPY frontend ./frontend
WORKDIR /app/frontend

# lock 파일이 없으므로 npm install 사용
RUN npm install && npm run build

# 2) nginx 이미지
FROM nginx:alpine
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/frontend/dist /usr/share/nginx/html
