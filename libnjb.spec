Summary:	A software library for talking to the Creative Nomad Jukebox
Summary(pl):	Biblioteka do komunikowania siê z Creative Nomad Jukebox
Name:		libnjb
Version:	2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://mesh.dl.sourceforge.net/sourceforge/libnjb/%{name}-%{version}.tar.gz
# Source0-md5:	3f8b1d8a4e48d87cb78b2a6431fddb76
URL:		http://sourceforge.net/projects/libnjb
BuildRequires:	libusb-devel
Requires:	libusb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a software library for communicating with the
Creative Nomad Jukebox line of MP3 players.

%description -l pl
Pakiet ten dostarcza bibliotekê do komunikowania siê z odtwarzaczem MP3 
Creative Nomad Jukebox.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" 
./configure \
	--prefix=%{_prefix}
%{__make} lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install nomadjukebox $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb
install nomad.usermap $RPM_BUILD_ROOT%{_sysconfdir}/hotplug/usb

%clean
rm -r $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES FAQ HACKING LICENSE README
%{_prefix}/lib/*.so
%{_prefix}/lib/*.a
%{_prefix}/lib/*.la
%{_includedir}/*.h
%dir %{_prefix}/lib/pkgconfig
%{_prefix}/lib/pkgconfig/*.pc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hotplug/usb/*
