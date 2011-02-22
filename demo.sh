#!/bin/bash

# purpose: demonstrate broken yum/rpm behavior 
#          with respect to scriptlets (pre, post, preun, postun)
#
# usage:   update the following three variables as appropriate
#          for your test box.

dir=/tmp/tito/noarch/
rpm1=$dir/rpm-scriptlets-0.1-1.fc14.noarch.rpm
rpm2=$dir/rpm-scriptlets-0.2-1.fc14.noarch.rpm

# ensure we do not have rpm-scriptlets installed
yum -y remove rpm-scriptlets &> /dev/null

# marker for grep
marker='>>>>>>>>>>'

echo "Demo with yum"
echo " ============="
echo "initial install"
yum -y --nogpgcheck localinstall $rpm1 2>&1 | grep "$marker"

echo "upgrade"
yum -y --nogpgcheck localinstall $rpm2 2>&1 | grep "$marker"

echo "final removal"
yum -y remove rpm-scriptlets 2>&1 | grep "$marker"

echo
echo "Demo with rpm"
echo " ============="
echo "initial install"
rpm -U $rpm1 2>&1 | grep "$marker"

echo "upgrade"
rpm -U $rpm2 2>&1 | grep "$marker"

echo "final removal"
rpm -e 2>&1 | grep "$marker"
