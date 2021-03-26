from .detik import Detik
from .liputan6 import Liputan6
from .cnnIndo import CnnIndo
from .kompas import Kompas
from .tempo import Tempo
from .turnbackhoax import TurnBackHoax
from .newsBase import NewsBaseSrc
from .newsResult import NewsResult

from enum import Enum
from datetime import datetime
from typing import List

availableSrc = {
    "detik": Detik(),
    "liputan6": Liputan6(),
    "cnnIndo": CnnIndo(),
    "kompas": Kompas(),
    "tempo": Tempo(),
    "turnbackhoax": TurnBackHoax()
}


def init(src, target_total, start_date=None, end_date=None):
    sourceClass: NewsBaseSrc = availableSrc.get(src, "detik")

    result: List[NewsResult] = sourceClass.run(target_total=target_total,
                                               start_date=start_date, end_date=end_date)

    return result
