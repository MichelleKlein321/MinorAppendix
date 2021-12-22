
import os
import fnmatch

svfiles = []
folderlist = []

def performAnalysis(options):
    outFile = open(options.outf, "w")

    # Search through directories to find files containing 'tumor-control_filtered_germlineStrict' in the name
    for root, dirs, files in os.walk('/icgc/dkfzlsdf/project/OE0290/StJudeCloud_Validation/sequencing/whole_genome_sequencing/view-by-pid'):
        for file in files:
            if fnmatch.fnmatch(file, '*tumor00-control00_filtered_germlineStrict*'):
                folderlist.append(os.path.join(root, file))

    # Generate a header for the output file
    for i in folderlist:
        InputFile = open(i, 'r')
        for line in InputFile:
            if line.startswith('#'):
                headers = line

    # Add 'SampleID' to the header on the first position and write the header to the output file
    header = headers.split('\t')
    header.insert(0, 'SampleID')
    outFile.write(",".join(header))

    # Determine the samplenames/IDs of each line bu looking up the name of the input files
    # Extract this name and safe as SampleName
    for i in folderlist:
        InputFile = open(i, 'r')
        Name = str(i)
        FileName = Name.split('/')
        Name = FileName[14]
	print(Name)
        NameSplit = Name.split('_')
        SampleName = NameSplit[4]
        # # Skip headers of the input files
        for line in InputFile:
            if line.startswith('#'):
                continue
            # Split each line, skip the line if the event score is below 3
            s =  line.split('\t')
            if s[9] < '3':
                continue

            # Add samplename to the lines on the first position
            s.insert(0, SampleName)
            print(s)

            # Change all the , to _ to be able to write it properly to the outfile
            s[17] = s[17].replace(",", "_")
            s[18] = s[18].replace(",", "_")
            s[19] = s[19].replace(",", "_")
            s[20] = s[20].replace(",", "_")
            s[21] = s[21].replace(",", "|")
            s[22] = s[22].replace(",", "_")
            s[23] = s[23].replace(",", "_")
            s[24] = s[24].replace(",", "_")
            s[25] = s[25].replace(",", "_")
            s[26] = s[26].replace(",", "_")
            s[27] = s[27].replace(",", "_")
            s[28] = s[28].replace(",", "_")
            s[29] = s[29].replace(",", "_")
            s[30] = s[30].replace(",", "_")
            s[31] = s[31].replace(",", "|")
            s[32] = s[32].replace(",", "_")
            s[33] = s[33].replace(",", "_")
            s[34] = s[34].replace(",", "_")
            s[35] = s[35].replace(",", "_")
            s[36] = s[36].replace(",", "_")
            s[37] = s[37].replace(",", "_")
            s[38] = s[38].replace(",", "_")
            s[39] = s[39].replace(",", "_")
            s[40] = s[40].replace(",", "_")
            s[41] = s[41].replace(",", "_")
            s[42] = s[42].replace(",", "_")
            s[43] = s[43].replace(",", "_")
            s[44] = s[44].replace(",", "_")
            s[45] = s[45].replace(",", "_")
            s[46] = s[46].replace(",", "_")
            s[47] = s[47].replace(",", "_")
            s[48] = s[48].replace(",", "_")
            s[49] = s[49].replace(",", "_")
            s[50] = s[50].replace(",", "_")
            s[51] = s[51].replace(",", "_")
            s[52] = s[52].replace(",", "_")
            s[53] = s[53].replace(",", "_")
            s[54] = s[54].replace(",", "_")
            s[55] = s[55].replace(",", "_")
            s[56] = s[56].replace(",", "_")
	    s[57] = s[57].replace(",", "_")


            outFile.write(",".join(s))
    outFile.close()

if __name__ == '__main__':
    print("Starting analysis...\n")
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--outf',action='store',type='string',dest='outf',help='Specify the name of the output file',default='')

    (options,args) = parser.parse_args()

    performAnalysis(options)
    print("\nDone....")
