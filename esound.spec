Summary:	The Enlightened Sound Daemon
Summary(pl):	O鈍iecony Demon D德i瘯u ;)
Name:		esound
Version:	0.2.12
Release:	1
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
O鈍iecony demon d德i瘯u ;) jest serwerem, kt鏎y umo磧iwia korzystanie
(dzielenie) z jednej karty d德i瘯owej przez r騜ne aplikacje. Przeznaczony 
g堯wnie dla Enlightenmenta.

%package	devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(pl):	Biblioteki, pliki nag堯wkowe oraz dokumentacja
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop EsounD applications.

%description -l pl devel
Biblioteki, pliki nag堯wkowe oraz dokumentacja - czyli wszystko czego 
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
./configure %{_target} \
	--prefix=/usr \
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
%attr(755,root,root) /usr/bin/esd
%attr(755,root,root) /usr/bin/esdcat
%attr(755,root,root) /usr/bin/esdctl
%attr(755,root,root) /usr/bin/esddsp
%attr(755,root,root) /usr/bin/esdfilt
%attr(755,root,root) /usr/bin/esdloop
%attr(755,root,root) /usr/bin/esdmon
%attr(755,root,root) /usr/bin/esdplay
%attr(755,root,root) /usr/bin/esdrec
%attr(755,root,root) /usr/bin/esdsample

%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS}.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) /usr/bin/esd-config

/usr/include/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Sat Apr 24 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.12-1]
- added BuildPrereq: for alsa-lib-devel, audiofile-devel,
- added /usr/bin/esdplay to main,
- added /etc/esd.conf,
- recompiles on new rpm.

* Wed Mar 10 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.8-2]
- removed "Requires: libaudiofile".

* Sat Feb 27 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.8-1]
- changed Group in devel and static to Development/Libraries,
- fixed Group(pl) in main,
- changed base Source url.

* Tue Jan 05 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.7-1d]
- changed prefix to /usr (this is not X11 stuff),
- added "Requires: libaudiofile = 0.1.5",
- removed -n %%{name} from %setup.

* Mon Nov  2 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.2.6-1]
- added -n %%{name} %setup parameter,
- added ignoring errors on stripping binaries,
- added stripping shared libraries,
- removed packing lib*.so.* sym links,
- esd-config moved to devel,
- some %doc moved to devel,
- /sbin/ldconfig is now runed as -p parameter in %post{un}.

* Sun Oct 04 1998 Wojtek 奸usarczyk <wojtek@shadow.eu.org>
  [0.2.4-3]
- fixed pl translation,
- added static subpackage.

* Mon Jul 20 1998 Wojtek 奸usarczyk <wojtek@shadow.eu.org>
  [0.2.4-2]
- added pl translation,
- changed prefix to /usr/X11R6 (for enlightenment location).
- minor modifications of spec file,
- build against GNU libc-2.1.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>
- First try at an RPM
