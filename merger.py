# -*- coding: utf-8 -*-
""" Python commandline script for merging multiple CSV files in a given directory
"""



import glob, csv, time, sys, argparse

# args

# how to call the function
# Place csv files in a directory. eg. files
# you can specify the name of the output file with -o filename. default name is merged.csv
# Command
# python merger.py -o new.csv ./files

def main(argv):
    dir='.'
    inputfile=None

    parser = argparse.ArgumentParser(description='Merge multiple csv files.')
    parser.add_argument('dir', help='directory containing csv files', default=".")
    parser.add_argument('-o', '--output', help='output file name', default="merged.csv")
    args = parser.parse_args()

    csvfiles =  glob.glob(args.dir.rstrip("/")+'/*.csv')
    startTime = time.time()
    
    with open(args.output,'w', newline='') as f:
        writer = csv.writer(f,delimiter =',')
        
        i = 0
        for file in csvfiles:
            rd = csv.reader(open(file,'r'),delimiter = ',')
            if i != 0:
                next(rd)#skip header
            for row in rd:
                writer.writerow(row)
            i += 1
        print(i)

    
    # print("Done!")
    print("Merged in %.2f"%(time.time() - startTime))


if __name__ == "__main__":
   main(sys.argv[0:])
