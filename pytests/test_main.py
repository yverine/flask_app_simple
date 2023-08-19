from flask import current_app
from app import create_app

def test_current_app_exists():
    app = create_app()
    with app.app_context():
        assert current_app is not None
