import logging

import requests

__all__ = [
    'me',
    'current_timer',
]

logger = logging.getLogger(__name__)

API_BASE_URL = 'https://api.track.toggl.com/api/v9/'
TIMEOUT = 5  # sec


def request(path, params=None, token=None):
    assert token is not None, 'Toggl Track API token is required'
    url = f'{API_BASE_URL}{path}'
    logger.debug(f'requesting "{url}" params:{params}')
    try:
        response = requests.request(
            'get',
            url,
            params=params,
            timeout=TIMEOUT,
            auth=(token, 'api_token'),
        )
    except Exception as e:
        logger.error(f'request failed: {e}')
        return
    if not response.ok:
        logger.error(f'response is not OK (status={response.status_code}): {response.text}')
    return response


def me(**kwargs):
    response = request('me', **kwargs)
    if not response:
        return
    return response.json()


def current_timer(**kwargs):
    response = request('me/time_entries/current', **kwargs)
    if not response:
        return
    return response.json()
