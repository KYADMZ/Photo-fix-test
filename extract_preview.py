def extract_largest_jpeg(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    jpeg_starts = []
    i = 0

    while True:
        idx = data.find(b'\xFF\xD8\xFF', i)
        if idx == -1:
            break
        jpeg_starts.append(idx)
        i = idx + 1

    print(f"JPEG Found: {len(jpeg_starts)}")

    largest_jpeg = b''
    largest_size = 0

    for start in jpeg_starts:
        end = data.find(b'\xFF\xD9', start)
        if end != -1:
            jpeg_data = data[start:end+2]
            size = len(jpeg_data)

            if size > largest_size:
                largest_size = size
                largest_jpeg = jpeg_data

    if largest_jpeg:
        with open(output_file, 'wb') as out:
            out.write(largest_jpeg)
        print(f"Biggest JPEG extracted: {largest_size/1024/1024:.2f} MB")
    else:
        print("No valid JPEG has been found.")


extract_largest_jpeg("SRH_3029.NEF", "3029.jpg")

