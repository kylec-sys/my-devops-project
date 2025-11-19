#!/usr/bin/env python3
"""
简单的应用测试
"""
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """测试首页"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, DevOps!' in response.data

def test_health_endpoint(client):
    """测试健康检查接口"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_info_endpoint(client):
    """测试信息接口"""
    response = client.get('/info')
    assert response.status_code == 200
    assert b'DevOps' in response.data

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
