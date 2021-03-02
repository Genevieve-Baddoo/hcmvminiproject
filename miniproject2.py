#import Biopython modules needed
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO

Entrez.email = "gbaddoo@luc.edu"
#recieve record for EF999921
handle = Entrez.efetch(db="nucleotide", id="EF999921", rettype="gb")
records = list(SeqIO.parse(handle, "gb"))

#current list has one item in record. Create 2 output files.
recs = records[0] #start at first item
#add count to record # of CDS sequences
count = 0
#create two outputfiles
#write to outputfiles
outputfile = open("miniProject.log", "w") 
fastafile = open("CDS_EF999921.fasta","w")

#want to pull out the CDS reads
for feature in recs.features:
    if feature.type == "CDS":
        #count # of CDS reads
        count = count+1
        #get CDS and write to fasta file
        seqcds = feature.location.extract(recs).seq
        #print(seqcds)
        fastafile.write(">HCMV" + str(count) + "\n")
        fastafile.write(str(seqcds) + "\n")
        
#write in log file the CDS count
outputfile.write("The HCMV genome (EF99921) has " + str(count) + " CDS." + "\n")    
outputfile.close() #close both files
fastafile.close()
