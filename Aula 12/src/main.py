import schedule
import time
from csv_source import CsvSource

csv = CsvSource()


for i in range(1, 10):
    csv.create_path()
    csv.check_for_new_files()
    time.sleep(1)
    