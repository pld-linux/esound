Summary:	The Enlightened Sound Daemon
Summary(pl):	O¶wiecony Demon D¼wiêku ;)
Name:		esound
Version:	0.2.7
Release:	3d
Copyright:	GPL
Group:		Daemons
Group(pl):	Demony
#######		ftp://ftp.enlightenment.org/pub/enlightenment
Source:		%{name}-%{version}.tar.gz
Requires:	libaudiofile = 0.1.5
URL:		http://pw1.netcom.com/~ericmit/EsounD.html
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
O¶wiecony demon d¼wiêku ;) jest serwerem, który umo¿liwia korzystanie
(dzielenie) z jednej karty d¼wiêkowej przez ró¿ne aplikacje. Przeznaczony 
g³ównie dla Enlightenmenta.

%package	devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(pl):	Biblioteki, pliki nag³ówkowe oraz dokumentacja
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag³ówkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package	static
Summary:	EsounD static library
Summary(pl):	Biblioteka statyczna esound
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description static
EsounD static library.

%description -l pl static
Biblioteka statyczna esound.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

chmod 755 $RPM_BUILD_ROOT/usr/lib/lib*.so.*
strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

bzip2 -9 README AUTHORS ChangeLog NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.bz2

%attr(755,root,root) /usr/bin/esd
%attr(755,root,root) /usr/bin/esdcat
%attr(755,root,root) /usr/bin/esdctl
%attr(755,root,root) /usr/bin/esddsp
%attr(755,root,root) /usr/bin/esdfilt
%attr(755,root,root) /usr/bin/esdloop
%attr(755,root,root) /usr/bin/esdmon
%attr(755,root,root) /usr/bin/esdrec
%attr(755,root,root) /usr/bin/esdsample

%attr(755,root,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS.bz2 ChangeLog.bz2 NEWS.bz2

%attr(755,root,root) /usr/lib/lib*.so
%attr(755,root,root) /usr/bin/esd-config

/usr/include/*
/usr/share/aclocal/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.7-1d]
- changed prefix to /usr (this is not X11 stuff),
- added "Requires: libaudiofile = 0.1.5",
- removed -n %%{name} from %setup.

* Mon Nov  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.6-1]
- added -n %%{name} %setup parameter,
- added ignoring errors on stripping binaries,
- added stripping shared libraries,
- removed packing lib*.so.* sym links,
- esd-config moved to devel,
- some %doc moved to devel,
- /sbin/ldconfig is now runed as -p parameter in %post{un}.

* Sun Oct 04 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-3]
- fixed pl translation,
- added static subpackage.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-2]
- added pl translation,
- changed prefix to /usr/X11R6 (for enlightenment location).
- minor modifications of spec file,
- build against GNU libc-2.1.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
