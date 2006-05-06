Summary:	API interface to talk to Zen Creative devices
Summary(pl):	Interfejs API do komunikacji z urz±dzeniami Zen Creative
Name:		libnjb
Version:	2.2.5
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libnjb/%{name}-%{version}.tar.gz
# Source0-md5:	f7461574b9a28ed1c79fb40d3d307d78
URL:		http://libnjb.sourceforge.net/
BuildRequires:	libusb-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnjb is a C library and API for communicating with the Creative
Nomad JukeBox and Dell DJ digital audio players under BSD, Linux, Mac
OS X and Windows. The protocol these devices use is presumably called
PDE (Portable Digital Entertainment protocol) at Creative. Newer
devices using the Microsoft MTP (Media Transfer Protocol) are NOT
supported

%description -l pl
libnjb jest bibliotek± C jak równie¿ API u¿ywanym do komunikacji z
Creative Nomad JukeBox i cyfrowym odtwarzaczem muzyki Dell DJ dla
platform BSD, Linux, Mac IS X i Windows. Protokó³ jest przypuszczalnie
nazwany przez Creative PDE (Portable Digital Entertainment protocol).
Nowsze urz±dzenia u¿ywaj±ce Microsoft MTP (Media transfer Protocol)
NIE s± obs³ugiwane.

%package devel
Summary:	Header files for njb library
Summary(pl):	Pliki nag³ówkowe biblioteki libnjb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for njb library.

%description devel -l pl
Pliki nag³ówkowe biblioteki njb.

%package static
Summary:	Static njb library
Summary(pl):	Statyczna biblioteka njb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static njb library.

%description static -l pl
Statyczna biblioteka njb.

%package utils
Summary:	njb utilities
Summary(pl):	Narzêdzia njb
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description utils
Utilities for njb library.

%description utils -l pl
Narzêdzia dla biblioteki njb.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	includedir=%{_includedir}/%{name}

install nomadjukebox $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb
install nomad.usermap $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ HACKING README
%attr(755,root,root) %{_libdir}/libnjb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnjb.so
%{_libdir}/libnjb.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnjb.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/njb*
