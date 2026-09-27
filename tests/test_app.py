import os
import sys
import tempfile

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import app as app_module


def test_home_page():

    # Use a separate temporary database for testing
    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()

    app_module.DATABASE = temp_db.name

    # Create the required database table
    app_module.init_db()

    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:

        response = client.get("/")

        assert response.status_code == 200

    # Remove temporary database
    os.unlink(temp_db.name)