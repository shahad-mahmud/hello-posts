from app.users.services import get_user_details_service


def test_get_user_details_service():
    user_id = 1
    result = get_user_details_service(user_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == user_id

    # Test case 2: Test without user ID
    result = get_user_details_service()
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0

    # Test case 3: Test with invalid user ID
    user_id = -999
    result = get_user_details_service(user_id)
    assert result is None
