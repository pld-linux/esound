#
# Conditional build:
# _without_alsa		- support OSS, not ALSA
# _without_libwrap	- without hosts.{access,deny} support
#
Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	DИmon audio de Enlightment
Summary(pl):	O╤wiecony Demon D╪wiЙku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	Сервер, позволяющий микшировать вывод на звуковое устройство
Summary(uk):	Сервер, що дозволя╓ м╕кширувати вив╕д на звуковий пристр╕й
Name:		esound
Version:	0.2.31
Release:	1
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	5b8349f7dd58349e626e1701f2a420af
Patch0:		%{name}-am.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://www.tux.org/~ricdude/EsounD.html
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel >= 0.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{!?_without_libwrap:BuildRequires:	libwrap-devel}
BuildRequires:	pkgconfig
Obsoletes:	libesound0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l es
El servidor de sonido esound es en proceso que permite que mЗltiples
aplicaciones compartan una misma tarjeta de sonido.

%description -l fr
Le dИmon audio de Enlightment est un processus serveur qui permets Ю
plusieures applications d'utilsier la carte son Ю la fois.

%description -l pl
"O╤wiecony demon d╪wiЙku" jest serwerem, ktСry umo©liwia korzystanie
(dzielenie) z jednej karty d╪wiЙkowej przez rС©ne aplikacje.

%description -l pt_BR
O servidor de som esound И um processo que permite que mЗltiplas
aplicaГУes compartilhem uma placa de som.

%description -l ru
EsounD (демон, обслуживающий звук, из проекта Enlightenment) может
микшировать несколько звуковых потоков в одно устройство в реальном
времени.

%description -l uk
EsounD (демон, обслуговуючий звук, з проекту Enlightenment) може
м╕кширувати к╕лька звукових поток╕в в один пристр╕й в реальному час╕.

%package devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(es):	Bibliotecas, archivos de inclusiСn, etc para desarrollar aplicaciones EsounD
Summary(fr):	BibliothХques, includes, etc pour programmer pour EsounD
Summary(pl):	Biblioteki, pliki nagЁСwkowe oraz dokumentacja
Summary(pt_BR):	Bibliotecas, arquivos de inclusЦo, etc para desenvolver aplicaГУes EsounD
Summary(ru):	Библиотеки разработки для esound
Summary(uk):	Б╕бл╕отеки розробки для esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
%{!?_without_alsa:Requires:	alsa-lib-devel}
Requires:	audiofile-devel
Obsoletes:	libesound0-devel

%description devel
Libraries, include files, etc you can use to develop EsounD
applications.

%description devel -l es
Bibliotecas, archivos de inclusiСn, etc, para que puedas desarrollar
aplicaciones que usen el servidor de sonido EsounD.

%description devel -l fr
BibliothХques, fichiers d'en-tЙtes, etc. necessaires pour Иcrire des
applications avec support EsounD

%description devel -l pl
Biblioteki, pliki nagЁСwkowe oraz dokumentacja - czyli wszystko czego
potrzebujesz do tworzenia aplikacji pod EsounD.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusЦo, etc, para que vocЙ possa
desenvolver aplicaГУes que usem o servidor de som EsounD.

%description devel -l ru
Этот пакет включает файлы хедеров и библиотеки, необходимые для
разработки приложений, использующих esound.

%description devel -l uk
Цей пакет м╕стить .h-файли та б╕бл╕отеки, необх╕дн╕ для розробки
прикладних програм, що використовують esound.

%package static
Summary:	EsounD static library
Summary(es):	Bibliotecas estАticas para desarrollar aplicaciones EsounD
Summary(pl):	Biblioteka statyczna esound
Summary(pt_BR):	Bibliotecas estАticas para desenvolver aplicaГУes EsounD
Summary(ru):	Статические библиотеки разработки для esound
Summary(uk):	Статичн╕ б╕бл╕отеки розробки для esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description static
EsounD static library.

%description static -l es
Bibliotecas estАticas para que puedas desarrollar aplicaciones que
usen el servidor de sonido EsounD.

%description static -l pl
Biblioteka statyczna esound.

%description static -l pt_BR
Bibliotecas estАticas para que vocЙ possa desenvolver aplicaГУes que
usem o servidor de som EsounD.

%description static -l ru
Этот пакет включает статические библиотеки, необходимые для разработки
приложений, использующих esound.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки
прикладних програм, що використовують esound.

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
%configure \
	--enable-ipv6 \
	--with%{?_without_libwrap:out}-libwrap \
	%{?_without_alsa:--disable-alsa}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
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
