#
# Conditional build:
%bcond_without alsa 		# support OSS, not ALSA
%bcond_without libwrap 		# without hosts.{access,deny} support
#

%ifarch sparc sparc64
%bcond_with alsa
%endif

Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	Démon audio de Enlightment
Summary(pl):	O¶wiecony Demon D¼wiêku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	óÅÒ×ÅÒ, ÐÏÚ×ÏÌÑÀÝÉÊ ÍÉËÛÉÒÏ×ÁÔØ ×Ù×ÏÄ ÎÁ Ú×ÕËÏ×ÏÅ ÕÓÔÒÏÊÓÔ×Ï
Summary(uk):	óÅÒ×ÅÒ, ÝÏ ÄÏÚ×ÏÌÑ¤ Í¦ËÛÉÒÕ×ÁÔÉ ×É×¦Ä ÎÁ Ú×ÕËÏ×ÉÊ ÐÒÉÓÔÒ¦Ê
Name:		esound
Version:	0.2.32
Release:	1
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	b2a5e71ec8220fea1c22cc042f5f6e63
Patch0:		%{name}-am.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://www.tux.org/~ricdude/EsounD.html
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel >= 0.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{?with_libwrap:BuildRequires:	libwrap-devel}
BuildRequires:	pkgconfig
Requires:	esound-driver
Provides:	libesd.so.0
Obsoletes:	libesound0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	libesd.so.0

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l es
El servidor de sonido esound es en proceso que permite que múltiples
aplicaciones compartan una misma tarjeta de sonido.

%description -l fr
Le démon audio de Enlightment est un processus serveur qui permets à
plusieures applications d'utilsier la carte son à la fois.

%description -l pl
"O¶wiecony demon d¼wiêku" jest serwerem, który umo¿liwia korzystanie
(dzielenie) z jednej karty d¼wiêkowej przez ró¿ne aplikacje.

%description -l pt_BR
O servidor de som esound é um processo que permite que múltiplas
aplicações compartilhem uma placa de som.

%description -l ru
EsounD (ÄÅÍÏÎ, ÏÂÓÌÕÖÉ×ÁÀÝÉÊ Ú×ÕË, ÉÚ ÐÒÏÅËÔÁ Enlightenment) ÍÏÖÅÔ
ÍÉËÛÉÒÏ×ÁÔØ ÎÅÓËÏÌØËÏ Ú×ÕËÏ×ÙÈ ÐÏÔÏËÏ× × ÏÄÎÏ ÕÓÔÒÏÊÓÔ×Ï × ÒÅÁÌØÎÏÍ
×ÒÅÍÅÎÉ.

%description -l uk
EsounD (ÄÅÍÏÎ, ÏÂÓÌÕÇÏ×ÕÀÞÉÊ Ú×ÕË, Ú ÐÒÏÅËÔÕ Enlightenment) ÍÏÖÅ
Í¦ËÛÉÒÕ×ÁÔÉ Ë¦ÌØËÁ Ú×ÕËÏ×ÉÈ ÐÏÔÏË¦× × ÏÄÉÎ ÐÒÉÓÔÒ¦Ê × ÒÅÁÌØÎÏÍÕ ÞÁÓ¦.

%package devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(es):	Bibliotecas, archivos de inclusión, etc para desarrollar aplicaciones EsounD
Summary(fr):	Bibliothèques, includes, etc pour programmer pour EsounD
Summary(pl):	Biblioteki, pliki nag³ówkowe oraz dokumentacja
Summary(pt_BR):	Bibliotecas, arquivos de inclusão, etc para desenvolver aplicações EsounD
Summary(ru):	âÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ esound
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÒÏÚÒÏÂËÉ ÄÌÑ esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
%{?with_alsa:Requires:	alsa-lib-devel}
Requires:	audiofile-devel
Obsoletes:	libesound0-devel

%description devel
Libraries, include files, etc you can use to develop EsounD
applications.

