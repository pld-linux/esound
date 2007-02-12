#
# Conditional build:
%bcond_without	libwrap 	# without hosts.{access,deny} support
#
Summary:	The Enlightened Sound Daemon
Summary(es.UTF-8):   El servidor de sonido del Enlightenment
Summary(fr.UTF-8):   Démon audio de Enlightment
Summary(pl.UTF-8):   Oświecony Demon Dźwięku
Summary(pt_BR.UTF-8):   O servidor de som do Enlightenment
Summary(ru.UTF-8):   Сервер, позволяющий микшировать вывод на звуковое устройство
Summary(uk.UTF-8):   Сервер, що дозволяє мікширувати вивід на звуковий пристрій
Name:		esound
Version:	0.2.36
Release:	7
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/esound/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	3facb5aa0115cc1c31771b9ad454ae76
Patch0:		%{name}-am.patch
Patch1:		%{name}-etc_dir.patch
Patch2:		%{name}-auto_spawn.patch
URL:		http://www.tux.org/~ricdude/EsounD.html
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	audiofile-devel >= 1:0.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	libtool
%{?with_libwrap:BuildRequires:	libwrap-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l es.UTF-8
El servidor de sonido esound es en proceso que permite que múltiples
aplicaciones compartan una misma tarjeta de sonido.

%description -l fr.UTF-8
Le démon audio de Enlightment est un processus serveur qui permets à
plusieures applications d'utilsier la carte son à la fois.

%description -l pl.UTF-8
"Oświecony demon dźwięku" jest serwerem, który umożliwia korzystanie
(dzielenie) z jednej karty dźwiękowej przez różne aplikacje.

%description -l pt_BR.UTF-8
O servidor de som esound é um processo que permite que múltiplas
aplicações compartilhem uma placa de som.

%description -l ru.UTF-8
EsounD (демон, обслуживающий звук, из проекта Enlightenment) может
микшировать несколько звуковых потоков в одно устройство в реальном
времени.

%description -l uk.UTF-8
EsounD (демон, обслуговуючий звук, з проекту Enlightenment) може
мікширувати кілька звукових потоків в один пристрій в реальному часі.

%package libs
Summary:	EsounD libraries
Summary(pl.UTF-8):   Biblioteki EsounD
Group:		Libraries
Obsoletes:	esound-alsa
Obsoletes:	esound-oss
Obsoletes:	libesound0

%description libs
EsounD libraries.

%description libs -l pl.UTF-8
Biblioteki EsounD.

%package devel
Summary:	Header files etc. to develop EsounD applications
Summary(es.UTF-8):   Archivos de inclusión, etc para desarrollar aplicaciones EsounD
Summary(fr.UTF-8):   Includes, etc pour programmer pour EsounD
Summary(pl.UTF-8):   Pliki nagłówkowe i inne do tworzenia aplikacji z użyciem EsounD
Summary(pt_BR.UTF-8):   Arquivos de inclusão, etc para desenvolver aplicações EsounD
Summary(ru.UTF-8):   Библиотеки разработки для esound
Summary(uk.UTF-8):   Бібліотеки розробки для esound
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	alsa-lib-devel >= 1.0.0-pre1
Requires:	audiofile-devel
Obsoletes:	libesound0-devel

%description devel
Header files, etc you can use to develop EsounD applications.

%description devel -l es.UTF-8
Archivos de inclusión, etc, para que puedas desarrollar aplicaciones
que usen el servidor de sonido EsounD.

%description devel -l fr.UTF-8
Fichiers d'en-têtes, etc. necessaires pour écrire des applications
avec support EsounD.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne potrzebne do tworzenia aplikacji
korzystających z systemu EsounD.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão, etc, para que você possa desenvolver aplicações
que usem o servidor de som EsounD.

%description devel -l ru.UTF-8
Этот пакет включает файлы хедеров и библиотеки, необходимые для
разработки приложений, использующих esound.

%description devel -l uk.UTF-8
Цей пакет містить .h-файли та бібліотеки, необхідні для розробки
прикладних програм, що використовують esound.

%package static
Summary:	EsounD static library
Summary(es.UTF-8):   Bibliotecas estáticas para desarrollar aplicaciones EsounD
Summary(pl.UTF-8):   Biblioteka statyczna esound
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolver aplicações EsounD
Summary(ru.UTF-8):   Статические библиотеки разработки для esound
Summary(uk.UTF-8):   Статичні бібліотеки розробки для esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
EsounD static library.

%description static -l es.UTF-8
Bibliotecas estáticas para que puedas desarrollar aplicaciones que
usen el servidor de sonido EsounD.

%description static -l pl.UTF-8
Biblioteka statyczna esound.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para que você possa desenvolver aplicações que
usem o servidor de som EsounD.

%description static -l ru.UTF-8
Этот пакет включает статические библиотеки, необходимые для разработки
приложений, использующих esound.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для розробки
прикладних програм, що використовують esound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

%configure \
	--enable-ipv6 \
	--with%{!?with_libwrap:out}-libwrap \
	--enable-alsa \
	--enable-oss \
	--enable-local-sound
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TIPS TODO docs/html
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
%{_mandir}/man1/esd.1*
%{_mandir}/man1/esd[a-z]*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesd*.so.*.*

%files devel
%defattr(644,root,root,755)
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
