import psutil
from time import sleep

def __main__():
    get_bandwidth       = psutil.net_io_counters()
    initial_total       = get_bandwidth.bytes_sent + get_bandwidth.bytes_recv

    while True:        
        get_bandwidth   = psutil.net_io_counters()
        bandwidth_used  = get_bandwidth.bytes_sent + get_bandwidth.bytes_recv - initial_total

        print_total(bandwidth_used)
        sleep(1)

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return round(size,2), power_labels[n]+'bytes'


def print_total(bandwidth_used):
    formated_bytes, unit = format_bytes(bandwidth_used)
    print(f"Total bandwidth used: {formated_bytes} {unit}", end="\r")

if __name__ == '__main__':
    __main__()