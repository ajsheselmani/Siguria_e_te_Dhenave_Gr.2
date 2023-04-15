if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Book Cipher')

    required = parser.add_argument_group('required arguments')

    required.add_argument('-m', '--mode', choices=['encipher', 'e', 'decipher', 'd'],

                          help='Mode: encipher or decipher', required=True, dest='mode')


    required.add_argument("-b", "--bookfilename",

                          help="Book filename", required=True, dest='bookfilename')


    required.add_argument("-i", "--inputfilename",

                          help="Input file to be processed", required=True, dest='inputfilename')


    required.add_argument("-o", "--outputfilename",

                          help="Output file to be created", required=True, dest='outputfilename')


    main(parser.parse_args())