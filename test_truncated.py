import rawpy # type: ignore
import imageio # type: ignore
import numpy as np # type: ignore

try:
    with rawpy.imread('truncado.NEF') as raw:
        print("Truncated RAW successfully open")

        try:
            rgb = raw.postprocess(
                use_camera_wb=True,
                no_auto_bright=True,
                output_bps=16
            )

            imageio.imwrite('output_truncated.tiff', rgb)
            print("Image exported as output_truncated.tiff")

        except Exception as e:
            print("Fail en postprocess:")
            print(e)

except Exception as e:
    print("Error trying to open truncated RAW:")
    print(e)
