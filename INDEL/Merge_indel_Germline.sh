#!/bin/sh           
#PBS -l mem=5g
#PBS -l ddisk=1gb
#PBS -l walltime=72:00:00
#PBS -l nodes=1:ppn=1
#PBS -j eo
#PBS -m ae
#PBS -o /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/logs
#PBS -e /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/logs
#PBS -M michelle01.klein@dkfz-heidelberg.de


cd /icgc/dkfzlsdf/project/pedbrain/pa/sequencing/whole_genome_sequencing/view-by-pid 
python /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/INDEL/Merge_indel_Germline.py --inf /b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/INDEL/Indel_header.csv --outf=/b06x-isilon/b06x-p/PanCanPredispo/2ndHitAnalysis/mklein/INDEL/indel_pa_germline.vcf


