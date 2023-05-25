# Script based on James Minock's bash script
# M. Ascencio, Wed Apr 12, 2023

import os
import sys

# Make a script given an array with rawfile's IDs and the run number 
def submit_script_subset_lappd(subset, total_file, run_number):
    pathBF='./submit_job.sh'
    os.system('rm '+pathBF)

    job_commnad = 'jobsub_submit -G annie --expected-lifetime=${QUEUE} --memory=4000MB --disk=30GB'
    job_commnad += ' --resource-provides=usage_model=OFFSITE --site=Colorado,BNL,Caltech,Nebraska,SU-OG,Wisconsin,UCSD,NotreDame,MIT,Michigan,MWT2,UChicago,Hyak_CE'
    job_commnad += ' -f ${INPUT_PATH}/ToolAnalysis_ANNIEsoft_grid.tar.gz' 
    job_commnad += ' -f ${INPUT_PATH}/script_for_singularity.sh' 

    #for i in range(0,total_file):
    new_subset = []
    new_subset_2 = [2,34,5]
    print(len(subset))
    new_subset_2 = new_subset_2 + [subset[0]] + [subset[(len(subset) - 1)]]
    print(new_subset_2) 
    new_subset = subset

    '''
    if subset[0] == 0:
        new_subset = subset + [subset[(len(subset) - 1)]] 
    else:
        if subset[(len(subset) - 1)] == (total_file - 1):
            new_subset = [(subset[0] - 1)] + subset
            print(subset[(len(subset) - 1)])
            print((total_file - 1))
        else:
            new_subset = [(subset[0] - 1)] + subset + [(subset[(len(subset) - 1)] + 1)] 
    '''
    new_subset = subset

    for i in range(0, len(new_subset)):
        rawname = 'RAWDataR'+str(run_number)+'S0p'+str(new_subset[i])
        print(rawname)
        job_commnad = job_commnad +  ' -f ${INPUT_PATH_RAWFILE}/'+rawname

    job_commnad = job_commnad + ' -d OUTPUT $OUTPUT_FOLDER file://${SCRIPT_PATH}/script_for_grid_lappd.sh '+str(run_number)+' '+str(subset[0])+' '+str(subset[(len(subset) -1 )])+' \n' 
    print(job_commnad) 
    with open(pathBF, 'w') as f:
        f.write('#!/bin/bash \n')
        f.write(' \n')
        f.write('export SCRIPT_PATH=/annie/app/users/mascenci/GridSubmissionII/nested_container/ \n')
        f.write('export INPUT_PATH=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/tool_lappd/ \n')
        f.write('export INPUT_PATH_RAWFILE=/pnfs/annie/persistent/raw/raw/'+str(run_number)+'\n')
        f.write(' \n')
        f.write('QUEUE=medium \n')
        f.write('OUTPUT_FOLDER=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/output_lappd/'+str(run_number)+' \n')
        f.write('mkdir -p $OUTPUT_FOLDER \n')
        f.write(' \n')
        f.write(job_commnad)

# Make a script given an array with rawfile's IDs and the run number 
def submit_script_subset(subset, total_file, run_number):
    pathBF='./submit_job.sh'
    os.system('rm '+pathBF)

    job_commnad = 'jobsub_submit -G annie --expected-lifetime=${QUEUE} --memory=4000MB --disk=30GB'
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/ToolAnalysis_ANNIEsoft_grid.tar.gz' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/my_prueba.sh' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/Run_Analyse_DD.py' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/RunINFO.csv' 

    #for i in range(0,total_file):
    new_subset = []
    new_subset_2 = [2,34,5]
    print(len(subset))
    new_subset_2 = new_subset_2 + [subset[0]] + [subset[(len(subset) - 1)]]
    print(new_subset_2) 
    new_subset = subset

    if subset[0] == 0:
        new_subset = subset + [subset[(len(subset) - 1)]] 
    else:
        if subset[(len(subset) - 1)] == (total_file - 1):
            new_subset = [(subset[0] - 1)] + subset
            print(subset[(len(subset) - 1)])
            print((total_file - 1))
        else:
            new_subset = [(subset[0] - 1)] + subset + [(subset[(len(subset) - 1)] + 1)] 

    for i in range(0, len(new_subset)):
        rawname = 'RAWDataR'+str(run_number)+'S0p'+str(new_subset[i])
        print(rawname)
        job_commnad = job_commnad +  ' -f ${INPUT_PATH_RAWFILE}/'+rawname

    job_commnad = job_commnad + ' -d OUTPUT $OUTPUT_FOLDER file://${SCRIPT_PATH}/Send_script.sh '+str(run_number)+' '+str(subset[0])+' '+str(subset[(len(subset) -1 )])+' \n' 
    print(job_commnad) 
    with open(pathBF, 'w') as f:
        f.write('#!/bin/bash \n')
        f.write(' \n')
        f.write('export SCRIPT_PATH=/annie/app/users/mascenci/GridSubmissionII/nested_container/ \n')
        f.write('export INPUT_PATH=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/tool/ \n')
        f.write('export INPUT_PATH_RAWFILE=/pnfs/annie/persistent/raw/raw/'+str(run_number)+'/ \n')
        f.write(' \n')
        f.write('QUEUE=medium \n')
        f.write('OUTPUT_FOLDER=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/output/'+str(run_number)+' \n')
        f.write('mkdir -p $OUTPUT_FOLDER \n')
        f.write(' \n')
        f.write(job_commnad)

