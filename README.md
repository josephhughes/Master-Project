# Scripts: A Walkthrough

## dBScripts
The directory dBScripts contains scripts which create databases for each classifier.

### Kraken

Invoking the command "python ratKrakDBCreationScript.py" will automatically create a Kraken database
with the name HumanVirusBacteriaRat. It is best to run this command within a separate directory which
has already been named appropriately (i.e.: I typically run this command once I have created
a directory called "KrakDB"). 
This script will create an arachael genome, human genome, bacterial genome, viral genome and rat genome

In order to run Kraken on specific sequences, invoke the following command:

Without explanation:

kraken --preload --threads 12 --fastq-input --paired --db <$DIR_DB> sample1.R1.fq sample2.R2.fq

With explanation:

kraken --preload (preloads database) --threads 12 (number of threads) --fastq-input (remove for fa/fasta files) --paired (remove if not paired) --db <$DIR_DB> (replace <$DIR_DB> with database that you have made (i.e.: mine is HumanVirusBacteriaRat) sample1.R1.fq sample2.R2.fq

In order to store output, you could either create a bash script and concatenante the output: (i.e.: KrakenClassificationScript.sh > KrakenOutput.txt) or simply concatenate the command itself: 
kraken --preload --threads 12 --fastq-input --paired --db <$DIR_DB> sample1.R1.fq sample2.R2.fq > KrakenOutput.txt


### Kaiju

Invoking the command 'makeDB.sh -e -v -t 12' will automatically create a Kaiju database. The name of
the database is not relevant as it is not included within the commands to query the database.
It is best to run this command within a separate directory which has already been named 
appropriately (i.e.: I typically run this command once i Have created a directory called 
"kaijudb".)

The script will create arachael genome, human genome, bacterial genome and viral genome. The
rat genome still has to be incorporated. 

VITAL: YOU MUST COPY ALL CONTENTS FROM THE BIN IN THE ORIGINAL DOWNLOAD TO YOUR WD BEFORE THIS SCRIPT WILL WORK (/home4/rich01e/kaiju/bin).


### CLARK

CLARK must be told what genomes/reference sequences you would like to use in order to classify reads of interest. 
This can be done using the command "set_targets.sh <$DIR_DB> human viruses bacteria custom".
The command custom allows for the selection of a genome or reference sequence of your choosing (it references the custom folder). 

<$DIR_DB> can be replaced with whatever you would like to name the database directory (I've named this one DBDirectory).

In order to include any reference sequence, simply download the sequence, add it to the custom folder, and rename it to the taxonomic ID (as appears on the NCBI website). THIS MUST BE DONE
BEFORE YOU RUN THE PREVIOUS COMMAND.

==NORMAL CLASSIFCATION==

In order to run a normal classification, CLARK must first generate a database of specific sized k-mers. Here, only the default size has been used (31-mers). The database can be created by simply invoking the
main CLARK classification command as follows (CLARK.exe is located in the exe subdirectory of the main CLARK folder):

Without explanation:

CLARK -T <$DIR_DB>/targets.txt -D <£DIR_DB> -P samples.L.txt samples.R.txt -R <$RESULTS_DIR> -m 0 -n 12 --extended

With explanation:

CLARK -T <$DIR_DB>/targets.txt -D <£DIR_DB> -P (or -O sample.fa for non-paired-end reads) samples.L.txt samples.R.txt -R <$RESULTS_DIR> (replace <$RESULTS_DIR> with wherever you want to keep these results) -m 0 (-m 0 is full mode (more results), use -m 2 for express mode) -n 12 (number of threads) --extended (more results)

The targets.txt file is generated by the initial "set_targets.sh" command and is located in the <$DIR_DB>

==METAGENOMICS==
In order to run metagenomic classification you must invoke the command "classify_metagenome.sh -O (or -P for paired-reads) sample.fa (or "samples.L.txt samples.R.txt" if using paired reads) -R <$RESULTS_DIR> -m 0 -n 8.

==PAIRED-READS==
Paired-read command example:
PAIRED-READS
samples.L.txt MUST CONTAIN ALL R1 READS IN CORRECT ORDER
samples.R.txt MUST CONTAIN ALL R2 READS IN CORRECT ORDER

Example:
samples.L.txt would contain:
sample1.R1.txt
sample2.R1.txt
sample3.R1.txt

samples.R.txt would contain:
sample1.R2.txt
sample2.R2.txt
sample3.R3.txt

------------------------------------------------------------------------------------
## rScripts
The directory rScripts contains scripts which utilise data downloaded by scripts in the 
ncbiScripts directory - curates & generates figures & RMarkdown.

VITAL: PAY ATTENTION TO VARIABLES NAMES, THEY MUST BE EXACTLY AS NAMED IN THE RSCRIPT OR
IT WILL NOT WORK!

### FigureGen.R

This R script curates all downloaded metadata from the ncbiScripts and generates a fair
amount of figures based upon that data.

Figures include platform abundance, organism abundance, platform utilisation over time (bases
per year), rat sample wordcloud.


### SRACharMarkdown.RMD

This generates an RMarkdown document to your liking. Can be modified to include whichever 
figures take the user's fancy. At this moment in time includes all relevant figures. Please
run the FigureGen.R before attempting to render the RMarkdown document, all figures must be
generated at least once beforehand.

----------------------------------------------------------------------------------
## ncbiScripts
The directory ncbiScripts contains scripts which download all metadata from every dataset
on the SRA (fixScript.pl) as well as scripts which return correct taxonomic classification
for every taxonomic ID given from the original metadata.

VITAL: YOU MUST FIRST GENERATE A LIST OF TAXONOMIC IDS FROM THE METADATA DOWNLOADED VIA
fixScript.pl, A TUTORIAL ON HOW TO DO SO EXISTS IN FigureGen.R, INCLUDES ALL NECESSARY CODE.

### fixScript.pl

This script downloads all metadata necessary from every single dataset on the SRA. Metadata
includes ID, organism common name & scientific name, organism taxonomic ID, sample information,
creation date and update date, platform model used, generic platform name, number of bases,
study title, and study description. 

Generates text file named to your liking, merely invoke 'fixScript.pl > "filename".txt'

### taxScript.pl

This script returns taxonomic names based upon a text file with provided taxonomic IDs.
Taxonomic IDs must be separated via a newline character. IDs are read in as an array.


