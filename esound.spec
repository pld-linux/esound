#
# Conditional build:
# _without_libwrap	- without hosts.{access,deny} support
#
Summary:	The Enlightened Sound Daemon
Summary(es):	El servidor de sonido del Enlightenment
Summary(fr):	D�mon audio de Enlightment
Summary(pl):	O�wiecony Demon D�wi�ku
Summary(pt_BR):	O servidor de som do Enlightenment
Summary(ru):	������, ����������� ����������� ����� �� �������� ����������
Summary(uk):	������, �� ������Ѥ ͦ��������� ��צ� �� �������� �����Ҧ�
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

%package devel
Summary:	Libraries, includes, etc to develop EsounD applications
Summary(es):	Bibliotecas, archivos de inclusi�n, etc para desarrollar aplicaciones EsounD
Summary(fr):	Biblioth�ques, includes, etc pour programmer pour EsounD
Summary(pl):	Biblioteki, pliki nag��wkowe oraz dokumentacja
Summary(pt_BR):	Bibliotecas, arquivos de inclus�o, etc para desenvolver aplica��es EsounD
Summary(ru):	���������� ���������� ��� esound
Summary(uk):	��̦����� �������� ��� esound
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	audiofile-devel
Obsoletes:	libesound0-devel

%description devel
Libraries, include files, etc you can use to develop EsounD
applications.

%description devel -l es
Bibliotecas, archivos de inclusi�n, etc, para que puedas desarrollar
aplicaciones que usen el servidor de sonido EsounD.

%description devel -l fr
Biblioth�ques, fichiers d'en-t�tes, etc. necessaires pour �crire des
applications avec support EsounD

%description devel -l pl
Biblioteki, pliki nag��wkowe oraz dokumentacja - czyli wszystko czego
potrzebujesz do tworzenia aplikacji pod EsounD.

%description devel -l pt_BR
Bibliotecas, arquivos de inclus�o, etc, para que voc� possa
desenvolver aplica��es que usem o servidor de som EsounD.

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
Requires:	%{name} = %{version}

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
