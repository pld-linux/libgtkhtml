Name:		libgtkhtml
Summary:	GTk HTML widget 2
Version:	1.99.7
Release:	1
License:	GPL/LGPL
Group:		X11/Development/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+2-devel
Requires:	libxml2-devel
Requires:	gnome-vfs2-devel
Requires:	gail-devel

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME2

%description
GTK HTML Widget for the GNOME 2 platform

%package devel
Summary:	Header, docs and development libraries for atk.
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel

%package static
Summary:	Header, docs and development libraries for atk.
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static

%prep
%setup -q

%build
%configure \
	--disable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog INSTALL README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gtkhtml-2.0
%attr(755,root,root) %{_libdir}/*.??
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
