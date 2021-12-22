def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")
    input = options.input

    # Choice of input is necessary for the Update_Burden_file script, whether you want
    # SampleIDs added (input == 'ID') or just the fact that there is a mutation (input == 'Germline' or 'Somatic')

    if input == 'Germline' or input == 'Somatic':

    # Empty list for all the genes extracted from the input file
        final_list = []

        # This step extracts the Gene names out of the input vcf file and add it to a Gene_list
        for lines in infile:

            Gene_list = []
            if lines.startswith('#'):
                continue
            line = lines.split("\t")
            # In some files, not the full line is available and therefore the gene name is in a different location
            if len(line) > 14:
                print(line)
                Genes = line[16]
                Genes = Genes.split(',')
                print(Genes)

                # Some files contain 1, 2 or more genes, besides the format differs
                # It can either be 'Gene', 'Gene;Gene' or 'Gene(ENSG*)'
                # from all possible formats an attempt has been made to filter the gene name

                # if len == 1
                if len(Genes) == 1:

                    # If Gene name contains '('
                    if '(' in Genes[0]:
                        # AND Gene name contains ';'
                        if ';' in Genes[0]:
                            Genes = Genes[0]
                            Genes = Genes.split(';')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                        else:
                            Genes = Genes[0]
                            Genes = Genes.split('(')
                            Genes = Genes[0]
                            Gene_list.append(Genes)

                    # Gene name does not contain '(' and len == 1
                    else:
                        for i in Genes:
                            i = i.replace('"', "")
                            Gene_list.append(i)

                # if len > 1
                else:

                    # If Gene name contains '('
                    if '(' in Genes[0]:
                        # AND Gene name contains ';'
                        if ';' in Genes[0]:
                            Genes = Genes[0]
                            Genes = Genes.split(';')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                        else:
                            Genes = Genes[0]
                            Genes = Genes.split('(')
                            Genes = Genes[0]
                            Gene_list.append(Genes)

                    # Gene name does not contain '(' and len > 1
                    else:
                        for i in Genes:
                            i = i.replace('"', "")
                            Gene_list.append(i)

            # When not the full line is available
            else:
                Genes = line[7]
                Genes = Genes.split('|')
                Genes = Genes[3]
                Gene_list.append(Genes)


            # To make sure that every gene name is added in the list.
            # Sometimes more gene names are mentioned in the input vcf file
            Indel_Gene_list = []
            if len(Gene_list) == 1:
                Indel_Gene_list.append(Gene_list[0])
            elif len(Gene_list) == 2:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
            elif len(Gene_list) == 3:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
                Indel_Gene_list.append(Gene_list[2])
            elif len(Gene_list) == 4:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
                Indel_Gene_list.append(Gene_list[2])
                Indel_Gene_list.append(Gene_list[3])

            # add all unique gene names to the final list --> no duplicates
            if Indel_Gene_list not in final_list:
                final_list.append(Indel_Gene_list)

        # Exracts all the gene names of the burden output file
        Burden_Genes = []
        for i in compare:
            if i.startswith('GENE'):
                continue
            Burden_line = i.split("\t")
            Burden_Genes.append(Burden_line[0])


        # To make a final gene list containing only unique gene names
        # present in both input vcf file as in burden output file
        Genes_result = []
        for i in final_list:
            for j in Burden_Genes:
                if len(i) == 1:
                    if i[0] == j:
                        Genes_result.append(i[0])
                if len(i) == 2:
                    if i[0] == j:
                        Genes_result.append(i[0])
                    if i[1] == j:
                        Genes_result.append(i[1])
                if len(i) == 3:
                    if i[0] == j:
                        Genes_result.append(i[0])
                    if i[1] == j:
                        Genes_result.append(i[1])
                    if i[2] == j:
                        Genes_result.append(i[2])
                if len(i) == 4:
                    if i[0] == j:
                        Genes_result.append(i[0])
                    if i[1] == j:
                        Genes_result.append(i[1])
                    if i[2] == j:
                        Genes_result.append(i[2])
                    if i[3] == j:
                        Genes_result.append(i[3])

        # Saves the generated Gene_result list in the outfile
        for i in Genes_result:
            outfile.write(i + '\n')


    if input == 'ID':

    # Empty list for all the genes extracted from the input file
    # And adds the sample name to the same list
        final_list = []

        for lines in infile:
            Gene_list = []
            if lines.startswith('##'):
                continue
            if lines.startswith('#'):
                lines = lines.split("\t")
                #print(lines)
                # index = lines.index("SampleID")
                continue

            line = lines.split("\t")

            # In some files, not the full line is available and therefore the gene name is in a different location
            if len(line) > 14:
                Genes = line[16]
                Genes = Genes.split(',')

                # Some files contain 1, 2 or more genes, besides the format differs
                # It can either be 'Gene', 'Gene;Gene' or 'Gene(ENSG*)'
                # from all possible formats an attempt has been made to filter the gene name

                # if len == 1
                if len(Genes) == 1:
                    # If Gene name contains '('
                    if '(' in Genes[0]:
                        # AND Gene name contains ';'
                        if ';' in Genes[0]:
                            Genes = Genes[0]
                            Genes = Genes.split(';')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                            lines = lines.split("\t")
                            Gene_list.append(lines[len(lines)-2])
                        else:
                            Genes = Genes[0]
                            Genes = Genes.split('(')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                            lines = lines.split("\t")
                            Gene_list.append(lines[len(lines)-2])

                    # Gene name does not contain '(' and len == 1
                    else:
                        for i in Genes:
                            i = i.replace('"', "")
                            Gene_list.append(i)
                            lines = lines.split("\t")
                            Gene_list.append(lines[len(lines)-2])

                # if len > 1
                else:
                    # If Gene name contains '('
                    if '(' in Genes[0]:
                        # AND Gene name contains ';'
                        if ';' in Genes[0]:
                            Genes = Genes[0]
                            Genes = Genes.split(';')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                            lines = lines.split("\t")
                            Gene_list.append(lines[len(lines)-2])
                        else:
                            Genes = Genes[0]
                            Genes = Genes.split('(')
                            Genes = Genes[0]
                            Gene_list.append(Genes)
                            lines = lines.split("\t")
                            Gene_list.append(lines[len(lines)-2])

                    # Gene name does not contain '(' and len > 1
                    else:
                        lines = lines.split('\t')
                        for i in Genes:
                            i = i.replace('"', "")
                            Gene_list.append(i)
                            Gene_list.append(lines[-2])

            # When not the full line is available
            else:
                Genes = line[7]
                Genes = Genes.split('|')
                Genes = Genes[3]
                Gene_list.append(Genes)
                Gene_list.append('NA')


            # To make sure that every gene name is added in the list.
            # Sometimes more gene names are mentioned in the input vcf file
            Indel_Gene_list = []
            if len(Gene_list) == 2:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
            elif len(Gene_list) == 3:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
                Indel_Gene_list.append(Gene_list[2])
            elif len(Gene_list) == 4:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
                Indel_Gene_list.append(Gene_list[2])
                Indel_Gene_list.append(Gene_list[3])
            elif len(Gene_list) == 5:
                Indel_Gene_list.append(Gene_list[0])
                Indel_Gene_list.append(Gene_list[1])
                Indel_Gene_list.append(Gene_list[2])
                Indel_Gene_list.append(Gene_list[3])
                Indel_Gene_list.append(Gene_list[4])

            # add all unique gene names to the final list --> no duplicates
            if Indel_Gene_list not in final_list:
                final_list.append(Indel_Gene_list)

        # Exracts all the gene names of the burden output file
        Burden_Genes = []
        for i in compare:
            if i.startswith('GENE'):
                continue
            Burden_line = i.split("\t")
            Burden_Genes.append(Burden_line[0])

        # To make a final gene list containing only unique gene names and the SampleID
        # present in both input vcf file as in burden output file
        Genes_result = []
        for i in final_list:
            for j in Burden_Genes:
                if len(i) == 2:
                    if i[0] == j:
                        Genes_result.append(i[0]+',' + i[1])
                if len(i) == 3:
                    if i[0] == j:
                        Genes_result.append(i[0]+',' + i[1])
                    if i[1] == j:
                        Genes_result.append(i[1]+',' + i[2])
                if len(i) == 4:
                    if i[0] == j:
                        Genes_result.append(i[0]+',' + i[1])
                    if i[1] == j:
                        Genes_result.append(i[1]+',' + i[2])
                    if i[2] == j:
                        Genes_result.append(i[2]+',' + i[3])
                if len(i) == 5:
                    if i[0] == j:
                        Genes_result.append(i[0]+',' + i[1])
                    if i[1] == j:
                        Genes_result.append(i[1]+',' + i[2])
                    if i[2] == j:
                        Genes_result.append(i[2]+',' + i[3])
                    if i[3] == j:
                        Genes_result.append(i[3]+',' + i[4])

        # Saves the generated Gene_result list in the outfile
        for i in Genes_result:
            outfile.write(i + '\n')

if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')
    parser.add_option('--input', action='store', type='string', dest='input', help='Type or ID', default='')


    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")

    performAnalysis(options)
    print("\nDone....")
