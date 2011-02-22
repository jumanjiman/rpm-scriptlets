Name:		rpm-scriptlets
Version:	0.1
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
%doc README.asciidoc

%global marker >>>>>>>>>>

%pre
echo "%{marker} %{version}-%{release} pre $1" > /dev/stderr


%post
echo "%{marker} %{version}-%{release} post $1" > /dev/stderr


%preun
echo "%{marker} %{version}-%{release} preun $1" > /dev/stderr


%postun
echo "%{marker} %{version}-%{release} postun $1" > /dev/stderr


%changelog
