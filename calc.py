import csv
import sys

import pandas as pd
from objects import Subject, Transcript
import tabula


class PDFParser:
    pass

class CSVParser:
    def __init__(self):
        self.transcript = Transcript()
        self.failed_rows = []
    
    def read_transcript(self, filepath):
        with open(filepath) as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                try:
                    year = row[0]
                    session = row[1]
                    uos_code = row[2]
                    uos_name = row[3]
                    mark = int(float(row[4]))
                    # grade = row[5]
                    credit_points = int(row[6])

                    new_subject = Subject(year, session, uos_code, uos_name, mark, credit_points)
                    self.transcript.add_subject(new_subject)
                except:
                    self.failed_rows.append(row)
                    continue

    def calc_wam(self):
        return self.transcript.get_wam()




if __name__ == '__main__':
    # df = read_pdf("/Users/vincey/Documents/repos/wam-calc/transcript/sample.pdf", pages='all', silent=False)
    # print(df) 

    # tabula.convert_into("/Users/vincey/Documents/repos/wam-calc/transcript/sample.pdf", \
    #                     "/Users/vincey/Documents/repos/wam-calc/transcript/pdfsample.csv",
    #                     output_format='csv', pages='all')



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

    parser = CSVParser()
    parser.read_transcript(test_file)
    print(parser.calc_wam())
