#
# Conditional build:
%bcond_without alsa 		# support OSS, not ALSA
%bcond_without libwrap 		# without hosts.{access,deny} support

%define _noautoprov libesd.so.0

Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	DИmon audio de Enlightment
Summary(pl):	O╤wiecony Demon D╪wiЙku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	Сервер, позволяющий микшировать вывод на звуковое устройство
Summary(uk):	Сервер, що дозволя╓ м╕кширувати вив╕д на звуковий пристр╕й
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
%{?with_alsa:Requires:	alsa-lib-devel}
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

%package oss
Summary:	EsounD OSS driver
Summary(pl):	Sterownik OSS dla EsoundD
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig
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
Requires(post,postun):	/sbin/ldconfig
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
%configure \
	--enable-ipv6 \
	--with%{!?with_libwrap:out}-libwrap \
	--disable-alsa
%{__make}
cp -f .libs/libesd.so.%{version} libesd-oss.so.%{version}

%if %{with alsa}
%{__make} clean
%configure \
	--enable-ipv6 \
	--with%{!?with_libwrap:out}-libwrap \
	--enable-alsa
%{__make}
cp -f .libs/libesd.so.%{version} libesd-alsa.so.%{version}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/libesd.so.*.*
install libesd-*.so.*.* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post oss
ln -fs libesd-oss.so.%{version} %{_libdir}/libesd.so.%{version}
/sbin/ldconfig

%postun oss
rm -f %{_libdir}/libesd.so.%{version}
/sbin/ldconfig

%post alsa
ln -fs libesd-alsa.so.%{version} %{_libdir}/libesd.so.%{version}
/sbin/ldconfig

%postun alsa
rm -f %{_libdir}/libesd.so.%{version}
/sbin/ldconfig


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
