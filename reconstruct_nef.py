import os


def reconstruct_nef(input_file, output_file, split_offset):
    print("Opening file:", input_file)

    with open(input_file, "rb") as f:
        data = f.read()

    total_size = len(data)
    print("Original file size:", total_size, "bytes")

    if split_offset >= total_size:
        print("ERROR: The offset is bigger than file size.")
        return

    part_after = data[split_offset:]   # desde BF0000 hasta final
    part_before = data[:split_offset]  # desde inicio hasta BF0000

    print("Size part 1 (from offset to end):", len(part_after))
    print("Size part 2 (from start to offset):", len(part_before))

    reconstructed = part_after + part_before

    with open(output_file, "wb") as f:
        f.write(reconstructed)

    print("\nReconstruction finalized.")
    print("New file size:", len(reconstructed), "bytes")

    with open(output_file, "rb") as f:
        header = f.read(4)

    print("First 4 bytes from new file:", header.hex().upper())

    if header[:2] == b'II' and header[2:] == b'\x2A\x00':
        print("Valid TIFF header detected (II 2A 00).")
    else:
        print("Warning: TIFF header doesn't match with II 2A 00.")



    
input_file = "SRH_2048.NEF"
output_file = "reconstructed.NEF"

  
split_offset = 0x00BF0000

if not os.path.exists(input_file):
    print("Could not find file:", input_file)
else:
    reconstruct_nef(input_file, output_file, split_offset)