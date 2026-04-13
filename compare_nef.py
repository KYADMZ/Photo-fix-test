def compare_files(file1, file2, max_checks=50000000):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        data1 = f1.read()
        data2 = f2.read()

    size1 = len(data1)
    size2 = len(data2)

    print("Filesize no.1:", size1)
    print("Filesize  no.2:", size2)

    min_size = min(size1, size2)

    diff_count = 0
    first_diff = None

    for i in range(min_size):
        if data1[i] != data2[i]:
            diff_count += 1
            if first_diff is None:
                first_diff = i

        if i >= max_checks:
            break

    if first_diff is not None:
        print("First difference in the offset:", first_diff)
        print("Byte File 1:", data1[first_diff])
        print("Byte File 2:", data2[first_diff])
    else:
        print("No differences have been found in the analyzed range.")

    print("Total differences found:", diff_count)


if __name__ == "__main__":
    compare_files("SRH_2046.NEF", "reconstructed.NEF")