# Make a script given number of rawfile and the run number 
def submit_script(nfiles, run_number):
    pathBF='./submit_job.sh'
    os.system('rm '+pathBF)

    job_commnad = 'jobsub_submit -G annie --expected-lifetime=${QUEUE} --memory=4000MB --disk=30GB'
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/ToolAnalysis_ANNIEsoft_grid.tar.gz' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/my_prueba.sh' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/Run_Analyse_DD.py' 
    job_commnad = job_commnad + ' -f ${INPUT_PATH}/RunINFO.csv' 

    for i in range(0,nfiles):
        rawname = 'RAWDataR'+str(run_number)+'S0p'+str(i)
        job_commnad = job_commnad +  ' -f ${INPUT_PATH_RAWFILE}/'+rawname

    job_commnad = job_commnad + ' -d OUTPUT $OUTPUT_FOLDER file://${SCRIPT_PATH}/Send_script.sh '+str(run_number)+' \n' 

    with open(pathBF, 'w') as f:
        f.write('#!/bin/bash \n')
        f.write(' \n')
        f.write('export SCRIPT_PATH=/annie/app/users/mascenci/GridSubmissionII/nested_container/ \n')
        f.write('export INPUT_PATH=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/tool/ \n')
        f.write('export INPUT_PATH_RAWFILE=/pnfs/annie/persistent/raw/raw/'+str(run_number)+'/ \n')
        f.write(' \n')
        f.write('QUEUE=medium \n')
        f.write('OUTPUT_FOLDER=/pnfs/annie/persistent/users/mascenci/GridToolAnalysis/output/'+str(run_number)+' \n')
        f.write('mkdir -p $OUTPUT_FOLDER \n')
        f.write(' \n')
        f.write(job_commnad)

