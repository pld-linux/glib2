Summary:	Useful routines for 'C' programming
Summary(cs):	�ikovn� knihovna s funkcemi pro pomocn� programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine n�tzliche Library von Dienstprogramm-Funktionen
Summary(es):	Conjunto de funciones gr�ficas utilitarias
Summary(fi):	Kirjasto, jossa on ty�kalufunktioita
Summary(fr):	Biblioth�que de fonctions utilitaires
Summary(ja):	�����ʥ桼�ƥ���ƥ��ؿ��Υ饤�֥��
Summary(pl):	Biblioteka zawieraj�ca wiele u�ytecznych funkcji C
Summary(pt_BR):	Conjunto de fun��es gr�ficas utilit�rias
Summary(tr):	Yararl� ufak yordamlar kitapl���
Summary(zh_CN):	ʵ�ù��ߺ�����
Name:		glib2
Version:	2.6.0
Release:	2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/glib/2.6/glib-%{version}.tar.bz2
# Source0-md5:	649b89c8bfd152feea6db6f68b7cd54e
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-bug161668.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	gettext-devel
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	rpm-build >= 4.1-8.2
Requires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%description -l cs
�ikovn� knihovna s funkcemi pro pomocn� programy. V�vojov� knihovny a
hlavi�ky jsou v bal��ku glib-devel.

%description -l da
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de
Eine n�tzliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l es
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusi�n est�n en glib-devel.

%description -l fi
Kirjasto, jossa on ty�kalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l ja
GLib�ϥ桼�ƥ���ƥ��ؿ��򽸤᤿�����ʥ饤�֥��Ǥ������Σø����ѥ饤�֥��ϡ�
�����Ĥ���������褹��褦�߷פ���Ƥ��ꡢ¿���Υץ���फ���׵ᤵ���Ȥ��䤹��
�ؿ����󶡤��ޤ���

GLib��GDK,
GTK+¾¿���Υ��ץꥱ�����������Ѥ���롣���Υ饤�֥��˰�¸���륢�ץꥱ�������
���Τ���ˤ���glib�ѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description -l pl
Glib jest zestawem bibliotek zawieraj�cych funkcje do obs�ugi list i
drzew, funkcje mieszaj�ce, funkcje do alokacji pami�ci i du�o innych
podstawowych funkcji i r�nych struktur danych u�ywanych przez program
GIMP i wiele innych.

%description -l pt_BR
Conjunto de fun��es utilit�rias. Bibliotecas de desenvolvimento e
arquivos de inclus�o est�o em glib-devel.

%description -l tr
Yararl� yordamlar kitapl���. Geli�tirme kitapl�klar� ve ba�l�k
dosyalar� glib-devel paketinde yer almaktad�r.

%package devel
Summary:	Glib heades files, documentation
Summary(es):	Conjunto de funciones gr�ficas utilitarias para desarrollo
Summary(pl):	Pliki nag��wkowe i dokumentacja do glib
Summary(pt_BR):	Conjunto de ferramentas e biblioteca do kit de desenho do GIMP
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk-doc-common

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description devel -l es
Conjunto de funciones gr�ficas utilitarias para desarrollo.

%description devel -l ja
glib2-devel�ѥå������ˤϡ����̥饤�֥��Ȥ���ͭ����GIMP��X�饤�֥�귲
(Gtk��GDK)�򥵥ݡ��Ȥ���饤�֥������˥����ƥ��å��饤�֥��ȥإå���
�ޤޤ�Ƥ��ޤ���

�⤷GLib��Ȥäƥץ�����ȯ����ʤ�С�glib-devel�ѥå������򥤥󥹥�
���뤷�Ƥ���������

%description devel -l pl
Pliki nag��wkowe i dokumentacja do glib przydatna przy pisaniu
program�w wykorzystuj�cych t� bibliotek�.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para a biblioteca de suporte para
as bibliotecas X do GIMP, que s�o dispon�veis como bibliotecas
p�blicas. A GLIB inclui estruturas de dados gen�ricas �teis.

%package static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne glib
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static glib libraries.

%description static -l pl
Biblioteki statyczne glib.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com glib.

%prep
%setup -q -n glib-%{version}
%patch0 -p1
%patch1 -p1

%build
gtkdocize --copy
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-threads \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--enable-static \
	--enable-debug=%{?debug:yes}%{!?debug:minimum} \
	--enable-man
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang glib --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f glib.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/gettext
%attr(755,root,root) %{_datadir}/glib-2.0/gettext/mkinstalldirs
%{_datadir}/glib-2.0/gettext/po
%{_pkgconfigdir}/*
%{_libdir}/glib-2.0
%{_includedir}/*
%{_gtkdocdir}/*
%{_aclocaldir}/*
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
