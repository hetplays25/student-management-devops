import tempfile
import app as app_module

def test_home_page():
    old_path = app_module.DB_PATH
    app_module.DB_PATH = old_path.parent / "test_students.db"
    app_module.init_db()
    client = app_module.app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Management System" in response.data

    if app_module.DB_PATH.exists():
        app_module.DB_PATH.unlink()
    app_module.DB_PATH = old_path

def test_health():
    client = app_module.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
