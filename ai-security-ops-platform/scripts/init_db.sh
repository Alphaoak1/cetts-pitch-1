#!/bin/bash
docker exec -it backend alembic upgrade head
docker exec -it backend python scripts/create_admin.py