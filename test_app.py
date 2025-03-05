from app import fetch_data


def test_fetch_data():
    data = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
    # Check if the fetched data has an 'id' key with value 1
    assert data["id"] == 1
