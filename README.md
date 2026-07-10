# Fuhrer AI

Fuhrer AI is a production-grade Local AI Assistant designed with a Local-First architecture.

## Goals

- Privacy First
- Local AI
- Offline Capabilities
- Production Ready
- Clean Architecture
- SOLID Principles
- Plugin Based
- High Performance
- Secure by Design

---

## Architecture

## Quick Start

### Local development

1. Create an environment file from the example:

   ```bash
   cp .env.example .env
   ```

2. Install the backend in editable mode:

   ```bash
   pip install -e .
   ```

3. Run the development server:

   ```bash
   make dev
   ```

4. Open the API health check:

   ```bash
   curl http://localhost:8000/health
   ```

### Docker Compose

Run the application and Redis together:

```bash
docker compose up --build
```

The backend listens on `http://localhost:8000` and Redis listens on `localhost:6379`.

## Development Commands

```bash
make format     # Format Python code with Black
make lint       # Lint Python code with Ruff
make typecheck  # Type-check backend code with mypy
make test       # Run pytest
make all        # Run format, lint, typecheck, and tests
```

