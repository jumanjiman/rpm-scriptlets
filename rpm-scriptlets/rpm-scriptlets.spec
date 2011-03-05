Name:		rpm-scriptlets
Version:	0.3
Release:	1%{?dist}
Summary:	Demonstrate order of scriptlets during rpm install/upgrade

Group:		Development/Tools
License:	GPLv3+
URL:		https://github.com/jumanjiman/rpm-scriptlets
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	rpm-build

%description
Demonstrate the execution order of RPM scriptlets and the dollar-one
variable during RPM installation, upgrade, and removal.


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


%changelog
* Tue Feb 22 2011 Paul Morgan <jumanjiman@gmail.com> 0.3-1
- README reflects output from updated demo.sh
- improved demo logic and reporting

* Tue Feb 22 2011 Paul Morgan <jumanjiman@gmail.com> 0.2-1
- bump version (jumanjiman@gmail.com)

* Tue Feb 22 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito


