#!/bin/sh           
#PBS -l mem=5g
#PBS -l ddisk=1gb
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=1
#PBS -j eo
#PBS -m ae
#PBS -o /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/logs
#PBS -e /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/logs
#PBS -M michelle01.klein@dkfz-heidelberg.de



python /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/SV/Merge_sv_Germline.py --outf=/b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/SV/sv_StJude_germline.csv


