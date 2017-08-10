#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: sejalmodha
"""
#import OS module to use os methods and functions
import os
import subprocess
import sys
import re
# you'll see this alias in documentation, examples, etc.
import pandas as pd
#import biopython SeqIO
from Bio import SeqIO

#set present working directory
if len(sys.argv) > 1:
    cwd = sys.argv[1]
else:
    cwd=os.getcwd()
#os.chdir(pwd)

print(cwd)

#get the current working directory 
os.chdir(cwd)
print(os.getcwd())
#function to process ftp url file that is created from assembly files
def process_url_file(inputurlfile):
    url_file=open(inputurlfile,'r')
    file_suffix=r'genomic.gbff.gz'
    for line in url_file:
        url=line.rstrip('\n').split(',')
        ftp_url= url[0]+'/'+url[1]+'_'+url[2]+'_'+file_suffix
        #print(new_url)
        print("Downloading"+ ftp_url)
        #Download the files in the gbff format
        subprocess.call("wget "+ftp_url,shell=True) 
        #unzip the files
        
    return

#function to download bacterial sequences
def download_bacterial_genomes(outfile='outfile.txt'):
    assembly_summary_file=r'ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt'
    if os.path.exists('assembly_summary.txt'):
       os.remove('assembly_summary.txt')
    #Download the file using wget sysyem call
    subprocess.call("wget "+assembly_summary_file, shell=True)
    #Reformat the file to pandas-friendly format
    subprocess.call("sed -i '1d' assembly_summary.txt",shell=True)
    subprocess.call("sed -i 's/^# //' assembly_summary.txt", shell=True)
    #Read the file as a dataframe - using read_table
    #Use read_table if the column separator is tab
    assembly_sum = pd.read_table('assembly_summary.txt')
    #filter the dataframe and save the URLs of the complete genomes in a new file
    my_df=assembly_sum[(assembly_sum['version_status'] == 'latest') &
                   (assembly_sum['assembly_level']=='Complete Genome') 
                  ]
    my_df=my_df[['ftp_path','assembly_accession','asm_name']]
    #output_file.write
    my_df.to_csv(outfile,mode='w',index=False,header=None)
    process_url_file(outfile)
    return
     
#function to download reference genomes 
#this function downloads latest version human reference genome by default 
def download_refseq_genome(taxid=9606,outfile='refseq_genome.txt'):
    assembly_summary_file="ftp://ftp.ncbi.nih.gov/genomes/refseq/assembly_summary_refseq.txt"
    if os.path.exists('assembly_summary_refseq.txt'):
        os.remove('assembly_summary_refseq.txt')
    #Download the file using wget sysyem call
    subprocess.call("wget "+assembly_summary_file, shell=True)
    #Reformat the file to pandas-friendly format
    subprocess.call("sed -i '1d' assembly_summary_refseq.txt",shell=True)
    subprocess.call("sed -i 's/^# //' assembly_summary_refseq.txt", shell=True)
    #Read the file as a dataframe - using read_table
    #Use read_table if the column separator is tab
    assembly_sum = pd.read_table('assembly_summary_refseq.txt')
    my_df=assembly_sum[(assembly_sum['taxid'] == taxid) &
                       ((assembly_sum['refseq_category'] == 'reference genome') |
                        (assembly_sum['refseq_category'] == 'representative genome')
                       )]
    my_df=my_df[['ftp_path','assembly_accession','asm_name']]
    #Process the newly created file and download genomes from NCBI website
    my_df.to_csv(outfile,mode='w',index=False,header=None)
    process_url_file(outfile)
    return


print('Downloading human genome'+'\n')
#change argument in the following function if you want to download other reference genomes
#taxonomy ID 9606 (human) should be replaced with taxonomy ID of genome of interest
download_refseq_genome(9606,'human_genome_url.txt')


print('Downloading rat genome'+'\n')
download_refseq_genome(10116,'rat_genome_url.txt')


print('Downloading bacterial genomes'+'\n')
download_bacterial_genomes('bacterial_complete_genome_url.txt')

subprocess.call(wget ftp://ftp.ncbi.nlm.nih.gov/refseq/release/archaea/archaea.*.genomic.gbff.gz)
subprocess.call(wget ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.*.genomic.gbff.gz)
subprocess.call(wget ftp://ftp.ncbi.nlm.nih.gov/refseq/release/plasmid/plasmid.*.genomic.gbff.gz)
subprocess.call(gunzip *.gz)