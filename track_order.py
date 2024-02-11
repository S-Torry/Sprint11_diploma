#Спиридонова_Виктория_13когорта
import send_request

def get_order_track_number ():
    track_number = send_request.post_new_order()
    return track_number.json()["track"]

def test_create_track_order ():
    track_number = get_order_track_number()
    get_response = send_request.get_order_info(track_number)
    assert get_response.status_code == 200
