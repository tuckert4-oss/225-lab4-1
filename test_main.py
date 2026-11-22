
import sqlite3
import main

def test_homepage(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"

    connection = sqlite3.connect(db_path)
    connection.execute("""
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

    monkeypatch.setattr(main, "DATABASE", str(db_path))

    tester = main.app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert b"Add Contact" in response.data

