import argparse, sys

###### Counting logic ######


def process_chunk(chunk):
    print (str(chunk))


#######  Glue logic and convenience code ###########

parser = argparse.ArgumentParser(description="Python number counting script. run with --file to provide file to read.")
parser.add_argument("--file")
args, leftovers = parser.parse_known_args()

input_file = sys.stdin if args.file is None else open(args.file, mode="rb")

# Process file in 1MB chunks
while True:
    piece = input_file.read(1024)
    if not piece:
        break
    process_chunk(piece)



