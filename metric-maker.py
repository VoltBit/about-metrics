import os
import datadog
import statsd
from colorama import init, Fore, Style

# colorama init
init()

class MetricMaker(object):

    def __init__(self):
        self.__initialize_dd()

    def __initialize_dd(self):
        options = {
            'api_key': os.getenv('DD_API_KEY'),
            'app_key': os.getenv('DD_APP_KEY'),
            'statsd_host': '0.0.0.0',
            'statsd_port': 8125
        }

        if not options['api_key']:
            print(Fore.YELLOW + 'Warning: Missing API key')
        if not options['app_key']:
            print(Fore.YELLOW + 'Warning: Missing APP key')
        print(Style.RESET_ALL)
        datadog.initialize(**options)

    def make_gauge(self):
        print('Making a gauge')
        datadog.statsd.gauge('bogus_gauge', 40)

    def make_histogram(self):
        print('Making a histogram')
        pass

    def make_counter(self):
        print('Making a counter')
        # datadog.statsd.increment('bogus_counter_metric')
        datadog.statsd.increment('bogus_counter_metric', 10)

    def make_distribution(self):
        print('Making a distribution')
        pass

class MetricOrchestra(object):
    pass

def main():
    mm = MetricMaker()
    mm.make_counter()

if __name__ == '__main__':
    main()
