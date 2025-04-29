import re, sys, argparse
import splitter
from collections import defaultdict

####### Business logic section #######

hdd_models = defaultdict(lambda: 0)

def analyse_and_process_item(id, model, serial):
    global hdd_models
    hdd_models[model] = hdd_models[model] + 1

def aggregate_results_and_print():
    print("Aggregating results...")
    print(f"HDD models present: {len(hdd_models.keys())}")
    hdd_counts_by_model_ascending_count = sorted(hdd_models.items(), key=lambda item: item[1])
    print("Models found sorted in ascending order:")
    for hdd, count in hdd_counts_by_model_ascending_count:
        print (f"{hdd}: {count}")



#######  Glue logic and convenience code ###########

parser = argparse.ArgumentParser(description="Python analysis script. Run with --stdin option or --file option.")
parser.add_argument("--stdin",action='store_true')
parser.add_argument("--file")
args, leftovers = parser.parse_known_args()

input_file = None

if args.stdin is not None:
    input_file = sys.stdin
if args.file is not None:
    input_file = open(args.file)
if not (args.stdin or args.file):
    print(parser.description)
    exit(0)

# A regex to match data like:
# "id":3,"model":"SSDF1","serial":"HD18368977"
hdd_regex = re.compile(r'\"id\":(\d+),\"model\":\"(\w+)\",\"serial\":\"(\w+)\"', re.IGNORECASE)

####### File processing #######


progress_count = 0
intermediate_progress_display_count = 1000000 # a million records

for line in splitter.line_splitter(input_file, newline="},{", chunk_size=1024*1024):
    match = re.search(hdd_regex, line)
    if match:
        id, model, serial = match.group(1), match.group(2), match.group(3)
        analyse_and_process_item(id, model, serial)
    else:
        print(f"Error parsing '{line}'", file=sys.stderr)

    if progress_count % intermediate_progress_display_count == 0:
        print(f"Records processed: {progress_count}")
    progress_count += 1

aggregate_results_and_print()

print("Done.")