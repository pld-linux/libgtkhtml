Summary:	GTK HTML widget 2
Summary(pl.UTF-8):	Widget GTK HTML dla GNOME2
Name:		libgtkhtml
Version:	2.11.1
Release:	7
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libgtkhtml/2.11/%{name}-%{version}.tar.bz2
# Source0-md5:	a1d1a197dcff8c4571659deef5495e24
Patch0:		format-security.patch
URL:		https://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.9.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
Requires:	gail >= 1.9.0
Requires:	libxml2 >= 1:2.6.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK HTML Widget for the GNOME 2 platform.

%description -l pl.UTF-8
Widget GTK HTML dla platformy GNOME2.

%package devel
Summary:	Header files for GTK HTML 2
Summary(pl.UTF-8):	Pliki nagłówkowe GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.9.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for GTK HTML 2.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla GTK HTML 2.

%package static
Summary:	Static GTK HTML 2 library
Summary(pl.UTF-8):	Statyczna biblioteka GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of GTK HTML 2 library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki GTK HTML 2.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkhtml-2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO README NEWS
%attr(755,root,root) %{_libdir}/libgtkhtml-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-2.so
%{_includedir}/gtkhtml-2.0
%{_pkgconfigdir}/libgtkhtml-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-2.a
