Summary:	The Enlightened Sound Daemon
Summary(es):	Demonio de sonido de Enlightment
Summary(fr):	DÈmon audio de Enlightment
Summary(pl):	O∂wiecony Demon DºwiÍku
Name:		esound
Version:	0.2.23
Release:	1
Epoch:		1
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/esound/%{name}-%{version}.tar.gz
Patch0:		%{name}-esddsp.in.patch
URL:		http://www.tux.org/~ricdude/EsounD.html
BuildRequires:	libwrap-devel
BuildRequires:	audiofile-devel >= 0.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
The Enlightened Sound Daemon is a server process that allows multiple
applications to share a single sound card.

%description -l es
El demonio de sonido de Enlightment es un proceso servidor que permite
a m·s de una aplicaciÛn de usar la tarjeta de sonido al mismo tiempo

%description -l fr
Le dÈmon audio de Enlightment est un processus serveur qui permets ‡
plusieures applications d'utilsier la carte son ‡ la fois.

%description -l pl
"O∂wiecony demon dºwiÍku" jest serwerem, ktÛry umoøliwia korzystanie
(dzielenie) z jednej karty dºwiÍkowej przez rÛøne aplikacje.

%package devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(es):	Bibliotecas, includes, etc para desarrollar programas para EsounD
Summary(fr):	BibliothËques, includes, etc pour programmer pour EsounD
Summary(pl):	Biblioteki, pliki nag≥Ûwkowe oraz dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	audiofile-devel

%description devel
Libraries, include files, etc you can use to develop EsounD
applications.

%description devel -l es
Bibliotecas, archivos *.h, etc necesarios para escribir programas con
soporte para EsounD.

%description devel -l fr
BibliothËques, fichiers d'en-tÍtes, etc. necessaires pour Ècrire des
applications avec support EsounD

%description devel -l pl
Biblioteki, pliki nag≥Ûwkowe oraz dokumentacja - czyli wszystko czego
potrzebujesz do tworzenia aplikacji pod EsounD.

%package static
Summary:	EsounD static library
Summary(pl):	Biblioteka statyczna esound
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
EsounD static library.

%description static -l pl
Biblioteka statyczna esound.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--disable-alsa \
	--with-libwrap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf README AUTHORS ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz

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

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS}.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/esd-config

%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
