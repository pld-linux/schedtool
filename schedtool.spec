Summary:	Tool for querying and altering scheduler parameters
Summary(pl):	Narzêdzie do odpytywania i zmieniania parametrów schedulera
Name:		schedtool
Version:	0.99
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://freequaos.host.sk/schedtool/%{name}-%{version}.tar.bz2
# Source0-md5:	830d136ab492334e8649afb909a366da
Patch0:		%{name}-DESTDIR.patch
URL:		http://freequaos.host.sk/schedtool/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schedtool can be used to query or alter scheduler parameters.

%description -l pl
Schedtool mo¿e byæ u¿ywany w celu odpytania lub zmiany parametrów
schedulera.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README THANKS TUNING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
