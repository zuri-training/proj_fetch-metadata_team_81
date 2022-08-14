from django.db.models.expressions import Value
from django.shortcuts import redirect, render
import os
# Create your views here.
from PIL import Image 
from PIL.ExifTags import TAGS
import pikepdf
from tinytag import TinyTag
from mutagen.flac import FLAC
import ffmpeg._probe
import sys
from pprint import pprint


def meta(request):
    mean=request.POST.get('mename')
    mean=mean[1:]
    print(mean)
    png=(".png")
    jpg=(".jpg")
    pdf=(".pdf")
    mp=(".mp3")
    mpf=(".mp4")
    flac=(".flac")
    avi=("avi")
    mkv=(".mkv")


    if png in mean or jpg in mean:
        image = Image.open(mean)
        info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)}
        for label,value in info_dict.items():
            print(f"{label:25}: {value}")
            metadata=f"{label:25}: {value}"


        exifdata = image.getexif()
        print(exifdata)
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode('ascii','ignore')
            print(f"{tag:25}: {data}")
            metadata=f"{label:25}: {value}" + f"{tag:25}: {data}"


    if pdf in mean:
        pdf = pikepdf.Pdf.open(mean)
        pdf_info = pdf.docinfo
        for key, value in pdf_info.items():
            print(key[1:], ':', value)
            metadata=key[1:], ':', value

    if mp in mean or mpf in mean:
        audio = TinyTag.get(mean)
        metadata=[]
        if audio.title != None:
            metadata +=["Title:" + audio.title]
        if audio.artist != None:    
            metadata +=["Artist: " + audio.artist]
        if audio.genre != None:    
            metadata +=["Genre:" + audio.genre]
        if audio.year != None:    
            metadata +=["Year Released: " + audio.year]
        if audio.bitrate != None:    
            metadata +=["Bitrate:" + str(audio.bitrate) + " kBits/s"]
        if audio.composer != None:    
            metadata +=["Composer: " + audio.composer]
        if audio.filesize != None:    
            metadata +=["Filesize: " + str(audio.filesize) + " bytes"]
        if audio.albumartist != None:    
            metadata +=["AlbumArtist: " + audio.albumartist]
        if audio.duration != None:    
            metadata +=["Duration: " + str(audio.duration) + " seconds"]
        if str(audio.track_total) != None:    
            metadata +=["TrackTotal: " + str(audio.track_total)]
        if audio._filename != None:
               metadata +=["Filename: " + audio._filename]
        if audio.samplerate != None:
               metadata +=["Filename: " + str(audio.samplerate)]
        metadata='\n'.join(map(str, metadata))
        print(metadata)

    if flac in mean:
        audio = FLAC(mean)
        metadata=audio.pprint()

    #if avi in mean:
    #    media_file = mean
    #    pprint(ffmpeg.probe(media_file)["streams"])

    


    #f = open('media/store/files/IMG-20220706-WA0019.jpg', 'rb')
    #tags = exifread.process_file(f)
    #print(tags.keys())
    #pprint.pprint(tags)
    #f.close()
  
    #exifdata = image.getexif()
    #print(exifdata)
    #for tagid in exifdata:
    #    tagname = TAGS.get(tagid, tagid)
    #    value = exifdata.get(tagid)
    #    print(mean)
    #    print(f"{tagname:25}: {value}")
    context={
        'meta':metadata,
        }

    return render(request, 'registration/redirect.html', context)
    