# SUBLEVEL Local v0.4.1

개인 취미 기록, 자유 게시판, 이미지, 감상실을 한 폴더에 보관하는 로컬 개인 홈페이지입니다.

## v0.4.1

- 일본어 UI 문구 제거
- 합성 발신음 / DTMF / 링백 / 합성 핸드셰이크 제거
- 설치본에 포함된 실제 다이얼업 MP3를 접속 시 처음부터 끝까지 재생
- 게시판/게시글: SQLite (`data/sublevel.db`)
- 첨부 이미지: `data/images/`
- 로컬 영상 + YouTube THEATER
- 로컬 자막 및 CRT/VCR 오버레이
- 백업/복원
- GitHub 기반 인앱 업데이트

## 실행

Windows에서는 최초 설치 ZIP을 푼 뒤:

```
run-sublevel.bat
```

브라우저에서 `http://localhost:8765/`가 열립니다. Python 3가 필요하며 별도 Python 패키지는 사용하지 않습니다.

## 개인 데이터

다음 경로는 GitHub 업데이트 대상이 아니며 PC에만 남습니다.

```
data/
├─ sublevel.db
└─ images/

backup/
```

`.gitignore`에서도 해당 경로를 제외합니다.

## 자동 업데이트

SUBLEVEL은 다음 파일을 확인합니다.

```
https://raw.githubusercontent.com/9019paul/Sublevel/main/version.json
```

새 버전이 있으면 SYSTEM의 `CHECK UPDATE → DOWNLOAD UPDATE`로 업데이트 ZIP을 내려받고, 다음 실행 시 `launcher.py`가 `app/`과 `server.py`를 교체합니다.

업데이트 ZIP은 SHA-256을 검증합니다. 적용 전 기존 앱은 `.update/`에 보관되어 롤백할 수 있습니다.

### 모뎀 음원 보존

실제 모뎀 MP3는 최초 설치본에 포함됩니다. 이후 GitHub 업데이트 패키지는 음원을 다시 포함하지 않으며, `launcher.py`가 기존 `app/assets/sounds/` 폴더를 보존합니다. 따라서 작은 코드 패치마다 같은 음원을 다시 내려받지 않습니다.

## 저장소와 설치본의 차이

이 저장소는 업데이트 메타데이터와 배포 패키지의 기준점입니다. 개인 게시글·사진·SQLite DB는 저장소로 전송되지 않습니다.

## Credits

다이얼업 효과음 정보는 [CREDITS.md](CREDITS.md)를 참고하세요.
