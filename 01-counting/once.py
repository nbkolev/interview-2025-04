from count_frequencies import count_frequencies_from_input_and_store_bins, get_binned_frequencies

#count_frequencies_from_input_and_store_bins()

seen_only_once = 0
for frequency_bin in get_binned_frequencies():
    # As data is binned we know that every bin contains unique keys,
    # we need only to count the numbers where frequency (the value in the dict) = 1
    seen_only_once += list(frequency_bin.values()).count(1)

print(f"{seen_only_once} numbers seen only once")