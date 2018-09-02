import prometheus_client
from prometheus_client import CollectorRegistry, Gauge, write_to_textfile

registry = CollectorRegistry()
contentForPrometheus = "timing.txt"

gauge_names=[
    'macs_status_and_ttfb',
    'p1_status_and_ttfb',
    'p2_status_and_ttfb',
    'p3_status_and_ttfb',
    'p4_status_and_ttfb',
    'p5_status_and_ttfb',
    'vorl_status_and_ttfb',
    ]

gauges = [
        Gauge('macs_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('p1_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('p2_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('p3_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('p4_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('p5_status_and_ttfb', 'Time spent processing request', registry=registry),
        Gauge('vorl_status_and_ttfb', 'Time spent processing request', registry=registry)
    ]    

def writePrometheusHeader(gCount):
    f = open(contentForPrometheus, "a")
    f.write("# HELP "+ gauge_names[gCount] +" The HTTP Status code and TTFB\n")
    f.write("# TYPE "+ gauge_names[gCount] +" gauge\n")