Name:		rpm-scriptlets-ng
Version:	0.5
Release:	1%{?dist}
Summary:	Demonstrate order of scriptlets during rpm install/upgrade

Group:		Development/Tools
License:	GPLv3+
URL:		https://github.com/jumanjiman/rpm-scriptlets
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	rpm-build

obsoletes:	rpm-scriptlets < %{version}-%{release}
provides:	rpm-scriptlets = %{version}-%{release}

%description
Demonstrate the execution order of RPM scriptlets and the dollar-one
variable during RPM installation, upgrade, and removal.

This "next-generation" package demonstrates how to obsolete old
packages.


%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)


%global marker >>>>>>>>>>

%pre
echo "%{marker} %{version}-%{release} pre $1" > /dev/stderr


%post
echo "%{marker} %{version}-%{release} post $1" > /dev/stderr
if [ $1 -gt 0 ]; then
  sed -i "/^#RPM_SCRIPTLETS_BEGIN/,/^#RPM_SCRIPTLETS_END/d" /etc/hosts
  cat >> /etc/hosts << EOF
#RPM_SCRIPTLETS_BEGIN
4.2.2.1 vnsc-pri.sys.gtei.net emergency-nameserver
#RPM_SCRIPTLETS_END
EOF
fi


%preun
echo "%{marker} %{version}-%{release} preun $1" > /dev/stderr
if [ $1 -eq 0 ]; then
  sed -i "/^#RPM_SCRIPTLETS_BEGIN/,/^#RPM_SCRIPTLETS_END/d" /etc/hosts
fi


%postun
echo "%{marker} %{version}-%{release} postun $1" > /dev/stderr


%triggerpostun -- rpm-scriptlets < %{version}-%{release}
echo "%{marker} %{version}-%{release} triggerpostun $1" > /dev/stderr
# fix replacement of rpm-scriptlets since its preun runs
# after our post-install scriptlet
sed -i "/^#RPM_SCRIPTLETS_BEGIN/,/^#RPM_SCRIPTLETS_END/d" /etc/hosts || :
cat >> /etc/hosts << EOF
#RPM_SCRIPTLETS_BEGIN
4.2.2.1 vnsc-pri.sys.gtei.net emergency-nameserver
#RPM_SCRIPTLETS_END
EOF
:


%changelog
* Sat Mar 05 2011 Paul Morgan <jumanjiman@gmail.com> 0.5-1
- obsolete origin rpm-scriptlets


