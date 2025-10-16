# POGAS

## 프로젝트 개요
- Playwright 브라우저 제어 기반 여론 분석 시스템(Public Opinion Gathering Analysis System)

## 설치 및 실행
```powershell
# 레포지토리 연결
git clone https://github.com/dev-yoonho/POGAS.git
cd POGAS
```
```powershell
# 가상환경 생성 및 구동
python -m venv .venv
.\.venv\Scripts\activate
```
```powershell
# 필요 패키지 설치
pip install -r requirements.txt
playwright install
playwright install --force chrome
```
```.env
# 루트 폴더에 .env 파일 생성 후 아래 양식대로 입력
CLIENT_ID = INSERT_YOUR_API_ID
CLIENT_SECRET = INSERT_YOUR_API_SECRET
```
```powershell
python main.py
```
