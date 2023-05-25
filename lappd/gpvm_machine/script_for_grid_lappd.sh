#!/bin/bash
#  Based on /annie/app/users/dingpf/GridSub_test.sh
#  Copied from James Minock

cat <<EOF
condor   dir: $CONDOR_DIR_INPUT
process   id: $PROCESS
output   dir: $CONDOR_DIR_OUTPUT
EOF

HOSTNAME=$(hostname -f)
GRIDUSER="mascenci"

echo "Job starting on $(uname -a)"

DUMMY_OUTPUT_FILE=${CONDOR_DIR_OUTPUT}/${JOBSUBJOBID}_dummy_output
touch ${DUMMY_OUTPUT_FILE}

# Copy datafiles
${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/script_for_singularity.sh .
${JSB_TMP}/ifdh.sh cp -D $CONDOR_DIR_INPUT/ToolAnalysis_ANNIEsoft_grid.tar.gz .

tar -xzf ToolAnalysis_ANNIEsoft_grid.tar.gz
rm ToolAnalysis_ANNIEsoft_grid.tar.gz
ls -lrt  > /srv/log_001.log

# Moving stuff
mv script_for_singularity.sh ToolAnalysis_ANNIEsoft_grid/

cd ToolAnalysis_ANNIEsoft_grid
echo $CONDOR_DIR_INPUT > path_file.txt
cat ToolAnalysis_ANNIEsoft_grid/path_file.txt  > log_path.log
#singularity exec -B/srv:/srv,${CONDOR_DIR_INPUT},${PWD}:/ToolAnalysisGrid /cvmfs/singularity.opensciencegrid.org/anniesoft/toolanalysis\:latest/ $CONDOR_DIR_INPUT/script_for_singularity.sh $1 $2 $3
singularity exec -B/srv:/srv,${CONDOR_DIR_INPUT},${PWD}:/ToolAnalysisGrid /cvmfs/singularity.opensciencegrid.org/anniesoft/toolanalysis\:latest/ $CONDOR_DIR_INPUT/script_for_singularity.sh $1 $2 $3

echo "Moving the output files to CONDOR OUTPUT:" >> ${DUMMY_OUTPUT_FILE}
${JSB_TMP}/ifdh.sh cp -D *.root ${CONDOR_DIR_OUTPUT}
${JSB_TMP}/ifdh.sh cp -D ProcessedRawData_* ${CONDOR_DIR_OUTPUT}
${JSB_TMP}/ifdh.sh cp -D *.log ${CONDOR_DIR_OUTPUT}
${JSB_TMP}/ifdh.sh cp -D /srv/*.log ${CONDOR_DIR_OUTPUT}

echo "Cleaning up:" >> ${DUMMY_OUTPUT_FILE}
cd ..
rm /srv/script_for_singularity.sh
rm -rf ToolAnalysis_ANNIEsoft_grid/
## END ##
