#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	API interface to talk to Zen Creative devices
Summary(pl.UTF-8):	Interfejs API do komunikacji z urządzeniami Zen Creative
Name:		libnjb
Version:	2.2.6
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libnjb/%{name}-%{version}.tar.gz
# Source0-md5:	e1b3a89f6157c553ea46a78446429a0d
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

%description -l pl.UTF-8
libnjb jest biblioteką C jak również API używanym do komunikacji z
Creative Nomad JukeBox i cyfrowym odtwarzaczem muzyki Dell DJ dla
platform BSD, Linux, Mac IS X i Windows. Protokół jest przypuszczalnie
nazwany przez Creative PDE (Portable Digital Entertainment protocol).
Nowsze urządzenia używające Microsoft MTP (Media transfer Protocol)
NIE są obsługiwane.

%package devel
Summary:	Header files for njb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnjb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel

%description devel
Header files for njb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki njb.

%package static
Summary:	Static njb library
Summary(pl.UTF-8):	Statyczna biblioteka njb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static njb library.

%description static -l pl.UTF-8
Statyczna biblioteka njb.

%package utils
Summary:	njb utilities
Summary(pl.UTF-8):	Narzędzia njb
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description utils
Utilities for njb library.

%description utils -l pl.UTF-8
Narzędzia dla biblioteki njb.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnjb.a
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/njb*
