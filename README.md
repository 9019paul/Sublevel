# SUBLEVEL Local v0.5.0

개인 취미 기록과 감상실을 한 폴더에 보관하는 로컬 개인 홈페이지입니다.

## v0.5 — Dual Interface Update

- **LEGACY**: 개인 홈페이지 / BBS / 다이얼업 모뎀 / CRT 감상실
- **NEXUS**: 미래형 데이터 코어 / HUD / 합성 시스템 사운드 / MEDIA CORE
- 두 인터페이스는 같은 SQLite DB, 이미지, 게시판, THEATER 데이터를 공유합니다.
- 상단 **LEGACY / NEXUS** 버튼 또는 SYSTEM > INTERFACE CORE에서 즉시 전환할 수 있습니다.
- NEXUS MEDIA CORE는 Local Video / YouTube / Local Subtitle 기능을 그대로 사용하면서 실제 재생 상태를 HUD 텔레메트리에 표시합니다.

## 실행

Windows에서는 `run-sublevel.bat`을 실행합니다. Python 3 외 별도 패키지는 필요하지 않습니다.

## 개인 데이터

다음 데이터는 GitHub 업데이트 대상이 아닙니다.

```
data/
├─ sublevel.db
└─ images/

backup/
```

## 자동 업데이트

SYSTEM → UPDATE SYSTEM → **CHECK UPDATE** → **DOWNLOAD UPDATE**를 누릅니다.

다운로드가 끝나면 브라우저와 SUBLEVEL 서버 창을 닫고 기존 폴더의 `run-sublevel.bat`을 다시 실행합니다. `launcher.py`가 새 `app/`과 `server.py`를 적용하고 `data/`는 그대로 유지합니다.

업데이트 패키지는 SHA-256으로 검증하며, 적용 전 기존 앱은 `.update/previous_app`에 보관되어 롤백할 수 있습니다.

## GitHub update manifest

`version.json`이 현재 버전과 업데이트 ZIP의 SHA-256을 제공합니다. 공개 저장소의 raw 파일을 사용하므로 별도 GitHub 로그인이나 토큰이 필요하지 않습니다.
