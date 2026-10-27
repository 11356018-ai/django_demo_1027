# 學生選課與個人課表管理系統

這是一個使用 Django 6.1.2 建立的學生端選課、加課、退選與個人課表管理系統。

## 專案目的

- 讓學生能夠在系統中瀏覽與提出課程（課程需經管理員審核後才能開放選課）
- 支援學生加選、退選課程，維護個人課表
- 透過 Django Admin 進行課程審核與選課紀錄管理
- 簡潔易用，適合課堂練習或小型選課情境

## 技術架構

- **框架**: Django 6.1.2
- **語言**: Python >= 3.14.7
- **資料庫**: SQLite（`db.sqlite3`）
- **套件管理**: uv（含 `pyproject.toml` 與 `uv.lock`）
- **專案模組**: `config/`（設定、路由、WSGI/ASGI）
- **應用程式**: `courses/`（課程提案、選課、個人課表）

## 功能說明

- **課程提案（Course）**: 學生可提出新課程，狀態分為 `pending`（待審核）、`approved`（已核准）、`rejected`（已退回）。管理員可在後台批次審核。
- **選課（Enrollment）**: 學生可對已核准的課程加選／退選（透過 Django Admin 管理）。每位學生對同一門課程僅能選課一次（`unique_together` 限制）。
- **個人課表**: 透過選課紀錄即可檢視個人課表。

## 本地開發環境設定

### 1. 啟用虛擬環境
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. 安裝依賴（如尚未安裝）
```bash
uv sync
```

### 3. 資料庫遷移
```bash
python manage.py migrate
```

### 4. 建立管理員帳號
```bash
python manage.py createsuperuser
```

### 5. 啟動開發伺服器
```bash
python manage.py runserver
```

## 使用方式

- **管理後台**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
  登入後可管理課程提案（審核）、課程資料、選課紀錄等。

## 開發備註

- 語系已設定為繁體中文（`zh-hant`），時區設定為台北（`Asia/Taipei`）
- 開發環境使用 Console Email Backend（`MAILERS` 設定）
- 目前僅提供 Django Admin 操作介面，未實作自訂前台頁面
