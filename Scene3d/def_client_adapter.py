import os
import logging

def client_adapter_func(client, json_data):
    while True:
        try:
            message = client.recv(1024).decode()
            logging.info('def_client_adapter' + message)
            if message == '1':
                data = json_data.get()
                client.send(data.decode())
                logging.info('client send')
            if message == 'e':
                json_data.exit = True
                logging.info('exit')
                os._exit(0)
        except ConnectionRefusedError:
            logging.error('Planner disconnected. ConnectionRefusedError')
        except ConnectionAbortedError:
            logging.error('Planner disconnected. ConnectionAbortedError')
        except ConnectionResetError:
            logging.error('Planner disconnected. ConnectionResetError')
    client.close()
