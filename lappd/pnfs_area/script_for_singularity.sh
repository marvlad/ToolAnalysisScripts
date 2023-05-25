##------------------------------- Setup 0 -------------------------------- ##
cd /ToolAnalysisGrid/

##------------------------------- Setup 0_1 -------------------------------- ##
ln -s /ToolAnalysis/ToolDAQ /ToolAnalysisGrid/ToolDAQ

ls -lrt > /ToolAnalysisGrid/log_202.log

ToolDAQapp=/ToolAnalysisGrid

echo ${ToolDAQapp}

export LIBGL_ALWAYS_INDIRECT=1

source ${ToolDAQapp}/ToolDAQ/root-6.24.06/install/bin/thisroot.sh

export CLHEP_DIR=${ToolDAQapp}/ToolDAQ/2.4.0.2/CLHEP_install

export LD_LIBRARY_PATH=${ToolDAQapp}/lib:${ToolDAQapp}/lib:${ToolDAQapp}/ToolDAQ/zeromq-4.0.7/lib:${ToolDAQapp}/ToolDAQ/boost_1_66_0/install/lib:${ToolDAQapp}/ToolDAQ/root/lib:${ToolDAQapp}/ToolDAQ/WCSimLib/:${ToolDAQapp}/ToolDAQ/MrdTrackLib/src:${ToolDAQapp}/ToolDAQ/RATEventLib/lib/:${ToolDAQapp}/UserTools/PlotWaveforms:${ToolDAQapp}/ToolDAQ/log4cpp/lib:${ToolDAQapp}/ToolDAQ/Pythia6Support/v6_424/lib:${CLHEP_DIR}/lib:${ToolDAQapp}/ToolDAQ/LHAPDF-6.3.0/install/lib:${ToolDAQapp}/ToolDAQ/GENIE-v3-master/lib:${ToolDAQapp}/ToolDAQ/Reweight-3_00_04_ub3/lib:$LD_LIBRARY_PATH

export ROOT_INCLUDE_PATH=${ToolDAQapp}/ToolDAQ/WCSimLib/include/:${ToolDAQapp}/ToolDAQ/MrdTrackLib/include:${ToolDAQapp}/ToolDAQ/RATEventLib/include/:${ToolDAQapp}/UserTools/PlotWaveforms:$ROOT_INCLUDE_PATH

export PYTHIA6_DIR=${ToolDAQapp}/ToolDAQ/Pythia6Support/v6_424/
export LHAPATH=${ToolDAQapp}/ToolDAQ/LHAPDF-6.3.0/install/share/LHAPDF/
export GENIE=${ToolDAQapp}/ToolDAQ/GENIE-v3-master
export GENIE_REWEIGHT=${ToolDAQapp}/ToolDAQ/Reweight-3_00_04_ub3/

export PATH=${ToolDAQapp}/ToolDAQ/LHAPDF-6.3.0/install/bin:$GENIE/bin:$GENIE_REWEIGHT/bin:$PATH

export PATH=/ToolAnalysis/ToolDAQ/fsplit:$PATH
export TF_CPP_MIN_LOG_LEVEL=2

for folder in `ls -d ${ToolDAQapp}/UserTools/*/ `
do
    export PYTHONPATH=$folder:${PYTHONPATH}
done

ls -lrt > /ToolAnalysisGrid/log_203.log
##------------------------------- Setup 0_2 -------------------------------- ##

rm configfiles/loadLAPPDData/my_files.txt
ls -lrt > /ToolAnalysisGrid/list_ToolAnalysisGrid_dir.log

export var_new=$(cat /ToolAnalysisGrid/path_file.txt)
find $var_new -name "RAWDataR*" > /ToolAnalysisGrid/configfiles/loadLAPPDData/my_files.txt

cat /ToolAnalysisGrid/configfiles/loadLAPPDData/my_files.txt > /ToolAnalysisGrid/my_file_loadLAPPD.log

##------------------------------- Setup 0 -------------------------------- ##
/ToolAnalysisGrid/./Analyse Example1 > /ToolAnalysisGrid/example_1_out.log
/ToolAnalysisGrid/./Analyse configfiles/loadLAPPDData/ToolChainConfig > loadLAPPDData_run.log

mv RawDataWaveForms_2D.root RawDataWaveForms_2D_run_$1_files_$2_$3.root

cp /ToolAnalysisGrid/*.root /srv/

ls -lrt > /ToolAnalysisGrid/list_finishing.log
