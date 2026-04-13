import rawpy # type: ignore
import imageio # type: ignore
import os

input_file = "reconstructed.NEF"
output_file = "recovered_d750.tiff"

if not os.path.exists(input_file):
    print(input_file)
    print("Corrupted file not found")
    exit()

try:
    print("Trying to open NEF file...")
    with rawpy.imread(input_file) as raw:
        print("file read correctly")
        print("Solution found:", raw.sizes)

        rgb = raw.postprocess(
            use_camera_wb=True,
            no_auto_bright=False,
            output_bps=16
        )    

        imageio.imwrite(output_file, rgb)
        print("Image recovered successfully!")

except Exception as e:
    print("Error while procesing the file")
    print(e)