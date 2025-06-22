import sender_stand_request

# Берегова Екатерина, 31 когорта, финальный проект, Инженер по тестированию расширенный
def test_create_order():
    order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    order_response = sender_stand_request.post_new_client_order(order_body)

    # Проверка, что код ответа равен 201
    assert order_response.status_code == 201, f"Expected status code 201, but got {order_response.status_code}"

    track = order_response.json().get("track")
    track_params = {
        "t": track
    }
    track_response = sender_stand_request.get_client_order_track(track_params)

    assert track_response.status_code == 200, f"Expected status code 200, but got {track_response.status_code}"