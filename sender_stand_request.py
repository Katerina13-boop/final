import requests
import configuration

def post_new_client_order(body):
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )


def get_client_order_track(params):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
        params=params
    )


