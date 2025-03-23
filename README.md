# Django Performance Lab

이 프로젝트는 Django의 성능을 연구하고, 동기(Sync)와 비동기(Async) 처리 방식의 성능 차이를 비교하기 위한 실험을 수행하는 실험실(Lab)입니다. Docker를 사용하여 개발 환경을 구성하였으며, 다양한 테스트를 통해 성능을 측정하고 분석합니다.

## 프로젝트 구조

- `./lab/SyncAsyncLab/sync`: 동기(Sync) 방식의 성능 실험을 위한 폴더입니다.
- `./lab/SyncAsyncLab/async`: 비동기(Async) 방식의 성능 실험을 위한 폴더입니다.

## 실행 방법

1. **Docker 환경 설정**  
   프로젝트의 루트 디렉토리에서 다음 명령어로 Docker 컨테이너를 빌드하고 실행합니다.

   ```bash
   docker-compose up --build
