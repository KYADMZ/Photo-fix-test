import rawpy # type: ignore
import numpy as np # type: ignore
import imageio # type: ignore

try:
    raw = rawpy.imread('truncated.NEF')
    print("RAW open")

    try:
        rgb = raw.postprocess()
        imageio.imwrite('output_full.tiff', rgb)
        print("Export completed successfully")

    except Exception as e:
        print("Fail in postprocess:", e)
        print("Trying to extract raw_image directly...")

        raw_data = raw.raw_image.copy()

       
        raw_data = raw_data.astype(np.uint16)

        imageio.imwrite('output_partial.tiff', raw_data)
        print("Image has been saved as output_partial.tiff")

    raw.close()

except Exception as e:
    print("Total Error:", e)
