def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")
    input = options.input

    Burden_Genes = []
    Result = []

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

    for i in compare:
        Result.append(i)
    Result = list(map(lambda s: s.strip(), Result))

    # The input results in the right output result (exon --> Exon, intron --> Intron)
    # But only if the gene in the burden output file is the same as the gene in the list from script 1

    if input == 'Gene1_exon':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Exon")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    if input == 'Gene1_intron':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Intron")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    if input == 'Gene1_intron_fusion':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Intron_fusion")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    if input == 'Gene2_exon':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Exon")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    if input == 'Gene2_intron':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Intron")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")

    if input == 'Gene2_intron_fusion':
        Update_Burden_file = []

        for i in Burden_Genes:
            for j in Result:
                if i[1] == j:
                    i[0].append("Intron_fusion")
            Update_Burden_file.append(i[0])

        for i in Update_Burden_file:
            i = str(i)
            outfile.write(i+ "\n")


if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')
    parser.add_option('--input', action='store', type='string', dest='input', help='Gene1_exon, Gene1_intron, Gene2_exon, Gene2_intron', default='')

    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")

    performAnalysis(options)
    print("\nDone....")
