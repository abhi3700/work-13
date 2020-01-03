# import pyexif
# print(pyexif.getKeywords())

import exifread
# Open image file for reading (binary mode)
f = open('image.tif', 'rb')

# Return Exif tags
tags = exifread.process_file(f)
# print(tags)
# print('===============================')
print(tags.keys())
for tag in tags.keys():
    print(str(tag) + ' ' + str(tags[tag]))
# print('===============================')
# print(tags.values())

# Print the tag/ value pairs
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print "Key: %s, value %s" % (tag, tags[tag])

print(tags.get('IFD 2 ImageDescription'))