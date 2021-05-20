def test_login(test_app_with_auth):

    data = {"username": "admin", "password": "pass"}
    response = test_app_with_auth.post("/token", data=data)

    assert response.status_code == 200


def test_login_failure(test_app_with_auth):

    data = {"username": "admin", "password": "1010"}
    response = test_app_with_auth.post("/token", data=data)

    assert response.status_code == 401
