Summary:     The Enlightened Sound Daemon
Summary(pl): O�wiecony Demon D�wi�ku ;)
Name:        esound
Version:     0.2.6
Release:     1
Copyright:   GPL
Group:       Daemons
Source:      ftp://ftp.enlightenment.org/pub/enlightenment/%{name}-%{version}.tar.gz
URL:         http://pw1.netcom.com/~ericmit/EsounD.html
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l pl
O�wiecony demon d�wi�ku ;) jest serwerem, kt�ry umo�liwia korzystanie
(dzielenie) z jednej karty d�wi�kowej przez r�ne aplikacje. Przeznaczony 
g��wnie dla Enlightenmenta.

%package devel
Summary:     Libraries, includes, etc to develop EsounD applications
Summary(pl): Biblioteki, pliki nag��wkowe oraz dokumentacja
Group:       Libraries
Requires:    %{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag��wkowe oraz dokumentacja - czyli wszystko czego 
potrzebujesz do tworzenia aplikacji pod EsounD.

%package static
Summary:     EsounD static library
Summary(pl): Biblioteka statyczna esound
Group:       Libraries
Requires:    %{name} = %{version}

%description static
EsounD static library.

%description -l pl static
Biblioteka statyczna esound.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*.so.*.*} ||

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README 
%attr(755, root, root) /usr/X11R6/bin/esd
%attr(755, root, root) /usr/X11R6/bin/esdcat
%attr(755, root, root) /usr/X11R6/bin/esdctl
%attr(755, root, root) /usr/X11R6/bin/esddsp
%attr(755, root, root) /usr/X11R6/bin/esdfilt
%attr(755, root, root) /usr/X11R6/bin/esdloop
%attr(755, root, root) /usr/X11R6/bin/esdmon
%attr(755, root, root) /usr/X11R6/bin/esdrec
%attr(755, root, root) /usr/X11R6/bin/esdsample
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS
%attr(755, root, root) /usr/X11R6/lib/lib*.so
%attr(755, root, root) /usr/X11R6/bin/esd-config
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/*.a

%changelog
* Mon Nov  2 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.6-1]
- added -n %%{name} %setup parameter,
- added ignoring errors on striping binaries,
- added striping shared libraries,
- removed packing lib*.so.* sym links,
- esd-config moved to devel,
- some %doc moved to devel,
- /sbin/ldconfig is now runed as -p parameter in %post{un}.

* Sun Oct 04 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-3]
- fixed pl translation,
- added static subpackage.

* Mon Jul 20 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.2.4-2]
- added pl translation,
- changed prefix to /usr/X11R6 (for enlightenment location).
- minor modifications of spec file.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
