import hkbus.kmb.api as api

import time
from datetime import datetime
from typing import Dict, Tuple, List

STOP_ID = "30D564180B68ECA8"


def main():
    eta_dict: Dict[Tuple[str, str, str], List[datetime]] = {}

    while True:
        time.sleep(5)
        eta = api.get_stop_eta(STOP_ID).data
        eta_dict2: Dict[Tuple[str, str, str], List[datetime]] = {}

        for i in eta:
            key = (i.route, i.direction, i.destination)

            if key not in eta_dict:
                eta_dict[key] = []

            eta_dict[key].append(datetime.fromisoformat(i.eta))

        for v in eta_dict2.values():
            v.sort()

        for k in eta_dict2:
            if k not in eta_dict or len(eta_dict[k]) == 0:
                continue

            if len(eta_dict[k]) == 1:
                eta_dict[k].sort()
                eta_dict2[k] = eta_dict[k]
            else:
                eta_dict[k].sort()
                eta_dict2[k] = eta_dict[k][:2]

        for k in eta_dict2:
            eta_dict[k] = eta_dict2[k]


if __name__ == "__main__":
    main()
