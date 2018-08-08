# coding=utf-8
from enum import Enum
from .models import *


class Status(Enum):
    normal = 0
    abnormal = 1
    offline = 2
    poweroff = 3


def getStatus(data):
    status = ''

    if data is None:
        status = Status.offline
    else:
        nbq1 = float(data[0].nbqgl1)
        nbq2 = float(data[0].nbqgl2)
        nbq3 = float(data[0].nbqgl3)
        nbq4 = float(data[0].nbqgl4)
        nbq5 = float(data[0].nbqgl5)
        nbq6 = float(data[0].nbqgl6)
        nbq7 = float(data[0].nbqgl7)
        nbq8 = float(data[0].nbqgl8)
        nbq9 = float(data[0].nbqgl9)
        nbq10 = float(data[0].nbqgl10)
        if nbq1 and nbq2 and nbq3 and nbq4 and nbq5 and nbq6 and nbq7 and nbq8 and nbq9 and nbq10:
            status = Status.abnormal
        elif not (nbq1 or nbq2 or nbq3 or nbq4 or nbq5 or nbq6 or nbq7 or nbq8 or nbq9 or nbq10):
            status = Status.poweroff
        else:status = Status.normal
    return  status