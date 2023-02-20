import pytest
from fastapi.testclient import TestClient
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + '/app')
from app.server.app import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_retrieve_students():
    response = await client.get("/student")
    assert response.status_code == 200
    assert len(response.json()) > 0
