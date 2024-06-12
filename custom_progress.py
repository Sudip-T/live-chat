# import sys
# import time



# class SimpleProgressBar:
#     # Define standard and bright color codes
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'

#     # Custom color examples
#     CUSTOM_COLOR_1 = '\033[38;2;32;41;76m'

#     # Reset color
#     END_COLOR = '\033[0m'

#     def __init__(self, total, fill='█', empty='-', fill_color=GREEN, empty_start_color=RED, empty_end_color=GREEN):
#         self.total = total
#         self.length = 100
#         self.prefix = 'Progress : '
#         self.suffix = 'Completed'
#         self.fill = fill
#         self.empty = empty
#         self.fill_color = fill_color
#         self.empty_start_color = empty_start_color
#         self.empty_end_color = empty_end_color
#         self.current = 0

#     def update(self, progress):
#         self.current = progress
#         percent = self.current / self.total
#         filled_length = int(self.length * percent)
#         empty_length = self.length - filled_length
#         half_empty_length = empty_length // 2
#         bar = (
#             f'{self.fill_color}{self.fill * filled_length}{self.END_COLOR}'
#             f'{self.empty_start_color}{self.empty * half_empty_length}{self.END_COLOR}'
#             f'{self.empty_end_color}{self.empty * (empty_length - half_empty_length)}{self.END_COLOR}'
#         )
#         sys.stdout.write(f'\r{self.prefix} {bar} {percent:.1%} {self.suffix}')
#         sys.stdout.flush()

#     def simulate_progress(self, delay=0.05):
#         for i in range(self.total + 1):
#             self.update(i)
#             # time.sleep(delay)
#             # print('hello : ', i)
#         self.close()

#     def close(self):
#         sys.stdout.write('\n')
#         sys.stdout.flush()


# if __name__ == '__main__':
#     total = 100000
#     progress_bar = SimpleProgressBar(
#         total,
#         fill_color=SimpleProgressBar.CUSTOM_COLOR_1         ,
#         empty_start_color=SimpleProgressBar.MAGENTA,
#         empty_end_color=SimpleProgressBar.GREEN
#     )
#     progress_bar.simulate_progress(delay=0.1)




# import sys
# import time


# class SimpleProgressBar:
#     # Define standard and bright color codes
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'

#     # Custom color examples
#     CUSTOM_COLOR_1 = '\033[38;2;32;41;76m'

#     # Reset color
#     END_COLOR = '\033[0m'

#     def __init__(self, total, fill='█', empty='-', fill_color=GREEN, empty_start_color=RED, empty_end_color=GREEN):
#         self.total = total
#         self.length = 100
#         self.prefix = 'Progress : '
#         self.suffix = 'Completed'
#         self.fill = fill
#         self.empty = empty
#         self.fill_color = fill_color
#         self.empty_start_color = empty_start_color
#         self.empty_end_color = empty_end_color
#         self.current = 0

#     def update(self, progress, task_description=''):
#         self.current = progress
#         percent = self.current / self.total
#         filled_length = int(self.length * percent)
#         empty_length = self.length - filled_length
#         half_empty_length = empty_length // 2
#         bar = (
#             f'{self.fill_color}{self.fill * filled_length}{self.END_COLOR}'
#             f'{self.empty_start_color}{self.empty * half_empty_length}{self.END_COLOR}'
#             f'{self.empty_end_color}{self.empty * (empty_length - half_empty_length)}{self.END_COLOR}'
#         )
#         sys.stdout.write(f'\r{self.prefix} {bar} {percent:.1%} {self.suffix} - {task_description}')
#         sys.stdout.flush()

#     def simulate_progress(self, delay=0.05):
#         for i in range(self.total + 1):
#             self.update(i, task_description=f'Processing row {i}/{self.total}')
#             time.sleep(delay)
#         self.close()

#     def close(self):
#         sys.stdout.write('\n')
#         sys.stdout.flush()


# if __name__ == '__main__':
#     total = 100
#     progress_bar = SimpleProgressBar(
#         total,
#         fill_color=SimpleProgressBar.CUSTOM_COLOR_1,
#         empty_start_color=SimpleProgressBar.MAGENTA,
#         empty_end_color=SimpleProgressBar.GREEN
#     )
#     progress_bar.simulate_progress(delay=0.1)


# import sys
# import time

# class SimpleProgressBar:
#     # Define standard and bright color codes
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'

#     # Custom color examples
#     CUSTOM_COLOR_1 = '\033[38;2;32;41;76m'

#     # Reset color
#     END_COLOR = '\033[0m'

