#!/bin/bash
#rename.sh imagedir annotationdir target-dir
mkdir -p "$3/Annotations"
mkdir -p "$3/JPEGImages"

cnt=0
for f in $1/*.jpg; do
fn=$(printf "%06d" $cnt)
cp "$f" "$3/JPEGImages/$fn.jpg"
xmlfn=$(basename $f .jpg)
cp "$2/$xmlfn.xml" "$3/Annotations/$fn.xml"
cnt=$[cnt+1]
echo $cnt
done