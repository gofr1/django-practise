# Testing

Need to install factory:

    sudo pip3 install factory-boy

> As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex objects.

After running `pytest` in a project directory you will get:

        @pytest.mark.django_db
        def test_author_no_permissions(client, non_author):
            """should not allow non-authors to read posts"""
            client.force_login(non_author)
            blocked_response = client.get('/posts/')
    >       assert blocked_response.status_code == status.HTTP_403_FORBIDDEN
    E       assert 200 == 403
    E        +  where 200 = <Response status_code=200, "application/json">.    status_code
    E        +  and   403 = status.HTTP_403_FORBIDDEN

Fixing the issue in `views.py` and all works fine!