%description devel -l es
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones que usen el servidor de sonido EsounD.

%description devel -l fr
Bibliothèques, fichiers d'en-têtes, etc. necessaires pour écrire des
applications avec support EsounD

%description devel -l pl
Biblioteki, pliki nag³ówkowe oraz dokumentacja - czyli wszystko czego
potrzebujesz do tworzenia aplikacji pod EsounD.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusão, etc, para que você possa
desenvolver aplicações que usem o servidor de som EsounD.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ ÆÁÊÌÙ ÈÅÄÅÒÏ× É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ
ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ, ÉÓÐÏÌØÚÕÀÝÉÈ esound.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ .h-ÆÁÊÌÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ
ÐÒÉËÌÁÄÎÉÈ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ esound.

%package static
Summary:	EsounD static library
Summary(es):	Bibliotecas estáticas para desarrollar aplicaciones EsounD
Summary(pl):	Biblioteka statyczna esound
Summary(pt_BR):	Bibliotecas estáticas para desenvolver aplicações EsounD
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ esound
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÒÏÚÒÏÂËÉ ÄÌÑ esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description static
EsounD static library.

%description static -l es
Bibliotecas estáticas para que puedas desarrollar aplicaciones que
usen el servidor de sonido EsounD.

%description static -l pl
Biblioteka statyczna esound.

%description static -l pt_BR
Bibliotecas estáticas para que você possa desenvolver aplicações que
usem o servidor de som EsounD.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ÐÒÉÌÏÖÅÎÉÊ, ÉÓÐÏÌØÚÕÀÝÉÈ esound.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ
ÐÒÉËÌÁÄÎÉÈ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ esound.

%package oss
Summary:	EsounD OSS driver
Summary(pl):	Sterownik OSS dla EsoundD
Group:		Libraries
Requires(post):	/sbin/ldconfig
Requires(post):	fileutils
Requires:	%{name} = %{epoch}:%{version}
Provides:	esound-driver
Conflicts:	esound-alsa

%description oss
EsounD OSS driver.

%description oss -l pl
Sterownik OSS dla EsoundD.

%package alsa
Summary:	EsounD ALSA driver
Summary(pl):	Sterownik ALSA dla EsoundD
Group:		Libraries
Requires(post):	/sbin/ldconfig
Requires(post):	fileutils
Requires:	%{name} = %{epoch}:%{version}
Provides:	esound-driver
Conflicts:	esound-oss

%description alsa
EsounD ALSA driver.

%description alsa -l pl
Sterownik ALSA dla EsoundD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%if %{with alsa}
%configure \
	--enable-ipv6 \
	--with%{!?with_libwrap:out}-libwrap \
	--enable-alsa
%{__make}
cp -f .libs/libesd.so.%{version} libesd-alsa.so.%{version}
%{__make} clean
%endif

%configure \
	--enable-ipv6 \
	--with%{!?with_libwrap:out}-libwrap \
	--disable-alsa
%{__make}
cp -f .libs/libesd.so.%{version} libesd-oss.so.%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

install libesd-*.so.*.* $RPM_BUILD_ROOT%{_libdir}
> $RPM_BUILD_ROOT%{_libdir}/libesd.so.%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post oss
ln -fs libesd-oss.so.%{version} %{_libdir}/libesd.so.%{version}
/sbin/ldconfig

%postun oss -p /sbin/ldconfig

%post alsa
ln -fs libesd-alsa.so.%{version} %{_libdir}/libesd.so.%{version}
/sbin/ldconfig

%postun alsa -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TIPS docs/html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esd.conf
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
%attr(755,root,root) %{_libdir}/libesddsp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libesd.so.%{version}
%{_mandir}/man1/esd.1*
%{_mandir}/man1/esd[a-z]*.1*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/esd-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*
%{_pkgconfigdir}/esound*
%{_mandir}/man1/esd-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesd-oss.so.%{version}

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesd-alsa.so.%{version}
%endif
