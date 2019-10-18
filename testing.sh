#!/bin/bash
read -p "Enter package or service you want to install:" myvar
status2=$(yum list installed | grep "$myvar " |grep -v "tools" | awk -F "." '{print $1}')
echo $myvar
echo $status2
if [$status==$myvar ]; then
echo "This package or service is already installed"
exit 0;
else
read -p "Do you wish to install this program?:"
case $yn in
[Yy]* ) yum -y install "$1" ; break;;
[Nn]* ) exit;;
* ) echo "Please answer yes or no.";;
esac
fi
~
~
~
~
~
