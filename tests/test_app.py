from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # voltou 201?
    assert response.status_code == HTTPStatus.CREATED
    # Validar o UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'testusername', 'email': 'test@test.com', 'id': 1}
        ]
    }


def test_update_user(client):
    # cria o usuário
    response = client.post(
        '/users',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # edita o usuário
    response = client.put(
        '/users/1',
        json={
            'password': 'senha123',
            'username': 'test2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'test2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    # cria o usuário
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # deleta o usuário
    response = client.delete('/users/1')

    # verifica se está OK o status e se a mensagem é apresentada.
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    # cria o usuário
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # tenta deletar o usuário.
    response = client.delete('/users/999')

    # Verifica se o cliente 999 não foi encontrado.
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    response = client.get('users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 3,
        'username': 'testusername',
        'email': 'test@test.com',
    }
