#!/bin/sh     
#instance-00000002

DATE=`date +%d%B%y`
name=checkpoint-$1-$DATE

#get uuid of vm name
uuid=$(xe vm-list name-label="$1" | awk '{if ( $0 ~ /uuid/) {uuid=$5} if ($0 ~ /name-label/) {$1=$2=$3="";vmname=$0; printf "%s\n", uuid}}')     

#Create checkpoint
check_uuid=$(xe vm-snapshot uuid=$uuid new-name-label=testvmsnapshot) > /dev/null
xe template-param-set is-a-template=false ha-always-run=false uuid=$check_uuid > /dev/null


#Export Snapshot to File 
xe vm-export vm=$check_uuid filename=$name.xva > /dev/null


#Destroy Snapshot 
xe vm-uninstall uuid=$check_uuid force=true > /dev/null

echo $name.xva
