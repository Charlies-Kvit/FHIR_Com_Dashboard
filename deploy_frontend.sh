#!/bin/bash

On_Yellow='\033[43m'      # Yellow
On_Green='\033[42m'       # Green
Black='\033[0;30m'        # Black
Color_Off='\033[0m'       # Text Reset


echo -e "  ${Black}${On_Yellow}Warning:${Color_Off} at the end of this operation server will reboot"
echo -e "  ${Black}${On_Green}TIP:${Color_Off} Don't forget to pull before deploy"

while true; do

read -p "Do you want to proceed? (y/n) " yn

case $yn in
  [yY] ) echo ok, we will proceed;
    break;;
  [nN] ) echo exiting...;
    exit;;
  * ) echo invalid response;;
esac

done


REPOSITORY=/root/FHIR_Com_Dashboard
FRONTEND=$REPOSITORY/frontend

echo Build frontend
npm --prefix $FRONTEND upgrade
npm --prefix $FRONTEND install
npm --prefix $FRONTEND run build

DEPLOY_TARGET=/var/www/html

echo Deploy frontend
rm -rd $DEPLOY_TARGET/* # Clear before copy
cp -a $FRONTEND/build/. $DEPLOY_TARGET

reboot