# Send script, this is the script the will run in the grid 
def make_send_script_lappd():
    pathSS = './script_for_grid_lappd.sh'
    os.system('rm '+pathSS)

    with open(pathSS, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('#  Based on /annie/app/users/dingpf/GridSub_test.sh\n')
        f.write('#  Copied from James Minock\n')
        f.write('\n')
        f.write('cat <<EOF\n')
        f.write('condor   dir: $CONDOR_DIR_INPUT\n')
        f.write('process   id: $PROCESS\n')
        f.write('output   dir: $CONDOR_DIR_OUTPUT\n')
        f.write('EOF\n')
        f.write('\n')
        f.write('HOSTNAME=$(hostname -f)\n')
        f.write('GRIDUSER="mascenci"\n')
        f.write('\n')
        f.write('echo "Job starting on $(uname -a)"\n')
        f.write('\n')
        f.write('DUMMY_OUTPUT_FILE=${CONDOR_DIR_OUTPUT}/${JOBSUBJOBID}_dummy_output\n')
        f.write('touch ${DUMMY_OUTPUT_FILE}\n')
        f.write('\n')
        f.write('# Copy datafiles\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/script_for_singularity.sh .\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/ToolAnalysis_ANNIEsoft_grid.tar.gz .\n')
        f.write('\n')
        f.write('tar -xzf ToolAnalysis_ANNIEsoft_grid.tar.gz\n')
        f.write('rm ToolAnalysis_ANNIEsoft_grid.tar.gz\n')
        f.write('ls -lrt  > /srv/log_001.log\n')
        f.write('\n')
        f.write('# Moving stuff\n')
        f.write('mv script_for_singularity.sh ToolAnalysis_ANNIEsoft_grid/\n')
        f.write('\n')
        f.write('cd ToolAnalysis_ANNIEsoft_grid\n')
        f.write('echo $CONDOR_DIR_INPUT > path_file.txt\n')
        f.write('cat ToolAnalysis_ANNIEsoft_grid/path_file.txt  > log_path.log\n')
        #f.write('singularity exec -B/srv:/srv,${CONDOR_DIR_INPUT},${PWD}:/ToolAnalysisGrid /cvmfs/singularity.opensciencegrid.org/anniesoft/toolanalysis\:latest/ $CONDOR_DIR_INPUT/script_for_singularity.sh $1 $2 $3\n')
        f.write('singularity exec -B/srv:/srv,${CONDOR_DIR_INPUT},${PWD}:/ToolAnalysisGrid /cvmfs/singularity.opensciencegrid.org/anniesoft/toolanalysis\:latest/ $CONDOR_DIR_INPUT/script_for_singularity.sh $1 $2 $3\n')
        f.write('\n')
        f.write('echo "Moving the output files to CONDOR OUTPUT:" >> ${DUMMY_OUTPUT_FILE}\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *.root ${CONDOR_DIR_OUTPUT}\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D ProcessedRawData_* ${CONDOR_DIR_OUTPUT}\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *.log ${CONDOR_DIR_OUTPUT}\n')
        f.write('${JSB_TMP}/ifdh.sh cp -D /srv/*.log ${CONDOR_DIR_OUTPUT}\n')
        f.write('\n')
        f.write('echo "Cleaning up:" >> ${DUMMY_OUTPUT_FILE}\n')
        f.write('cd ..\n')
        f.write('rm /srv/script_for_singularity.sh\n')
        f.write('rm -rf ToolAnalysis_ANNIEsoft_grid/\n')
        f.write('## END ##\n')

# Send script, this is the script the will run in the grid 
def make_send_script():
    pathSS = './send_script_test.sh'
    os.system('rm '+pathSS)

    with open(pathSS, 'w') as f:
        f.write('#!/bin/bash \n')
        f.write('#  Based on /annie/app/users/dingpf/GridSub_test.sh \n')
        f.write('#  Copied from James Minock \n')
        f.write(' \n')
        f.write('cat <<EOF \n')
        f.write('condor   dir: $CONDOR_DIR_INPUT \n')
        f.write('process   id: $PROCESS \n')
        f.write('output   dir: $CONDOR_DIR_OUTPUT \n')
        f.write('EOF \n')
        f.write(' \n')
        f.write('HOSTNAME=$(hostname -f) \n')
        f.write('GRIDUSER="mascenci" \n')
        f.write(' \n')
        f.write('echo "Job starting on $(uname -a)" \n')
        f.write(' \n')
        f.write('DUMMY_OUTPUT_FILE=${CONDOR_DIR_OUTPUT}/${JOBSUBJOBID}_dummy_output \n')
        f.write('touch ${DUMMY_OUTPUT_FILE} \n')
        f.write(' \n')
        f.write('# Copy datafiles \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/my_prueba.sh . \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/ToolAnalysis_ANNIEsoft_grid.tar.gz . \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/Run_Analyse_DD.py . \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/RunINFO.csv . \n')
        f.write(' \n')
        f.write('tar -xzf ToolAnalysis_ANNIEsoft_grid.tar.gz \n')
        f.write('rm ToolAnalysis_ANNIEsoft_grid.tar.gz \n')
        f.write('ls -lrt  > /srv/log_001.log \n')
        f.write(' \n')
        f.write('# Moving stuff \n')
        f.write('mv my_prueba.sh ToolAnalysis_ANNIEsoft_grid/ \n')
        f.write('mv RunINFO.csv ToolAnalysis_ANNIEsoft_grid/ \n')
        f.write('mv Run_Analyse_DD.py ToolAnalysis_ANNIEsoft_grid/ \n')
        f.write(' \n')
        f.write('cd ToolAnalysis_ANNIEsoft_grid \n')
        f.write('echo $CONDOR_DIR_INPUT > path_file.txt \n')
        f.write('echo $CONDOR_DIR_INPUT  > log_path_0.log  \n')
        f.write('cat ToolAnalysis_ANNIEsoft_grid/path_file.txt  > log_path.log  \n')
        f.write('singularity exec -B/srv:/srv,${CONDOR_DIR_INPUT},${PWD}:/ToolAnalysisGrid /cvmfs/singularity.opensciencegrid.org/anniesoft/toolanalysis\:latest/ $CONDOR_DIR_INPUT/my_prueba.sh $1 \n')
        f.write(' \n')
        f.write('echo "Moving the output files to CONDOR OUTPUT:" >> ${DUMMY_OUTPUT_FILE} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *.status ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *.root ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D ProcessedRawData_* ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D TrigOverlap_* ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *_beamdbr ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D *.log ${CONDOR_DIR_OUTPUT} \n')
        f.write('${JSB_TMP}/ifdh.sh cp -D /srv/*.log ${CONDOR_DIR_OUTPUT} \n')
        f.write(' \n')
        f.write('echo "Cleaning up:" >> ${DUMMY_OUTPUT_FILE} \n')
        f.write('cd .. \n')
        f.write('rm /srv/my_prueba.sh \n')
        f.write('rm -rf ToolAnalysis_ANNIEsoft_grid/ \n')
        f.write('## END ## \n')

# Given a number makes a subset of arrays with `subset_length` elements
def divide_into_subsets(num, subset_length):
    subsets = []
    start = 0
    subset_length = (subset_length - 1) # because it starts with 0
    print('\033[91m'+'                   Each subset will have '+str(subset_length+1)+' RawData file'+'\033[0m')
    while start <= (num - 1):
        end = min(start + subset_length, (num-1)) 
        subsets.append(list(range(start, end+1)))
        print(start,end)
        start = end + 1
    return subsets

# makes the scritp excecutable and it run
def send_to_grid(subset, total_file, run_number):
    submit_script_subset(subset, total_file, run_number)
    os.system('chmod +x ./submit_job.sh')
    #os.system('cat ./submit_job.sh') 
    print('\033[94m'+'The submit_job.sh file was create and it will be source it ..................................' + '\033[0m')
    #os.system('./submit_job.sh') 

def send_to_grid_lappd(subset, total_file, run_number):
    submit_script_subset_lappd(subset, total_file, run_number)
    os.system('chmod +x ./submit_job.sh')
    #os.system('cat ./submit_job.sh') 
    print('\033[94m'+'The submit_job.sh file was create and it will be source it ..................................' + '\033[0m')
    os.system('./submit_job.sh') 

def send_individual_runs(nrun, subset_length):
    '''
    if len(sys.argv) < 2:
        print("ERROR: You need to add an the run number. Try like `python3 Run_Analyse_MRD.py 4197` ")
        sys.exit(1)
    else:
        print('\033[93m' + '***************************************************************************' + '\033[0m')
        print('\033[93m' + '                ANNIE will send jobs to the grid' + '\033[0m')
        print('\033[93m' + '***************************************************************************' + '\033[0m')

    nrun = int(sys.argv[1])
    '''
    print('\033[93m' + '***************************************************************************' + '\033[0m')
    print('\033[93m' + '                ANNIE will send jobs to the grid' + '\033[0m')
    print('\033[93m' + '***************************************************************************' + '\033[0m')


    path = '/pnfs/annie/persistent/raw/raw/'+str(nrun)+'/'
    file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    
    information = "                        RUN "+str(nrun)+", "+str(file_count) + " RawData file"
    print('\033[91m' + information + '\033[0m')

    subsets = divide_into_subsets(file_count, subset_length)

    for i in range(0,len(subsets)):
        sub_list = subsets[i]
        print('The subset ',i, 'of run ',nrun, ': ', sub_list) 
        #send_to_grid(sub_list, file_count, nrun)
        send_to_grid_lappd(sub_list, file_count, nrun)

    print('\x1b[6;30;42m' + 'The jobs were sent successfully!' + '\x1b[0m')

def main():
    input_string = input("Enter values separated by a comma and inside of quotation marks like '4210,4213': ")
    values = input_string.split(",")
    my_list = [int(val) for val in values]  # convert values to integers
    input_length = input("Enter the length of each subset: ")
    subset_length = int(input_length)
    #make_send_script_lappd()
    for i in my_list:
        send_individual_runs(i, subset_length)

if __name__ == "__main__":
    main()
