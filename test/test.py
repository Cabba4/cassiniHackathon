import pyheif
import exifread
import io

heif_file = pyheif.read_heif("./IMG_2165.HEIC")

for metadata in heif_file.metadata:

    if metadata['type'] == 'Exif':
        fstream = io.BytesIO(metadata['data'][6:])

    exifdata = exifread.process_file(fstream,details=False)

    # example to get device model from heic file
    lat = str(exifdata.get("GPS GPSLatitude"))
    long = str(exifdata.get("GPS GPSLongitude"))
    print(lat + long)