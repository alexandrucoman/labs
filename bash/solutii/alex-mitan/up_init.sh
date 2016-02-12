#!/bin/bash -x

echo '' >> ~/.bashrc
echo 'function up {' >> ~/.bashrc
echo '    LVLS=$1' >> ~/.bashrc
echo '    for i in `seq 1 $LVLS`; do' >> ~/.bashrc
echo '        cd ../' >> ~/.bashrc
echo '    done' >> ~/.bashrc
echo '} ' >> ~/.bashrc
echo '' >> ~/.bashrc

