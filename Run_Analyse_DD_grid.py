## Script to run BeamFetcher and PreProcessTrigOverlap tool chains
## M. Ascencio, Tue Apr 11, 2023

import os
import csv
import pandas as pd
import pytz
from datetime import datetime
import sys

# converts from Inp time zone to CT
def INP2CT(UTC_input_time):
    # create a datetime object representing the Inp time
    inp_tz = pytz.timezone('Europe/London')
    inp_time = datetime.strptime(UTC_input_time, '%Y-%m-%d %H:%M:%S.%f')
    inp_time = inp_tz.localize(inp_time) 

    # convert the Inp time to CT
    ct_zone = pytz.timezone('US/Central')
    ct_time = inp_time.astimezone(ct_zone)    

    return ct_time.strftime('%Y-%m-%d %H:%M:%S.%f')

# find run
def find_run(searched_value, path):
    df = pd.read_csv(path)
    print(df)
    return df.loc[df['run'] == searched_value] 

# replace run number in BeamFetcher configfile
def update_configfile(run_value):
    runvalue = str(run_value)
    conf_dir = "configfiles/BeamFetcher/"
    conf_file = "BeamFetcherConfig"
    sedtail = conf_dir+conf_file+" > "+conf_dir+"temp1 && mv "+conf_dir+"temp1 "+conf_dir+conf_file 
    outputname_line = "sed \'3s/.*/OutputFile .\/"+runvalue+"_beamdbr /\' " + sedtail 
    runnumber_line  = "sed \'6s/.*/RunNumber "+runvalue+"/\' " + sedtail

    # execute
    print(outputname_line)
    os.system(outputname_line)
    print(runnumber_line)
    os.system(runnumber_line)
   
# create a start and end files in BeamFetcher confifile
def make_start_end_files(start_val,end_val):
    conf_dir = "configfiles/BeamFetcher/" 
    start_file = "echo \""+start_val+"\" > "+conf_dir+"my_start_date.txt"
    end_file = "echo \""+end_val+"\" > "+conf_dir+"my_end_date.txt" 

    # execute
    print(start_file)
    os.system(start_file)
    print(end_file)
    os.system(end_file)


def make_rawlist(path, runnumber, PreProcessTrigOverlap):
    rawlist = path+str(runnumber)
    execute = "source configfiles/PreProcessTrigOverlap/CreateMyList.sh "+rawlist+" "+str(runnumber)
    print(execute)
    os.system(execute)

    out_cat = "cat ./my_files.txt"
    print(out_cat)
    os.system(out_cat)
    
    movePre = ""
    if PreProcessTrigOverlap == True:
        movePre = "mv ./my_files.txt configfiles/PreProcessTrigOverlap/"
    else:
        movePre = "mv ./my_files.txt configfiles/DataDecoderMRD/"

    print(movePre)
    os.system(movePre)

def run_beam_fetcher(my_run, path):
    run_number       = find_run(my_run, path)
    print(run_number)
    start_time_inptz = run_number['start'].values[0]
    end_time_inptz   = run_number['end'].values[0] 

    start_time_ct = INP2CT(start_time_inptz)
    end_time_ct   = INP2CT(end_time_inptz) 

    make_start_end_files(start_time_ct, end_time_ct)
    update_configfile(my_run)

    tool = "/ToolAnalysisGrid/./Analyse configfiles/BeamFetcher/ToolChainConfig" 
    print(tool)
    #os.system(tool) 


def run_PreProcessTrigOverlap(path, runnnumber):
    #make_rawlist(path, runnnumber, True) 
    tool = "/ToolAnalysisGrid/./Analyse configfiles/PreProcessTrigOverlap/ToolChainConfig" 
    print(tool)
    os.system(tool) 

def run_DataDecoderMRD(path, runnnumber):
    #make_rawlist(path, runnnumber, False) 
    tool = "/ToolAnalysisGrid/./Analyse configfiles/DataDecoderMRD/ToolChainConfig" 
    print(tool)
    os.system(tool) 

def run_DataDecoder(path, runnnumber):
    #make_rawlist(path, runnnumber, False) 
    tool = "/ToolAnalysisGrid/./Analyse configfiles/DataDecoder/ToolChainConfig" 
    print(tool)
    os.system(tool) 


def main():
    if len(sys.argv) < 2:
        print("ERROR: You need to add an the run number. Try like `python3 Run_Analyse_MRD.py 4197` ")
        sys.exit(1)
    else:
        print(">>--------------- RUNNING ----------------<<")
    
    my_run      = int(sys.argv[1])
    path        = str(sys.argv[2])
    rawdatapath = str(sys.argv[3])

    #path = '/annie/app/users/mascenci/ToolAnalysis_ANNIEsoft/new_version/RunINFO.csv'
    #rawdatapath = '/pnfs/annie/persistent/raw/raw/'

    run_beam_fetcher(my_run,path)
    run_PreProcessTrigOverlap(rawdatapath,my_run) 
    #run_DataDecoderMRD(rawdatapath,my_run) 
    run_DataDecoder(rawdatapath,my_run) 

if __name__ == "__main__":
    main()
