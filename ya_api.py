import requests

ya_token = ...  # Ваш токен
ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'
folder_name = 'test'
ya_params = {'path': f'{folder_name}'}


def create_folder(url: str, token: str, params: dict) -> int:
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':
    create_folder(ya_url, ya_token, ya_params)