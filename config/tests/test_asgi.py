from config.asgi import application

def test_asgi_application():
    """Test if the ASGI application is loaded without errors."""
    assert application is not None, "ASGI application is None"
