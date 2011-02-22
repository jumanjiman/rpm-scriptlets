#!/bin/bash

dir=/tmp/tito/noarch
rpm1=$dir/rpm-scriptlets-0.1-1.fc14.noarch.rpm
rpm2=$dir/rpm-scriptlets-0.2-1.fc14.noarch.rpm
yum_options="-y --nogpgcheck"

# ensure we do not have rpm-scriptlets installed
yum -y remove rpm-scriptlets &> /dev/null

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

echo "final removal"
run_command "yum $yum_options remove rpm-scriptlets"

echo
echo "Demo with yum and NO plugins"
echo "============================"
echo "initial install"
run_command "yum $yum_options --disableplugin=* localinstall $rpm1"

echo "upgrade"
run_command "yum $yum_options --disableplugin=* localinstall $rpm2"

echo "final removal"
run_command "yum $yum_options --disableplugin=* remove rpm-scriptlets"

echo
echo "Demo with rpm"
echo "============="
echo "initial install"
run_command "rpm -U $rpm1"

echo "upgrade"
run_command "rpm -U $rpm2"

echo "final removal"
run_command "rpm -e rpm-scriptlets"
