Name:		rpm-scriptlets-other
Version:	0.2
Release:	1%{?dist}
Summary:	Demonstrate trigger scriptlets

Group:		Development/Tools
License:	GPLv3+
URL:		https://github.com/jumanjiman/rpm-scriptlets
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	rpm-build

%description
This package should cause trigger scripts from rpm-scriptlets-ng
to run when rpm-scriptlets-other is installed, upgraded, or removed.
Otherwise, this package is a no-op.


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
echo "%{marker} %{name}-%{version}-%{release} pre $1" > /dev/stderr


%post
echo "%{marker} %{name}-%{version}-%{release} post $1" > /dev/stderr


%preun
echo "%{marker} %{name}-%{version}-%{release} preun $1" > /dev/stderr


%postun
echo "%{marker} %{name}-%{version}-%{release} postun $1" > /dev/stderr


%changelog
* Wed Apr 06 2011 Paul Morgan <jumanjiman@gmail.com> 0.2-1
- bump version

* Wed Apr 06 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito

