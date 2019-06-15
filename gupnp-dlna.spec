%define url_ver %(echo %{version} | cut -d. -f1,2)

%define api 2.0
%define major 3
%define girmajor 2.0
%define libname %mklibname %{name}-gst %{api} %{major}
%define girname %mklibname %{name}-gir %{girmajor}
%define devname %mklibname -d %{name}

Name:		gupnp-dlna
Version:	0.10.5
Release:	1
Summary:	A collection of helpers for building UPnP dlna applications
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gupnp.org/
Source0:		http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gtk-doc
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(vapigen)

%description
GUPnP is an object-oriented open source framework for creating UPnP devices and
control points, written in C using GObject and libsoup. The GUPnP API is
intended to be easy to use, efficient and flexible.

GUPnP DLNA is a small utility library that aims to ease the
DLNA-related tasks such as media profile guessing, transcoding to
a given profile, etc.

%package -n %{libname}
Summary:	A collection of helpers for building UPnP DLNA applications
Group:	System/Libraries

%description -n %{libname}
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP DLNA is a small utility library that aims to ease the
DLNA-related tasks such as media profile guessing, transcoding to
a given profile, etc.

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}gupnp-dlna2.0_3 < 0.10.2

%description -n %{devname}
Files for development with %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%build
%configure \
	--enable-introspection=yes

%make_build

%install
%make_install

#we don't want these
find %{buildroot} -name "*.la" -delete

%files
%{_bindir}/*
%{_datadir}/%{name}-%{girmajor}
%{_libdir}/%{name}

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/lib%{name}*%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUPnPDLNA-%{girmajor}.typelib
%{_libdir}/girepository-1.0/GUPnPDLNAGst-%{girmajor}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/%{name}*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}*-%{api}.so
%{_datadir}/gir-1.0/GUPnPDLNA-%{girmajor}.gir
%{_datadir}/gir-1.0/GUPnPDLNAGst-%{girmajor}.gir
%{_datadir}/vala/vapi/*
