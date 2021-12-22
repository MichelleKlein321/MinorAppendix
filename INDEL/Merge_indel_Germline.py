
import os
import fnmatch
import csv

#outFile = open('test.csv', "w")

svfiles = []
folderlist = []

def performAnalysis(options):
    infile = open(options.inf, "r")
    outFile = open(options.outf, "w")

    for root, dirs, files in os.walk('/icgc/dkfzlsdf/project/pedbrain/pa/sequencing/whole_genome_sequencing/view-by-pid'):
        for file in files:
            if fnmatch.fnmatch(file, '*germline_functional_indels_conf_8_to_10*'):
                folderlist.append(os.path.join(root, file))

       

    for i in folderlist:
        print i
        InputFile = open(i, 'r')
        Name = str(i)
        NameSplit = Name.split('/')
        SampleName = NameSplit[9]
        

        for line in InputFile:
            if line[0] == '#':
                continue

            s =  line.split('\t')
            s.insert(42, SampleName)

	    outFile.write("\t".join(s))
    #outFile.close()
#
#
if __name__ == '__main__':
    print("Starting analysis...\n")
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf',action='store',type='string',dest='inf',help='Specify the name of the output file',default='')
    parser.add_option('--outf',action='store',type='string',dest='outf',help='Specify the name of the output file',default='')

    (options,args) = parser.parse_args()

    performAnalysis(options)
    print("\nDone....")
