%define gail_req 1.3.2
%define libxml2_req 2.5.1
%define libgnomecanvas_req 2.3.0
Summary:	GTK HTML widget 2
Summary(pl):	Widget GTK HTML dla GNOME2
Name:		libgtkhtml
Version:	2.3.2
Release:	1
License:	GPL/LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
URL:		http://gtkhtml2.codefactory.se/
BuildRequires:	gail-devel >= %{gail_req}
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libxml2-devel >= %{libxml2_req}
BuildRequires:	libgnomecanvas-devel >= %{libgnomecanvsa_req}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK HTML Widget for the GNOME 2 platform.

%description -l pl
Widget GTK HTML dla platformy GNOME2.

%package devel
Summary:	Header files for GTK HTML 2
Summary(pl):	Pliki nag³ówkowe GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gail-devel >= %{gail_req}
Requires:	libxml2-devel >= %{libxml2_req}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_req}

%description devel
Header files for GTK HTML 2.

%description devel -l pl
Pliki nag³ówkowe dla GTK HTML 2.

%package static
Summary:	Static GTK HTML 2 library
Summary(pl):	Statyczna biblioteka GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	gail-static >= %{gail_req}
Requires:	libxml2-static >= %{libxml2_req}
Requires:	libgnomecanvas-static >= %{libgnomecanvas_req}

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
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
