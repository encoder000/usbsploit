def send_report_keyboard(report):
    open('/dev/hidg0', 'rb+').write(report)


def send_report_mouse(report):
    open('/dev/hidg1', 'rb+').write(report)
