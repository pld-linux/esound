Summary:	The Enlightened Sound Daemon
Summary(pl):	O�wiecony Demon D�wi�ku
Name:		esound
Version:	0.2.12
Release:	6
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://ftp.gnome.org/pub/NOME/sources/%{name}/%{name}-%{version}.tar.gz
Patch:		esound-sparc.patch
URL:		http://pw1.netcom.com/~ericmit/EsounD.html
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
"O�wiecony demon d�wi�ku" jest serwerem, kt�ry umo�liwia korzystanie
(dzielenie) z jednej karty d�wi�kowej przez r�ne aplikacje. Przeznaczony 
g��wnie dla Enlightenmenta.

%package devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(pl):	Biblioteki, pliki nag��wkowe oraz dokumentacja
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag��wkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package static
Summary:	EsounD static library
Summary(pl):	Biblioteka statyczna esound
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
EsounD static library.

%description -l pl static
Biblioteka statyczna esound.

%prep
%setup -q
%patch -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README AUTHORS ChangeLog NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%config(noreplace) %verify(not md5 mtime size) /etc/esd.conf
%attr(755,root,root) %{_bindir}/esd
%attr(755,root,root) %{_bindir}/esdcat
%attr(755,root,root) %{_bindir}/esdctl
%attr(755,root,root) %{_bindir}/esddsp
%attr(755,root,root) %{_bindir}/esdfilt
%attr(755,root,root) %{_bindir}/esdloop
%attr(755,root,root) %{_bindir}/esdmon
%attr(755,root,root) %{_bindir}/esdplay
%attr(755,root,root) %{_bindir}/esdrec
%attr(755,root,root) %{_bindir}/esdsample

%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS}.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/esd-config

%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
