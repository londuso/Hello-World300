#!/bin/bash
if [ -e /usr/bin/wget ]; then
 exit 0;
 fi
 yum -y install wget  # installs wget
  wget https://github.com/londuso/Hello-World300/new/master/package.txt
  for packages in $(cat packages.txt);do
  yum -y install $packages
  done