#     def __init__(self, total, fill='█', empty='-', fill_color=GREEN, empty_start_color=RED, empty_end_color=GREEN):
#         self.total = total
#         self.length = 100
#         self.prefix = 'Progress : '
#         self.suffix = 'Completed'
#         self.fill = fill
#         self.empty = empty
#         self.fill_color = fill_color
#         self.empty_start_color = empty_start_color
#         self.empty_end_color = empty_end_color
#         self.current = 0

#     def update(self, progress, task_description=''):
#         self.current = progress
#         percent = self.current / self.total
#         filled_length = int(self.length * percent)
#         empty_length = self.length - filled_length
#         half_empty_length = empty_length // 2
#         bar = (
#             f'{self.fill_color}{self.fill * filled_length}{self.END_COLOR}'
#             f'{self.empty_start_color}{self.empty * half_empty_length}{self.END_COLOR}'
#             f'{self.empty_end_color}{self.empty * (empty_length - half_empty_length)}{self.END_COLOR}'
#         )
#         sys.stdout.write(f'\r{self.prefix} {bar} {percent:.1%} {self.suffix} - {task_description}')
#         sys.stdout.flush()

#     def simulate_progress(self, delay=0.05):
#         for i in range(1, self.total + 1):
#             start_time = time.time()
#             time.sleep(delay)  # Simulate work
#             end_time = time.time()
#             iteration_time = end_time - start_time
#             elapsed_time = self.format_time(iteration_time)
#             self.update(i, task_description=f'Processing row {i}/{self.total} {elapsed_time}')
#         self.close()

#     def format_time(self, seconds):
#         days = int(seconds // (24 * 3600))
#         seconds = seconds % (24 * 3600)
#         hours = int(seconds // 3600)
#         seconds %= 3600
#         minutes = int(seconds // 60)
#         seconds %= 60
#         millis = int((seconds - int(seconds)) * 1000)
#         seconds = int(seconds)
#         return f'{days}:{hours}:{minutes}:{seconds}:{millis}'

#     def close(self):
#         sys.stdout.write('\n')
#         sys.stdout.flush()



import sys
import time


class SimpleProgressBar:
    # Define standard and bright color codes
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Custom color examples
    CUSTOM_COLOR_1 = '\033[38;2;32;41;76m'

    # Reset color
    END_COLOR = '\033[0m'

    def __init__(self, total, fill='█', empty='-', fill_color=GREEN, empty_start_color=RED, empty_end_color=GREEN):
        self.total = total
        self.length = 100
        self.prefix = 'Progress : '
        self.suffix = 'Completed'
        self.fill = fill
        self.empty = empty
        self.fill_color = fill_color
        self.empty_start_color = empty_start_color
        self.empty_end_color = empty_end_color
        self.current = 0

    def update(self, progress, task_description=''):
        self.current = progress
        percent = self.current / self.total
        filled_length = int(self.length * percent)
        empty_length = self.length - filled_length
        half_empty_length = empty_length // 2
        bar = (
            f'{self.fill_color}{self.fill * filled_length}{self.END_COLOR}'
            f'{self.empty_start_color}{self.empty * half_empty_length}{self.END_COLOR}'
            f'{self.empty_end_color}{self.empty * (empty_length - half_empty_length)}{self.END_COLOR}'
        )
        sys.stdout.write(f'\r{self.prefix} {bar} {percent:.1%} {self.suffix} - {task_description}')
        sys.stdout.flush()

    def simulate_progress(self, delay=0.05):
        for i in range(1, self.total + 1):
            start_time = time.time()
            time.sleep(delay)  # Simulate work
            end_time = time.time()
            iteration_time = end_time - start_time
            elapsed_time = self.format_time(iteration_time)
            self.update(i, task_description=f'Processing row {i}/{self.total} {elapsed_time}')
        self.close()

    def format_time(self, seconds):
        days = int(seconds // (24 * 3600))
        seconds = seconds % (24 * 3600)
        hours = int(seconds // 3600)
        seconds %= 3600
        minutes = int(seconds // 60)
        seconds %= 60
        millis = int((seconds - int(seconds)) * 1000)
        seconds = int(seconds)
        return f'{days}:{hours}:{minutes}:{seconds}:{millis}'

    def close(self):
        sys.stdout.write('\n')
        sys.stdout.flush()


if __name__ == '__main__':
    total = 100
    progress_bar = SimpleProgressBar(
        total,
        fill_color=SimpleProgressBar.CUSTOM_COLOR_1,
        empty_start_color=SimpleProgressBar.MAGENTA,
        empty_end_color=SimpleProgressBar.GREEN
    )
    progress_bar.simulate_progress(delay=0.1)
