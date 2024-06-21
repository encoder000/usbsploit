def send_report(report):
    open('/dev/hidg0', 'rb+').write(report)
