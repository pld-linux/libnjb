# TODO: udev support?
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_with	hotplug		# old-style hotplug support in "-utils"

Summary:	API interface to talk to Zen Creative devices
Summary(pl.UTF-8):	Interfejs API do komunikacji z urządzeniami Zen Creative
Name:		libnjb
Version:	2.2.7
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libnjb/%{name}-%{version}.tar.gz
# Source0-md5:	73f25f3297abe316dd0abec921781d50
Patch0:		docs.patch
URL:		http://libnjb.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
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
Requires:	libusb-compat-devel

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

%package apidocs
Summary:	API documentation for njb library
Summary(pl.UTF-8):	Dokumentacja API biblioteki njb
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for njb library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki njb.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_hotplug:--enable-hotplugging} \
	%{!?with_static_libs:--disable-static}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	includedir=%{_includedir}/%{name}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnjb.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ HACKING README
%attr(755,root,root) %{_libdir}/libnjb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnjb.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnjb.so
%{_includedir}/%{name}
%{_pkgconfigdir}/libnjb.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnjb.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/njb-*
%if %{with hotplug}
%attr(755,root,root) /etc/hotplug/usb/nomadjukebox
/etc/hotplug/usb/nomad.usermap
%endif
