def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")
    input = options.input

    # Choice of input is necessary to add SampleIDs to the burden file (input == 'ID') or only
    # the fact that there is a mutation (input == 'Germline or Somatic')

    Burden_Genes = []

    # Extract the genes in the burden output and add it to a list with the Burden output as well
    for i in infile:
        Burden_Gene_list = []
        if i.startswith('GENE'):
            continue
        Burden_line = i.split("\t")
        Gene = Burden_line[0]
        Burden_Gene_list.append(Burden_line)
        Burden_Gene_list.append(Gene)

        Burden_Genes.append(Burden_Gene_list)

    # if the input is germline or somatic, germline or somatic is added to the burden output file
    # But only if the gene in the burden output file is the same as the gene in the list from script 1

    if input == 'Germline' or input == 'Somatic':
        Genes = []
        for i in compare:
            Genes.append(i)
        Genes = list(map(lambda s: s.strip(), Genes))

        Update_Burden_file = []

        for i in Burden_Genes:
            Gene = []
            Gene.append(i[1])
            for j in Genes:
                if i[1] == j:
                    if input == 'Germline':
                        i[0].append("Germline")
                    if input == 'Somatic':
                        i[0].append("Somatic")
            Update_Burden_file.append(i[0])

        # Writes the new burden output to the output file
        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    # if the input is ID, the sampleID is added to the burden output file
    # But only if the gene in the burden output file is the same as the gene in the list from script 1

    if input == 'ID':
        GenesID = []
        Genes = []
        for i in compare:
            Genes.append(i)
        Genes = list(map(lambda s: s.strip(), Genes))

        for j in Genes:
            j = j.split(',')
            GenesID.append(j)

        Update_Burden_file = []

        for i in Burden_Genes:
            Gene = []
            Gene.append(i[1])
            for j in GenesID:
                if i[1] == j[0]:
                    i[0].append(j[1])
            Update_Burden_file.append(i[0])

        # Writes the new burden output to the output file
        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")



if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')
    parser.add_option('--input', action='store', type='string', dest='input', help='', default='')

    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")
    performAnalysis(options)
    print("\nDone....")
