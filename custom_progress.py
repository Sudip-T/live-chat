# import sys
# import time

# class SimpleProgressBar:
#     GREEN = '\033[92m'  # ANSI escape code for green color
#     END_COLOR = '\033[0m'  # ANSI escape code to reset color

#     def __init__(self, total, length=40, prefix='Progress', suffix='Complete', fill='█', empty='-', start_char='[', end_char=']'):
#         self.total = total
#         self.length = length
#         self.prefix = prefix
#         self.suffix = suffix
#         self.fill = fill
#         self.empty = empty
#         self.start_char = start_char
#         self.end_char = end_char
#         self.current = 0

#     def update(self, progress):
#         self.current = progress
#         percent = self.current / self.total
#         filled_length = int(self.length * percent)
#         bar = self.fill * filled_length + self.empty * (self.length - filled_length)
#         progress_bar = f'{self.GREEN}{bar}{self.END_COLOR}'
#         sys.stdout.write(f'\r{self.prefix} {progress_bar} {percent:.1%} {self.suffix}')
#         sys.stdout.flush()

#     def close(self):
#         sys.stdout.write('\n')
#         sys.stdout.flush()

# # Example usage
# total_items = 100
# progress_bar = SimpleProgressBar(total_items, prefix='Progress:', suffix='Complete', length=100)

# for i in range(total_items):
#     # Do some work here
#     time.sleep(0.1)  # Simulating work
#     progress_bar.update(i + 1)

# progress_bar.close()



import sys
import time


class SimpleProgressBar:
    GREEN = '\033[92m'  # ANSI escape code for green color
    END_COLOR = '\033[0m'  # ANSI escape code to reset color

    def __init__(self, total, fill='█', empty='-'):
        self.total = total
        self.length = 100
        self.prefix = 'Progress'
        self.suffix = 'Complete'
        self.fill = fill 
        self.empty = empty
        self.current = 0

    def update(self, progress):
        self.current = progress
        percent = self.current / self.total
        filled_length = int(self.length * percent)
        bar = self.fill * filled_length + self.empty * (self.length - filled_length)
        progress_bar = f'{self.GREEN}{bar}{self.END_COLOR}'
        sys.stdout.write(f'\r{self.prefix} {progress_bar} {percent:.1%} {self.suffix}')
        sys.stdout.flush()

    def close(self):
        sys.stdout.write('\n')
        sys.stdout.flush()



# Example usage
total_items = 100
progress_bar = SimpleProgressBar(total_items)


for i in range(total_items):
    time.sleep(0.1)
    progress_bar.update(i + 1)

progress_bar.close()