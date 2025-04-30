import argparse, sys, pickle, os, glob
import tempfile
from collections import defaultdict
import numpy
TEMPDIR = os.path.join(os.getcwd(), "frequencies")

BIN_COUNT = 1000

def bin_id_2_filename(bin_id):
    return os.path.join(TEMPDIR, f"{bin_id}.pickle")

def get_bin_data(bin_id):
    if os.path.exists(bin_id_2_filename(bin_id)):
        # Load already counted frequencies
        return pickle.load(open(bin_id_2_filename(bin_id), "rb"))
    else:
        # Empty
        return {}

def store_bin_data(bin_id, bin_counts):
    with open(bin_id_2_filename(bin_id), "wb") as output_file:
        pickle.dump(bin_counts, output_file)



def chunk_cruncher(array):
    uniq= numpy.unique_counts(array)
    current_bins = defaultdict(lambda: defaultdict(lambda: 0))

    for value, count in zip(uniq.values.astype(int).tolist(), uniq.counts.astype(int).tolist()):
        bin_id = value % BIN_COUNT
        current_bins[bin_id][value] = count

    for bin_id in current_bins.keys():
        bin_contents = get_bin_data(bin_id)
        if bin_contents:
            for value, count in current_bins[bin_id].items():
                 if value in bin_contents:
                     bin_contents[value] += count
                 else:
                     bin_contents[value] = count

        else:
            bin_contents = dict(current_bins[bin_id])
        store_bin_data(bin_id, bin_contents)


#######  Glue logic and convenience code ###########

def count_frequencies_from_input_and_store_bins():

    # Cleanup cache
    for filename in glob.glob(os.path.join(TEMPDIR, "*.pickle")):
        os.unlink(filename)

    os.makedirs(TEMPDIR, exist_ok=True)

    parser = argparse.ArgumentParser(
        description="Python number counting script. run with --file to provide file to read.")
    parser.add_argument("--file")
    args, leftovers = parser.parse_known_args()

    input_file = sys.stdin if args.file is None else open(args.file, mode="rb")

    # In trivial implementation I would have done:
    # import numpy as np
    #
    # f = open("file.bin", "r")
    # a = np.fromfile(f, dtype=np.uint32)


    # Process file in 1MB chunks and display progress
    crunched_mb = 0 # calming the spirit
    intermediate_progress_display = 100 # every 100MB

    while True:
        chunk = input_file.read(1024*1024)
        if not chunk:
            break
        uint32_array = numpy.frombuffer(chunk, dtype=numpy.uint32)
        chunk_cruncher(uint32_array)

        if crunched_mb % intermediate_progress_display == 0:
            print(f"Data processed: {crunched_mb} MB")
        crunched_mb += 1


def get_binned_frequencies():
    for i in range(0, BIN_COUNT):
        data = get_bin_data(i)
        if len(data.keys())>0 : # skip empty bins
            yield data

if __name__ == "__main__":
    count_frequencies_from_input_and_store_bins()

