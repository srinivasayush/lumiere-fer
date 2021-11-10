def show_current_progress(current: int, total: int, bar_length = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * bar_length - 1) + '>'
    spaces  = ' ' * (bar_length - len(arrow))

    print(f'Progress: [{arrow}{spaces}] {current}/{total}', end='\r')
