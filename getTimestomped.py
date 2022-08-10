#!/usr/bin/env python3
#Dr0p

import os
import datetime
import argparse
from subprocess import run
import csv 

def argsParser():
    pars = argparse.ArgumentParser()
    pars.add_argument("--path","-p", help="Path to find all files recursive")
    pars.add_argument("--dst","-d", help="Path to output")
    return pars


def FileList(path):
    filelist = run(f"find {path} -type f",shell=True,text=True,capture_output=True).stdout.split("\n")[:-1]
    return filelist
    
def timer(stamp):
    return datetime.datetime.fromtimestamp(stamp)

def getTimestompedFiles(filelist,dst):
    timestomped = []

    if len(filelist) > 0:
        for elem in filelist:
            filestat = os.stat(elem)
            if(timer(filestat.st_atime).microsecond == 0):
                timestomped.append(elem)

        print("[*] All Files are checked")
        if len(timestomped) > 0:
            print(f"[*] Detected {len(timestomped)} Files with possible timestomping")

            with open(f"{dst}/timestomped.csv","w") as f:
                f.write("Accesstime,Changetime,Filename\n")
                for elem in timestomped:
                    data = {timer(filestat.st_atime),timer(filestat.st_ctime),elem}
                    f.write(f"{timer(filestat.st_atime)},{timer(filestat.st_ctime)},{elem}\n")
        else:
            print("[*] Detected no files with possible timestomping")
    else:
        print(f"[*] No Files to check")

def main():
    pars = argsParser()
    args = pars.parse_args()

    if args.path is None:
        args.path = "."
    if args.dst is None:
        args.dst = "."

    filelist = FileList(args.path)
    getTimestompedFiles(filelist,args.dst)

if __name__ == "__main__":
    main()
