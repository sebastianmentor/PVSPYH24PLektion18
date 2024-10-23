class Connetion:
    def connect(self):
        ...
    def send_data(self, data):
        ...
    def close_connection(self):
        ...

def connect(connection:Connetion):
    try:
        connection.connect()

    except ConnectionError as e:
        print('Unabel to connect! Check your connection.')

    else:
        connection.send_data('Important data!')


    finally:
        connection.close_connection()