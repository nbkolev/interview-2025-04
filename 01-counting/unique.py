from count_frequencies import count_frequencies_from_input_and_store_bins, get_binned_frequencies

# As the solution for subtask A and B requires the same data processing
# the code is moved to a common location count_frequencies.py
count_frequencies_from_input_and_store_bins()

unique_numbers = 0
for frequency_bin in get_binned_frequencies():
    # As data is binned we know that every bin contains only unique keys
    unique_numbers += len(frequency_bin.keys())

print(f"{unique_numbers} unique numbers")