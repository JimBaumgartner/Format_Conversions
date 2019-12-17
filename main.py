import csv
import json
from info import information
infile = open('data.json','r')
outfile = open('data.csv', 'a')
infile2 = open('data.csv','r')
outfile2 = open('data.json', 'a')
infile3=open('info.py','r')
# funk = input(f'Which Function do you want to run?  >  ' ) 

csv_reader = csv.reader(infile,delimiter = ':')
csv_reader2 = csv.DictReader(infile2)

#convert json file to csv file
def con_json_to_csv():
    writer = csv.writer(outfile)
    for line in infile:
        writer.writerow(line)
        print(line)

#convert csv file to json file
def con_csv_to_json():
    fieldnames = ['Company']
    csv_writer = csv.DictWriter(outfile2, fieldnames=fieldnames,delimiter=',')
    csv_writer.writeheader()
    for line in csv_reader2:
       csv_writer.writerow(line)
    return outfile2

def json_to_dict():
    pass


#convert from dictionary to new json file
def dict_to_json():
    x = json.dumps(information)
    with open('out3.json','a') as f:
        f.write(x)
        f.close()
    


dict_to_json()





