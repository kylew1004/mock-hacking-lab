# Mock Hacking Lab 사용법

## 개발 목적

로컬에서 보안 진단 도구와 공격 기법을 자유롭게 실험할 수 있는 테스트 환경 구축

## 아키텍처 구조

```
Frontend : Svelte  (Vite 빌드 → 정적 파일)
Backend  : FastAPI (Uvicorn)
DB       : MySQL
Proxy    : Nginx  (정적 파일 서빙 + /api 프록시)
```

컨테이너는 `docker compose` 하나로 동시에 뜹니다.

---

## 실행 방법

1. **.env 설정**

   ```bash
   cp .env.template .env   # 값(비번·포트) 원하는 대로 수정
   ```

2. **실행**

   ```bash
   docker compose up --build   # 최초 빌드
   # 이후부터는 docker compose up -d 만 해도 됨
   ```

3. **접속**

   - 웹 브라우저 → `http://localhost:<HOST_PORT>`
   - nuclei 등 보안 도구도 같은 URL 사용

4. **중지/정리**

   ```bash
   docker compose down
   ```

---

## 기타

- MySQL 초기 스크립트: `init/01_init.sql` (users 테이블 자동 생성)
- 추가 취약점 실습은 코드 수정 후 다시 `docker compose up --build` 하면 끝
- 이 저장소는 아직 추가 수정 중입니다. 구조나 사용 방법이 예고 없이 바뀔 수 있습니다.
