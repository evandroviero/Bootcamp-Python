import os
import pandas as pd
from file_source import FileSource

class CsvSource(FileSource):
    
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data','csv_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.csv')]

        if new_files:
            print(f'New files detected: {new_files}')
            self.previous_files = current_files
        else:
            print('No new files detected.')
    
    
    