# SUBLEVEL Local v0.5.0

개인 취미 기록, 자유 게시판, 이미지, 감상실을 한 폴더에 보관하는 로컬 개인 홈페이지입니다.

## DUAL INTERFACE UPDATE

- **LEGACY** — 복고풍 개인 홈페이지 / BBS / CRT / 실제 다이얼업 녹음
- **NEXUS** — 미래형 FUI / DATA ARCHIVE / MEDIA CORE / 미래형 UI 효과음
- 두 인터페이스가 같은 SQLite DB, 이미지, 게시글, 감상 데이터를 공유합니다.
- NEXUS MEDIA CORE는 SOURCE / PLAYBACK / POSITION / DURATION / SUBTITLE / SYNC 같은 실제 플레이어 상태를 HUD로 표시합니다.
- NEXUS HUD는 OFF / MINIMAL / FULL로 전환할 수 있습니다.

## 실행

Windows에서는 기존과 동일하게:

```
run-sublevel.bat
```

브라우저는 `http://localhost:8765/`에서 열립니다. Python 3가 필요합니다.

## 개인 데이터

다음 항목은 GitHub 업데이트 대상이 아닙니다.

```
data/
├─ sublevel.db
└─ images/

backup/
```

따라서 업데이트가 `app/`과 `server.py`를 교체해도 게시글·이미지는 유지됩니다.

## v0.4.1 → v0.5.0 인앱 업데이트

새 ZIP을 다시 받을 필요가 없습니다.

1. 기존 v0.4.1의 `run-sublevel.bat`을 실행합니다.
2. `SYSTEM → UPDATE SYSTEM`으로 이동합니다.
3. OWNER=`9019paul`, REPOSITORY=`Sublevel`인지 확인합니다.
4. 필요하면 `SAVE SOURCE`를 누릅니다.
5. `CHECK UPDATE`를 누릅니다.
6. `CURRENT 0.4.1 / LATEST 0.5.0 / PACKAGE FOUND`를 확인합니다.
7. `DOWNLOAD UPDATE`를 누르고 `RESTART REQUIRED`가 뜰 때까지 기다립니다.
8. 로컬 서버 콘솔을 종료한 뒤 **같은 폴더의 같은 `run-sublevel.bat`**을 다시 실행합니다.
9. `launcher.py`가 다운로드한 업데이트를 적용합니다.

`data/`, `backup/`, 기존 `app/assets/sounds/`의 모뎀 음원은 보존됩니다.

## 업데이트 검증

현재 배포 패키지 SHA-256:

```
98bd9489e5930b4dd9e8c1ddd3f6c788745adf961202e46826d7b832a0b280d0
```

SUBLEVEL은 GitHub의 `main/version.json`에서 최신 버전과 업데이트 조각 목록을 읽고, 다운로드 후 SHA-256이 일치해야 `.update/pending.zip`으로 등록합니다.

문제가 생기면 SYSTEM/CORE의 `ROLLBACK ON RESTART`를 사용할 수 있습니다.

## 최초/복구 설치

인앱 업데이트를 사용할 수 없는 경우에만 전체 설치 ZIP을 사용합니다. 평소 업데이트에서는 전체 설치 ZIP을 다시 내려받을 필요가 없습니다.

## Credits

다이얼업 효과음 정보는 [CREDITS.md](CREDITS.md)를 참고하세요.
