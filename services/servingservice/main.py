from skipper_lib.events.event_receiver import EventReceiver
from app.serving_service import ServingService


def main():
    event_receiver = EventReceiver(username='skipper',
                                   password='welcome1',
                                   host='localhost',
                                   port=5672,
                                   queue_name='skipper_serving',
                                   service=ServingService,
                                   service_name='serving',
                                   logger='http://127.0.0.1:5001/api/v1/skipper/logger/log_receiver')


if __name__ == "__main__":
    main()
