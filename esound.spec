#
# Conditional build:
%bcond_without	libwrap 	# without hosts.{access,deny} support
#
Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	D�mon audio de Enlightment
Summary(pl):	O�wiecony Demon D�wi�ku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	������, ����������� ����������� ����� �� �������� ����������
Summary(uk):	������, �� ������Ѥ ͦ��������� ��צ� �� �������� �����Ҧ�
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

%description -l es
El servidor de sonido esound es en proceso que permite que m�ltiples
aplicaciones compartan una misma tarjeta de sonido.

%description -l fr
Le d�mon audio de Enlightment est un processus serveur qui permets �
plusieures applications d'utilsier la carte son � la fois.

%description -l pl
"O�wiecony demon d�wi�ku" jest serwerem, kt�ry umo�liwia korzystanie
(dzielenie) z jednej karty d�wi�kowej przez r�ne aplikacje.

%description -l pt_BR
O servidor de som esound � um processo que permite que m�ltiplas
aplica��es compartilhem uma placa de som.

%description -l ru
EsounD (�����, ������������� ����, �� ������� Enlightenment) �����
����������� ��������� �������� ������� � ���� ���������� � ��������
�������.

%description -l uk
EsounD (�����, ������������� ����, � ������� Enlightenment) ����
ͦ��������� ˦���� �������� ����˦� � ���� �����Ҧ� � ��������� ��Ӧ.

%package libs
Summary:	EsounD libraries
Summary(pl):	Biblioteki EsounD
Group:		Libraries
Obsoletes:	esound-alsa
Obsoletes:	esound-oss
Obsoletes:	libesound0

%description libs
EsounD libraries.

%description libs -l pl
Biblioteki EsounD.

%package devel
Summary:	Header files etc. to develop EsounD applications
Summary(es):	Archivos de inclusi�n, etc para desarrollar aplicaciones EsounD
Summary(fr):	Includes, etc pour programmer pour EsounD
Summary(pl):	Pliki nag��wkowe i inne do tworzenia aplikacji z u�yciem EsounD
Summary(pt_BR):	Arquivos de inclus�o, etc para desenvolver aplica��es EsounD
Summary(ru):	���������� ���������� ��� esound
Summary(uk):	��̦����� �������� ��� esound
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	alsa-lib-devel >= 1.0.0-pre1
Requires:	audiofile-devel
Obsoletes:	libesound0-devel

%description devel
Header files, etc you can use to develop EsounD applications.

%description devel -l es
Archivos de inclusi�n, etc, para que puedas desarrollar aplicaciones
que usen el servidor de sonido EsounD.

%description devel -l fr
Fichiers d'en-t�tes, etc. necessaires pour �crire des applications
avec support EsounD.

%description devel -l pl
Pliki nag��wkowe i inne potrzebne do tworzenia aplikacji
korzystaj�cych z systemu EsounD.

%description devel -l pt_BR
Arquivos de inclus�o, etc, para que voc� possa desenvolver aplica��es
que usem o servidor de som EsounD.

%description devel -l ru
���� ����� �������� ����� ������� � ����������, ����������� ���
���������� ����������, ������������ esound.

%description devel -l uk
��� ����� ͦ����� .h-����� �� ¦�̦�����, ����Ȧ�Φ ��� ��������
���������� �������, �� �������������� esound.

%package static
Summary:	EsounD static library
Summary(es):	Bibliotecas est�ticas para desarrollar aplicaciones EsounD
Summary(pl):	Biblioteka statyczna esound
Summary(pt_BR):	Bibliotecas est�ticas para desenvolver aplica��es EsounD
Summary(ru):	����������� ���������� ���������� ��� esound
Summary(uk):	������Φ ¦�̦����� �������� ��� esound
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
EsounD static library.

%description static -l es
Bibliotecas est�ticas para que puedas desarrollar aplicaciones que
usen el servidor de sonido EsounD.

%description static -l pl
Biblioteka statyczna esound.

%description static -l pt_BR
Bibliotecas est�ticas para que voc� possa desenvolver aplica��es que
usem o servidor de som EsounD.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ����������
����������, ������������ esound.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� ��������
���������� �������, �� �������������� esound.

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
