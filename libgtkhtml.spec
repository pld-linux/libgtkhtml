Summary:	GTK HTML widget 2
Summary(pl):	Widget GTK HTML dla GNOME2
Name:		libgtkhtml
Version:	2.0.0
Release:	1
License:	GPL/LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	gail-devel >= 0.16
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	libgnomecanvas-devel >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME2

%description
GTK HTML Widget for the GNOME 2 platform.

%description -l pl
Widget GTK HTML dla platformy GNOME2.

%package devel
Summary:	Header files for GTK HTML 2
Summary(pl):	Pliki nag³ówkowe GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gail-devel >= 0.16
Requires:	libxml2-devel >= 2.4.22
Requires:	libgnomecanvas-devel >= 2.0.1

%description devel
Header files for GTK HTML 2.

%description devel -l pl
Pliki nag³ówkowe dla GTK HTML 2.

%package static
Summary:	Static GTK HTML 2 library
Summary(pl):	Statyczna biblioteka GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of GTK HTML 2 library.

%description static -l pl
Statyczna wersja biblioteki GTK HTML 2.

%prep
%setup -q

%build
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO README NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gtkhtml-2.0
%attr(755,root,root) %{_libdir}/*.??
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
