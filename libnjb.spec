#%define	prefix	/usr
Name:		libnjb
Version:	2.0
Release:	1
Summary:	A software library for talking to the Creative Nomad Jukebox
URL:		http://sourceforge.net/projects/libnjb
Group:		Libraries
Vendor:		PLD
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	BSD
Requires:       libusb
BuildRequires:	libusb-devel

%description
This package provides a software library for communicating with the
Creative Nomad Jukebox line of MP3 players.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make lib

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
make prefix=$RPM_BUILD_ROOT%{prefix} install
# install hotplug scripts so they are up to date
mkdir -p $RPM_BUILD_ROOT/etc/hotplug/usb
install -m 755 nomadjukebox $RPM_BUILD_ROOT/etc/hotplug/usb
install -m 644 nomad.usermap $RPM_BUILD_ROOT/etc/hotplug/usb

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root,755)
%{prefix}/lib/*.so
%{prefix}/lib/*.a
%{prefix}/lib/*.la
%{prefix}/include/*.h
%dir %{prefix}/lib/pkgconfig
%{prefix}/lib/pkgconfig/*.pc
%dir /etc/hotplug/usb
%config(noreplace) /etc/hotplug/usb/*
%doc AUTHORS CHANGES FAQ INSTALL LICENSE HACKING

%changelog

$Log: libnjb.spec,v $
Revision 1.1  2005-03-13 17:05:36  mick3y
- draft version only
- ripped from RH spec

 
