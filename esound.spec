Summary:     The Enlightened Sound Daemon
Summary(pl): O¶wiecony Demon D¼wiêku ;)
Name:        esound
Version:     0.2.4
Release:     4
Copyright:   GPL
Group:       Daemons
Source:      ftp://ftp.enlightenment.org/pub/enlightenment/enlightenment/%{name}-%{version}.tar.gz
URL:         http://pw1.netcom.com/~ericmit/EsounD.html
BuildRoot:   /tmp/%{name}-%{version}-%{release}-root

%description 
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
O¶wiecony demon d¼wiêku ;) jest serwerem, który umo¿liwia korzystanie
(dzielenie) z jednej karty d¼wiêkowej przez ró¿ne aplikacje. Przeznaczony 
g³ównie dla Enlightenmenta.

%package devel
Summary:     Libraries, includes, etc to develop EsounD applications
Summary(pl): Biblioteki, pliki nag³ówkowe oraz dokumentacja
Group:       Libraries
Requires:    %{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag³ówkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package static
Summary:     EsounD static library
Summary(pl): Biblioteka statyczna esound
Group:       Libraries
Requires:    %{name}-devel = %{version}

%description static
EsounD static library.

%description -l pl static
Biblioteka statyczna esound.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*.so.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/X11R6/bin/*
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog EsounD.html NEWS README 
%attr(755, root, root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Oct 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.4-4]
- corrected base Source URL,
- added striping shared libraries,
- all %doc moved to devel,
- /sbin/ldconfig in %post{un} is now runed as -p parameter.

* Sun Oct 04 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-3]
- fixed pl translation,
- added static subpackage.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-2]
- added pl translation,
- changed prefix to /usr/X11R6 (for enlightenment location).
- minor modifications of spec file.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
