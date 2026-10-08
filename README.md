# Aqua Bandhu AI — Seafood Supply Chain Platform

Aqua Bandhu is an end-to-end seafood supply chain platform featuring two connected windows:
1. **Buyer Dashboard**: Marketplace, live stock verification, Buy Now orders, real-time tracking.
2. **Automation / AI Operations Dashboard**: 11 command center pages, 7-agent AI orchestration, warehouse management (Stock In / Stock Out).
3. **Split-Screen Sync**: Side-by-side live synchronized view.

## Quick Start

### Option 1: Double Click
Double click `start_app.bat` to launch the server.

### Option 2: Command Line
```powershell
cd C:\Users\kopan\Desktop\aqua-bandhu
.venv\Scripts\python.exe run.py
```

Then open your browser at:
**http://127.0.0.1:8000**

## Project Structure
- `app/`
  - `main.py`: FastAPI routes, WebSocket endpoint, GPS telemetry simulator
  - `services.py`: Transactional order placement, inventory reservations, harvest intake
  - `ai_engine.py`: Multi-agent orchestration engine
  - `event_bus.py`: Real-time WebSocket event broadcaster
  - `database.py`: SQLite schema and connection manager
  - `seed_data.py`: Initial datasets from references
- `static/`
  - `css/style.css`: Glassmorphic dark marine design system
  - `js/app.js`: Interactive frontend logic and modal controllers
  - `js/websocket.js`: Live WebSocket synchronization client
  - `assets/`: Approved seafood, truck, farmer, warehouse imagery
- `templates/`
  - `index.html`: Complete HTML application template
- `aquabandhu.db`: Persistent SQLite database
- `test_flow.py`: End-to-end verification script
- `run.py`: Application launcher
