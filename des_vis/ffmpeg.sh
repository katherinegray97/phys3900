ffmpeg -y -i outputs/$1%03d.png -c:v libx264 -preset veryslow -pix_fmt yuv420p -crf 30 -profile:v main outputs/$2.mp4
