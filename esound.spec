#
# Conditional build:
# _without_libwrap	- without hosts.{access,deny} support
#
Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	Démon audio de Enlightment
Summary(pl):	O¶wiecony Demon D¼wiêku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	óÅÒ×ÅÒ, ÐÏÚ×ÏÌÑÀÝÉÊ ÍÉËÛÉÒÏ×ÁÔØ ×Ù×ÏÄ ÎÁ Ú×ÕËÏ×ÏÅ ÕÓÔÒÏÊÓÔ×Ï
Summary(uk):	óÅÒ×ÅÒ, ÝÏ ÄÏÚ×ÏÌÑ¤ Í¦ËÛÉÒÕ×ÁÔÉ ×É×¦Ä ÎÁ Ú×ÕËÏ×ÉÊ ÐÒÉÓÔÒ¦Ê
Name:		esound
Version:	0.2.29
Release:	1
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.1/sources/esound/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.tux.org/~ricdude/EsounD.html
BuildRequires:	audiofile-devel >= 0.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{!?_without_libwrap:BuildRequires:	libwrap-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libesound0

%define		_sysconfdir	/etc

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
Requires:	%{name} = %{version}
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
Requires:	%{name} = %{version}

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

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal} || ( echo 'AC_DEFUN([AM_PATH_ALSA],[])' > acinclude.m4 && aclocal )
%{__autoconf}
%{__automake}
%configure \
	--disable-alsa \
	--with%{?_without_libwrap:out}-libwrap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/esd.1*
%{_mandir}/man1/esd[a-z]*.1*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
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
