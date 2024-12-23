from config.wsgi import application

def test_wsgi_application():
    """Test that the WSGI application is loaded without errors."""
    assert application is not None, "WSGI application is None"
