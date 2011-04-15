%define api 1.0
%define major 2
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:           gupnp-dlna
Version:        0.6.1
Release:        %mkrel 1
Summary:        A collection of helpers for building UPnP dlna applications
Group:		System/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk-doc
BuildRequires: libxml2-devel
BuildRequires: libgstreamer0.10-plugins-base-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP devices and
control points, written in C using GObject and libsoup. The GUPnP API is
intended to be easy to use, efficient and flexible.

GUPnP DLNA is a small utility library that aims to ease the
DLNA-related tasks such as media profile guessing, transcoding to
a given profile, etc.

%package -n %libname
Summary: A collection of helpers for building UPnP DLNA applications
Group: System/Libraries

%description -n %libname
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP DLNA is a small utility library that aims to ease the
DLNA-related tasks such as media profile guessing, transcoding to
a given profile, etc.

%package -n %develname
Summary: Development package for %{name}
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %version-%release

%description -n %develname
Files for development with %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/lib%{name}-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/*
%{_libdir}/pkgconfig/%name-%api.pc
%{_libdir}/lib%name-%api.so
%{_libdir}/lib%name-%api.la
