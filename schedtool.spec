Summary:	Tool for querying and altering scheduler parameters
Summary(pl.UTF-8):	Narzędzie do odpytywania i zmieniania parametrów schedulera
Name:		schedtool
Version:	1.3.0
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://freequaos.host.sk/schedtool/%{name}-%{version}.tar.bz2
# Source0-md5:	0d968f05d3ad7675f1f33ef1f6d0a3fb
Patch0:		%{name}-DESTDIR.patch
URL:		http://freequaos.host.sk/schedtool/
# requires new sched_getaffinity prototype
BuildRequires:	glibc-devel >= 6:2.3.4
BuildRequires:	linux-libc-headers >= 7:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schedtool can be used to query or alter scheduler parameters.

%description -l pl.UTF-8
Schedtool może być używany w celu odpytania lub zmiany parametrów
schedulera.

%prep
%setup -q
%patch0 -p1

%build
# -D... is workaround for test - libc headers don't include <asm/unistd.h>
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -D__NR_sched_getaffinity"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README SCHED_DESIGN TUNING
%attr(755,root,root) %{_bindir}/schedtool
%{_mandir}/man8/schedtool.8*
