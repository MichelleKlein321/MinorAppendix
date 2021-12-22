def striplist(l):
    return([x.strip() for x in l])
#
def listToTabSep(listItems, sep='\t'):
    return sep.join(listItems)

def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")
    input = options.input

    Gene = []
    for line in compare:
        Gene.append(line)
    Gene = list(map(lambda s: s.strip(), Gene))

    if input == 'Gene1_exon' or input == 'Gene1_intron':

        for line in infile:
            if line.startswith('SampleID'):
                outfile.write(line)
                continue
            Test = line.split(",")
            Test[19] = Test[19].replace('"','')
            Test[19] = Test[19].strip()
            for i in Gene:
                if i == Test[19]:
                    outfile.write(line)

        infile.close()
        compare.close()
        outfile.close()

    if input == 'Gene2_exon' or input == 'Gene2_intron':

        for line in infile:
            if line.startswith('SampleID'):
                outfile.write(line)
                continue
            Test = line.split(",")
            Test[29] = Test[29].replace('"','')
            Test[29] = Test[29].strip()
            for i in Gene:
                #print(i, Test[19])
                if i == Test[29]:
                    outfile.write(line)

        infile.close()
        compare.close()
        outfile.close()


if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')
    parser.add_option('--input', action='store', type='string', dest='input', help='Gene1_exon, Gene1_intron, Gene2_exon, Gene2_intron', default='')

    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")
    # if len(options.outf) <1 or len(options.inf) <1:
    #     print("Wrong")
    #     print("Parameter settings")
    #     print(options)
    performAnalysis(options)
    print("\nDone....")
