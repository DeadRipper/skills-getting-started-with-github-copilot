def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity = "Tennis Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert expected_activity in data
    assert data[expected_activity]["max_participants"] == 16
    assert "alex@mergington.edu" in data[expected_activity]["participants"]


def test_signup_adds_participant_to_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Tennis Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    response = client.get("/activities")
    participants = response.json()[activity_name]["participants"]
    assert email in participants


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Nonexistent Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_fails_when_already_registered(client):
    # Arrange
    email = "alex@mergington.edu"
    activity_name = "Tennis Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "You are already registered for this activity"


def test_unregister_removes_participant(client):
    # Arrange
    email = "alex@mergington.edu"
    activity_name = "Tennis Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    response = client.get("/activities")
    participants = response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_not_registered_returns_400(client):
    # Arrange
    email = "notregistered@mergington.edu"
    activity_name = "Tennis Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "You are not registered for this activity"


def test_unregister_nonexistent_activity_returns_404(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Nonexistent Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
