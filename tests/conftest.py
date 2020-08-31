import pytest
from pyfood.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of Main flask App

    Returns:
        app: main app
    """
    return create_app()
