Summary:     The Enlightened Sound Daemon
Summary(pl): O¶wiecony Demon D¼wiêku ;)
Name:        esound
Version:     0.2.4
Release:     3
Copyright:   GPL
Group:       Daemons
Source0:     ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.tar.gz
URL:         http://pw1.netcom.com/~ericmit/EsounD.html
BuildRoot:   /tmp/%{name}-%{version}-root

%description 
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
O¶wiecony demon d¼wiêku ;) jest serwerem, który umo¿liwia korzystanie
(dzielenie) z jednej karty d¼wiêkowej przez ró¿ne aplikacje. Przeznaczony 
g³ównie dla Enlightenmenta.

%package devel
Summary:     Header files etc to develop EsounD applications
Summary(pl): Pliki nag³ówkowe oraz dokumentacja
Group:       Libraries
Requires:    %{name} = %{version}

%description devel
Header files etc you can use to develop EsounD applications.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package static
Summary:     Static EsounD librarires
Summary(pl): Biblioteki statyczne EsounD
Group:       Libraries
Requires:    %{name}-devel = %{version}

%description static
Static EsounD librarires.

%description -l pl static
Biblioteki statyczne EsounD.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 \
	--includedir=/usr/X11R6/include/X11  
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog EsounD.html NEWS README TIPS TODO
%attr(0711, root, root) /usr/X11R6/bin/*
%attr(0755, root, root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/X11/*

%files static
/usr/X11R6/lib/*.a

%changelog
* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.4-3]
- added static subpackage,
- /sbin/ldconfig in %post{un} is now runed as -p parameter,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- INSTALL and COPYING removed from %doc.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-2]
- build against Tornado,
- added pl translation,
- changed prefix to /usr/X11R6 (for enlightenment location).
- minor modifications of spec file.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
