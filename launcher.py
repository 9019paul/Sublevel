from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
UPD = ROOT / '.update'
PENDING = UPD / 'pending.zip'
ROLLBACK = UPD / 'rollback.flag'
PREV_APP = UPD / 'previous_app'
PREV_SERVER = UPD / 'server.py.prev'

UPD.mkdir(exist_ok=True)


def apply_pending():
    if not PENDING.is_file():
        return
    print('[SUBLEVEL] Applying pending update...')
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        with zipfile.ZipFile(PENDING) as z:
            for info in z.infolist():
                p = Path(info.filename)
                if p.is_absolute() or '..' in p.parts:
                    raise RuntimeError('Unsafe update path')
            z.extractall(t)
        manifest = t / 'manifest.json'
        app_new = t / 'app'
        if not manifest.is_file() or not app_new.is_dir():
            raise RuntimeError('Invalid SUBLEVEL update package')
        meta = json.loads(manifest.read_text(encoding='utf-8'))
        if PREV_APP.exists():
            shutil.rmtree(PREV_APP)
        preserved_sounds = None
        current_sounds = ROOT / 'app' / 'assets' / 'sounds'
        if current_sounds.is_dir():
            preserved_sounds = t / '_preserved_sounds'
            shutil.copytree(current_sounds, preserved_sounds)
        if (ROOT / 'app').exists():
            shutil.copytree(ROOT / 'app', PREV_APP)
        if (ROOT / 'server.py').is_file():
            shutil.copy2(ROOT / 'server.py', PREV_SERVER)
        shutil.rmtree(ROOT / 'app', ignore_errors=True)
        shutil.copytree(app_new, ROOT / 'app')
        # User/local sound assets are not required in GitHub update packages.
        # Preserve them across app/ replacement when the package omits them.
        target_sounds = ROOT / 'app' / 'assets' / 'sounds'
        if preserved_sounds and not target_sounds.exists():
            target_sounds.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(preserved_sounds, target_sounds)
        if (t / 'server.py').is_file():
            shutil.copy2(t / 'server.py', ROOT / 'server.py')
        PENDING.unlink(missing_ok=True)
        (UPD / 'last_update.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print('[SUBLEVEL] Update applied.')


def apply_rollback():
    if not ROLLBACK.exists():
        return
    print('[SUBLEVEL] Rolling back...')
    if not PREV_APP.is_dir():
        print('[SUBLEVEL] No previous app backup found.')
        ROLLBACK.unlink(missing_ok=True)
        return
    current = UPD / 'rollback_current_app'
    shutil.rmtree(current, ignore_errors=True)
    if (ROOT / 'app').exists():
        shutil.copytree(ROOT / 'app', current)
    shutil.rmtree(ROOT / 'app', ignore_errors=True)
    shutil.copytree(PREV_APP, ROOT / 'app')
    if PREV_SERVER.is_file():
        shutil.copy2(PREV_SERVER, ROOT / 'server.py')
    ROLLBACK.unlink(missing_ok=True)
    print('[SUBLEVEL] Rollback applied.')


if __name__ == '__main__':
    try:
        apply_rollback()
        apply_pending()
    except Exception as e:
        print('[SUBLEVEL] Update error:', e)
        input('Enter를 눌러 기존 버전으로 실행...')
    subprocess.call([sys.executable, str(ROOT / 'server.py')], cwd=str(ROOT))
