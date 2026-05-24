import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test"""
    from src.app import activities
    
    # Store original state
    original_state = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Learn and compete in tennis matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["alex@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Join the school basketball team and compete in tournaments",
            "schedule": "Mondays, Wednesdays, Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["marcus@mergington.edu", "ava@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and other visual arts",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["isabella@mergington.edu"]
        },
        "Music Band": {
            "description": "Play instruments and perform in the school band",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
        },
        "Debate Club": {
            "description": "Develop public speaking and argumentation skills through debate",
            "schedule": "Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 18,
            "participants": ["nathan@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore scientific concepts",
            "schedule": "Mondays, 3:30 PM - 4:30 PM",
            "max_participants": 22,
            "participants": ["ryan@mergington.edu", "sophia@mergington.edu"]
        }
    }
    
    yield
    
    # Reset after test
    activities.clear()
    activities.update(original_state)