from enum import Enum


class Status(Enum):
    OK = 1
    FAIL = 2


def check_if_okey(message:str) -> Status:
    if message.lower() == 'ok':
        return Status.OK
    return Status.FAIL


if check_if_okey('OK') == Status.OK:
    print('All is okay!!')
