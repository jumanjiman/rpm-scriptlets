#!/bin/bash

dir=/tmp/tito/noarch
rpm1=$dir/rpm-scriptlets-0.1-1.fc14.noarch.rpm
rpm2=$dir/rpm-scriptlets-0.2-1.fc14.noarch.rpm
rpm3=$dir/rpm-scriptlets-ng-0.5-3.fc14.noarch.rpm
other1=$dir/rpm-scriptlets-other-0.1-1.fc14.noarch.rpm
other2=$dir/rpm-scriptlets-other-0.2-1.fc14.noarch.rpm
yum_options="-y --nogpgcheck"

# ensure we do not have rpm-scriptlets installed
yum -y remove rpm-scriptlets &> /dev/null
yum -y remove rpm-scriptlets-other &> /dev/null

# marker for grep
marker='>>>>>>>>>>'

run_command() {
  _cmd="$*"
  output="$($_cmd 2>&1)"
  _rc=$?
  if [[ $_rc -eq 0 ]]; then
    IFS=" " grep -Eoh "${marker}.*$" <<< $output
  else
    (
    echo "error:"
    echo $output 
    ) >&2
  fi
  return $?
}

echo "Demo with yum and plugins"
echo "========================="
echo "initial install"
run_command "yum $yum_options localinstall $rpm1"

echo "upgrade"
run_command "yum $yum_options localinstall $rpm2"

echo "upgrade to $rpm3"
run_command "yum $yum_options localinstall $rpm3"

echo "install rpm-scriptlets-other"
run_command "yum $yum_options localinstall $other1"

echo "upgrade rpm-scriptlets-other"
run_command "yum $yum_options localinstall $other2"

echo "remove rpm-scriptlets-other"
run_command "yum $yum_options remove rpm-scriptlets-other"

echo "final removal"
run_command "yum $yum_options remove rpm-scriptlets"

echo
echo "Demo with yum and NO plugins"
echo "============================"
echo "initial install"
run_command "yum $yum_options --disableplugin=* localinstall $rpm1"

echo "upgrade"
run_command "yum $yum_options --disableplugin=* localinstall $rpm2"

echo "upgrade to $rpm3"
run_command "yum $yum_options --disableplugin=* localinstall $rpm3"

echo "install rpm-scriptlets-other"
run_command "yum $yum_options --disableplugin=* localinstall $other1"

echo "upgrade rpm-scriptlets-other"
run_command "yum $yum_options --disableplugin=* localinstall $other2"

echo "remove rpm-scriptlets-other"
run_command "yum $yum_options --disableplugin=* remove rpm-scriptlets-other"

echo "final removal"
run_command "yum $yum_options --disableplugin=* remove rpm-scriptlets"

echo
echo "Demo with rpm"
echo "============="
echo "initial install"
run_command "rpm -U $rpm1"

echo "upgrade"
run_command "rpm -U $rpm2"

echo "upgrade to $rpm3"
run_command "rpm -U $rpm3"

echo "install rpm-scriptlets-other"
run_command "rpm -U $other1"

echo "upgrade rpm-scriptlets-other"
run_command "rpm -U $other2"

echo "remove rpm-scriptlets-other"
run_command "rpm -e rpm-scriptlets-other"

echo "final removal"
run_command "rpm -e rpm-scriptlets"
