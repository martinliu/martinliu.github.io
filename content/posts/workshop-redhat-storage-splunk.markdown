---
author: liuadmin
categories:
- opensource
comments: true
date: 2014-12-04T02:34:03Z
slug: workshop-redhat-storage-splunk
tags:
- rhs
- splunk
title: workshop redhat storage and splunk
url: /2014/12/04/workshop-redhat-storage-splunk/
wordpress_id: 53324
---

## Instance Details


Replace userX with your user id. For example, user1 --> user 30
<table border="1" >
<tbody >
<tr >

<td >Instance
</td>

<td >DNS
</td>

<td >IP
</td>
</tr>
<tr >

<td >**Internal**
</td>
</tr>
<tr >

<td >RHS 01
</td>

<td >rhs-01.userX.apac.red
</td>

<td >10.100.0.101
</td>
</tr>
<tr >

<td >RHS 02
</td>

<td >rhs-02.userX.apac.red
</td>

<td >10.100.0.102
</td>
</tr>
<tr >

<td >RHS 03
</td>

<td >rhs-03.userX.apac.red
</td>

<td >10.100.0.103
</td>
</tr>
<tr >

<td >RHS 04
</td>

<td >rhs-04.userX.apac.red
</td>

<td >10.100.0.104
</td>
</tr>
<tr >

<td >Splunk Master
</td>

<td >splunkmaster.userX.apac.red
</td>

<td >10.100.0.201
</td>
</tr>
<tr >

<td >Splunk Search
</td>

<td >splunksearch.userX.apac.red
</td>

<td >10.100.0.202
</td>
</tr>
<tr >

<td >Splunk Peer 01
</td>

<td >splunkpeer-01.userX.apac.red
</td>

<td >10.100.0.211
</td>
</tr>
<tr >

<td >Splunk Peer 01
</td>

<td >splunkpeer-02.userX.apac.red
</td>

<td >10.100.0.212
</td>
</tr>
<tr >

<td >Splunk Peer 01
</td>

<td >splunkpeer-03.userX.apac.red
</td>

<td >10.100.0.213
</td>
</tr>
<tr >

<td >**Public**
</td>
</tr>
<tr >

<td >Gateway
</td>

<td >gw-userX.apac.red
</td>

<td >gw-userX.apac.red
</td>
</tr>
<tr >

<td >Splunk Master
</td>

<td >splunk.userX.apac.red
</td>

<td >splunk.userX.apac.red
</td>
</tr>
<tr >

<td >Splunk Search
</td>

<td >search.userX.apac.red
</td>

<td >search.userX.apac.red
</td>
</tr>
</tbody>
</table>


### On your laptop


cd ~/.ssh
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhte-splunk-lab
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhte-splunk-lab.pub
chmod 600 rhte-splunk-lab
chmod 644 rhte-splunk-lab.pub

ssh -i ~/.ssh/rhte-splunk-lab -l ec2-user gw-userX.apac.red


### On all RHS Nodes


sudo su -
subscription-manager attach --pool 8a85f9864675056e014684868378649c
subscription-manager repos --disable=*
subscription-manager repos --enable rhel-6-server-rpms --enable rhs-3-for-rhel-6-server-rpms --enable rhel-scalefs-for-rhel-6-server-rpms

yum -y update

cat /etc/redhat-* # should say Red Hat Enterprise Linux 6.6 (Santiago) and Red Hat Storage 3.0 Update 2

/sbin/service glusterd restart


### On RHS-01


gluster peer probe rhs-02.userX.apac.red
gluster peer probe rhs-03.userX.apac.red
gluster peer probe rhs-04.userX.apac.red

gluster pool list

gluster volume create splunk replica 2 rhs-01.userX.apac.red:/srv/brick1/splunk rhs-02.userX.apac.red:/srv/brick1/splunk rhs-03.userX.apac.red:/srv/brick1/splunk rhs-04.userX.apac.red:/srv/brick1/splunk

gluster volume set splunk storage.owner-uid 1001
gluster volume set splunk storage.owner-gid 1001
gluster volume set splunk user.nfs disable

gluster volume start splunk

gluster volume info
gluster volume status


### On Splunk Master and Splunk Search Nodes


subscription-manager attach --pool 8a85f9864675056e014684868378649c
subscription-manager repos --disable=*
subscription-manager repos --enable rhel-7-server-rpms

yum -y update

wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/splunk-6.2.0-237341-linux-2.6-x86_64.rpm --no-check-certificate


### On all Splunk Nodes


subscription-manager attach --pool 8a85f9864675056e014684868378649c
subscription-manager repos --disable=*
subscription-manager repos --enable rhel-7-server-rpms --enable rhel-7-server-openstack-5.0-rpms --enable rhel-7-server-rh-common-rpms

yum -y update

yum -y install wget lvm2

wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/splunk-6.2.0-237341-linux-2.6-x86_64.rpm --no-check-certificate

/bin/systemctl start lvm2-lvmetad.service
/bin/systemctl start lvm2-monitor.service

pvcreate --dataalignment 1024k /dev/xvdb1
vgcreate splunkdb /dev/xvdb1
/sbin/lvcreate -a y -l 100%VG -n splunkdb splunkdb
mkfs.xfs -i size=512 /dev/mapper/splunkdb-splunkdb


### On all Splunk Nodes


echo -e `blkid /dev/mapper/splunkdb-splunkdb | cut -d " " -f 2`"\t/opt/\txfs\tdefaults,inode64,noatime\t0\t0" >> /etc/fstab
mount /opt

