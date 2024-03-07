import os
import pandas as pd
from file_source import FileSource
import chardet
import csv

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
            self.transform_data_to_df()
        else:
            print('No new files detected.')

    def transform_data_to_df(self):
        for i in  self.previous_files:
            file = self.folder_path + '/' +i
            encoding = self.detect_encoding(file)
            _ = pd.read_csv(file, encoding=encoding)
            print(_)

    def detect_encoding(self, filename: str) -> str:
        with open(filename, 'rb') as file:
            raw_data = file.read(1024)
        result = chardet.detect(raw_data)
        return result['encoding']
    
    
    