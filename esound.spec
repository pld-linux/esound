Summary:	The Enlightened Sound Daemon
Summary(pl):	O¶wiecony Demon D¼wiêku
Name:		esound
Version:	0.2.12
Release:	2
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://ftp.gnome.org/pub/NOME/sources/%{name}/%{name}-%{version}.tar.gz
URL:		http://pw1.netcom.com/~ericmit/EsounD.html
BuildPrereq:	alsa-lib-devel
BuildPrereq:	audiofile-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
"O¶wiecony demon d¼wiêku" jest serwerem, który umo¿liwia korzystanie
(dzielenie) z jednej karty d¼wiêkowej przez ró¿ne aplikacje. Przeznaczony 
g³ównie dla Enlightenmenta.

%package	devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(pl):	Biblioteki, pliki nag³ówkowe oraz dokumentacja
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag³ówkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package	static
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

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

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
%attr(755,root,root) %{_bindir}/esd-config

%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.12-2]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
