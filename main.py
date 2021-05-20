import logging
import sys
import json

import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)


def read_metrics(filename):
    time_stamps = None
    values = None

    with open(filename, 'r') as f:
        response = json.load(f)

        if len(response.get('MetricDataResults', [])) == 1:
            result_set = response.get('MetricDataResults')[0]
            time_stamps = list()
            for buf in result_set.get('Timestamps', []):
                time_stamps.append(buf[:16])
            values = result_set.get('Values', [])

    return time_stamps, values


def draw_something(xstuff, ystuff):
    logger.info('draw_something() called')
    xpoints = np.array(xstuff)
    ypoints = np.array(ystuff)

    plt.plot(xstuff, ystuff)
    plt.xticks(xstuff, xstuff, rotation=-90)
    # plt.tight_layout(rect=(0.1, 0.1, 1, 1))
    plt.tight_layout(pad=2.25)  # , w_pad=1.5, h_pad=0)
    plt.title("SMB v3 Connections (average / hour) 2")
    plt.xlabel("Time")
    plt.ylabel("Connections")
    plt.savefig('food.png')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S'
    )

    xstuff, ystuff = read_metrics(sys.argv[1])
    draw_something(xstuff, ystuff)