yum -y localinstall splunk-6.2.0-237341-linux-2.6-x86_64.rpm

echo -e "splunk\t\tsoft\tnofile\t10240" >> /etc/security/limits.conf
echo -e "splunk\t\thard\tnofile\t20480" >> /etc/security/limits.conf


### On Splunk Master and Splunk Search


cd /lib/systemd/system
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/splunkd.service --no-check-certificate

sed -i.bak '/^After\|^Requires/d' splunkd.service
sed -i.bak '/Description/a After=network.target local-fs.target' splunkd.service
systemctl daemon-reload
systemctl enable splunkd.service
systemctl start splunkd.service

runuser -l splunk -c 'splunk status'
q
y
systemctl restart splunkd.service
runuser -l splunk -c 'splunk status'


### On Splunk Peer Nodes


yum install -y glusterfs-fuse python-httplib2 attr

mkdir /mnt/glusterfs
echo -e "rhs-01.userX.apac.red:/splunk\t\t/mnt/glusterfs\t\tglusterfs\t\tdefaults,_netdev,backup-volfile-servers=rhs02.userX.apac.red:rhs-03.userX.apac.red:rhs-04.userX.apac.red\t0\t0" >> /etc/fstab
mount /mnt/glusterfs

runuser -l splunk -c 'mkdir -p /opt/splunk/var/lib/splunk/glusterfs'
runuser -l splunk -c 'mkdir -p /mnt/glusterfs/$(hostname -s)'

cd /lib/systemd/system
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/splunkd-pre.service
systemctl enable splunkd-pre.service
systemctl start splunkd-pre.service

echo OPTIMISTIC_ABOUT_FILE_LOCKING = 1 >> /opt/splunk/etc/splunk-launch.conf

wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/splunkd.service
systemctl daemon-reload
systemctl enable splunkd.service
systemctl start splunkd.service
runuser -l splunk -c 'splunk status'
q
y
systemctl start splunkd.service
runuser -l splunk -c 'splunk status'

cd /opt/splunk/bin
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhsBucketMover.py
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhsBucketMover.sh
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhsLinkChecker.py

chown splunk:splunk/rhs*


### on gw-userX.apac.red


iptables -t nat -A PREROUTING -p tcp --dport 8001 -j DNAT --to-destination 10.100.0.211:8000
iptables -t nat -A PREROUTING -p tcp --dport 8002 -j DNAT --to-destination 10.100.0.212:8000
iptables -t nat -A PREROUTING -p tcp --dport 8003 -j DNAT --to-destination 10.100.0.213:8000


### Web GUI on Splunk Master (http://splunk.userX.apac.red:8000/)


Settings --> Indexer Clustering
Replication Factor 3
Search Factor 2
Enable Clustering - accept until restart and hit ok


### on each
Web GUI on Splunk Peer 01 (http://gw-userX.apac.red:8001/)
Web GUI on Splunk Peer 02 (http://gw-userX.apac.red:8002/)
Web GUI on Splunk Peer 03 (http://gw-userX.apac.red:8003/)


Settings --> Indexer Clustering
Enable Clustering
Type - Peer
host = https://splunkmaster.userX.apac.red
port 8089
replication port 8090


### Web GUI on Splunk Search (http://search.userX.apac.red:8000/)


Settings --> Indexer Clustering
Enable Clustering
Type - Search
host = https://splunkmaster.userX.apac.red
port 8089
replication port 8090


### on Splunk Master Node


cd /opt/splunk/etc/master-apps/_cluster/local directory
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/indexes.conf
runuser -l splunk -c 'splunk apply cluster-bundle --answer-yes'
admin
password
runuser -l splunk -c 'splunk show cluster-bundle-status'


### On each Node


runuser -l splunk -c 'splunk search "| rest /services/data/indexes | table title, homePath, coldPath"'|grep demo
< look for $SPLUNKDB/glusterfs/demo/colddb


### on Splunk Master Node


su - ec2-user

cd ~/.ssh
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhte-splunk-lab
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/rhte-splunk-lab.pub
chmod 600 rhte-splunk-lab
chmod 644 rhte-splunk-lab.pub

cd /tmp
wget https://s3-ap-southeast-1.amazonaws.com/splunk-lab/eventgen.tar.gz
scp -i ~/.ssh/rhte-splunk-lab eventgen.tar.gz splunkpeer-01.userX.apac.red:eventgen.tar.gz
scp -i ~/.ssh/rhte-splunk-lab eventgen.tar.gz splunkpeer-02.userX.apac.red:eventgen.tar.gz
scp -i ~/.ssh/rhte-splunk-lab eventgen.tar.gz splunkpeer-03.userX.apac.red:eventgen.tar.gz


### On each Peer Node


cd /opt/splunk
mv ~ec2-user/eventgen.tar.gz /opt/splunk
chown splunk:splunk eventgen.tar.gz
runuser -l splunk -c 'splunk install app /opt/splunk/eventgen.tar.gz'
runuser -l splunk -c 'splunk restart'

cd /opt/splunk/etc/apps/eventgen/samples
cp sample.tutorial1 demo_data
sed -i.bak s/main/demo/g demo_data
cd /opt/splunk/etc/apps/eventgen/local
cp ../README/eventgen.conf.tutorial1 eventgen.conf
sed -i.bak 's/main/demo/g;s/sample.tutorial1/demo_data/g' eventgen.conf

runuser -l splunk -c 'splunk restart'

Log into WebUI on Splunk Master
search "index = demo"
timeframe = realtime > 5 minutes

check /opt/splunk/var/lib/splunk/demo/db
