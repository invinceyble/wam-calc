import csv
import sys
import os

import pandas as pd
from objects import Subject, Transcript
import tabula

class Parser:
    def __init__(self):
        self.transcript = Transcript()
        self.failed_rows = []

    def read_transcript(self, filepath):
        df = self.get_df(filepath)
        for row in df.iterrows():
            row = row[1]
            try:
                year = row[0]
                session = row[1]
                uos_code = row[2]
                uos_name = row[3]
                mark = int(float(row[4]))
                credit_points = int(row[6])

                new_subject = Subject(year, session, uos_code, uos_name, mark, credit_points)
                self.transcript.add_subject(new_subject)
            except:
                self.failed_rows.append(row)
                continue

    def read_text(self, text):
        transcript = text.split('\n')
        transcript = [row.split('\t') for row in transcript]
        for row in transcript:
            try:
                year = row[0]
                session = row[1]
                uos_code = row[2]
                uos_name = row[3]
                mark = int(float(row[4]))
                credit_points = int(row[6])

                new_subject = Subject(year, session, uos_code, uos_name, mark, credit_points)
                self.transcript.add_subject(new_subject)
            except:
                self.failed_rows.append(row)
                continue
    
    def get_df(self, filepath):
        file_type = str(filepath.filename).split('.')[1].lower()
        if file_type == 'csv':
            return pd.read_csv(filepath, na_filter=False)
        elif file_type in ['xlsx', 'xls']:
            return pd.read_excel(filepath)
        elif file_type == 'pdf':
            filepath.save('temp.pdf')
            df = tabula.read_pdf('temp.pdf', pages='all')
            os.remove("temp.pdf")
            return df

    def calc_wam(self):
        return self.transcript.get_wam()

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("No file given in command line, using sample.csv instead.")
        test_file = "/Users/vincey/Documents/repos/wam-calc/transcript/sample.csv"
    else:
        test_file = sys.argv[1]

    file_type = test_file.split('.')[1]
    print(file_type)
    if file_type.lower() == 'pdf':
        print("File type is pdf, converting to csv file")
        tabula.convert_into(test_file, "transcript/pdfconvert.csv", output_format='csv', pages='all', silent=True)
        test_file = "transcript/pdfconvert.csv"

    parser = Parser()
    parser.read_transcript(test_file)
    print(parser.calc_wam())
