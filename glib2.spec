#
# Conditional build:
%bcond_without	apidocs         # disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	Useful routines for 'C' programming
Summary(cs.UTF-8):	Šikovná knihovna s funkcemi pro pomocné programy
Summary(da.UTF-8):	Nyttige biblioteksfunktioner
Summary(de.UTF-8):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(es.UTF-8):	Conjunto de funciones gráficas utilitarias
Summary(fi.UTF-8):	Kirjasto, jossa on työkalufunktioita
Summary(fr.UTF-8):	Bibliothèque de fonctions utilitaires
Summary(ja.UTF-8):	便利なユーティリティ関数のライブラリ
Summary(pl.UTF-8):	Biblioteka zawierająca wiele użytecznych funkcji C
Summary(pt_BR.UTF-8):	Conjunto de funções gráficas utilitárias
Summary(tr.UTF-8):	Yararlı ufak yordamlar kitaplığı
Summary(zh_CN.UTF-8):	实用工具函数库
Name:		glib2
Version:	2.12.11
Release:	3
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/glib/2.12/glib-%{version}.tar.bz2
# Source0-md5:	077a9917b673a9a0bc63f351786dde24
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-SEGV.patch
Patch2:		%{name}-noarch.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
%{?with_apidocs:BuildRequires:	gtk-doc-automake >= 1.7}
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	rpmbuild(macros) >= 1.197
%{!?with_apidocs:BuildRequires:	sed >= 4.0}
Requires:	iconv
Obsoletes:	glib2-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%description -l cs.UTF-8
Šikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavičky jsou v balíčku glib-devel.

%description -l da.UTF-8
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de.UTF-8
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l es.UTF-8
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusión están en glib-devel.

%description -l fi.UTF-8
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l ja.UTF-8
GLibはユーティリティ関数を集めた便利なライブラリです。このＣ言語用ライブラリは、
いくつかの問題を解決するよう設計されており、多くのプログラムから要求される使いやすい
関数を提供します。

GLibはGDK,
GTK+他多くのアプリケーションで利用される。このライブラリに依存するアプリケーション
等のためにこのglibパッケージをインストールしてください。

%description -l pl.UTF-8
Glib jest zestawem bibliotek zawierających funkcje do obsługi list i
drzew, funkcje mieszające, funkcje do alokacji pamięci i dużo innych
podstawowych funkcji i różnych struktur danych używanych przez program
GIMP i wiele innych.

%description -l pt_BR.UTF-8
Conjunto de funções utilitárias. Bibliotecas de desenvolvimento e
arquivos de inclusão estão em glib-devel.

%description -l tr.UTF-8
Yararlı yordamlar kitaplığı. Geliştirme kitaplıkları ve başlık
dosyaları glib-devel paketinde yer almaktadır.

%package devel
Summary:	Glib heades files, documentation
Summary(es.UTF-8):	Conjunto de funciones gráficas utilitarias para desarrollo
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do glib
Summary(pt_BR.UTF-8):	Conjunto de ferramentas e biblioteca do kit de desenho do GIMP
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description devel -l es.UTF-8
Conjunto de funciones gráficas utilitarias para desarrollo.

%description devel -l ja.UTF-8
glib2-develパッケージには、一般ライブラリとして有効なGIMPのXライブラリ群
(GtkとGDK)をサポートするライブラリ向けにスタティックライブラリとヘッダが
含まれています。

もしGLibを使ってプログラムを開発するならば、glib-develパッケージをインスト
ールしてください。

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do glib przydatna przy pisaniu
programów wykorzystujących tę bibliotekę.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para a biblioteca de suporte para
as bibliotecas X do GIMP, que são disponíveis como bibliotecas
públicas. A GLIB inclui estruturas de dados genéricas úteis.

%package static
Summary:	Static glib libraries
Summary(pl.UTF-8):	Biblioteki statyczne glib
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static glib libraries.

%description static -l pl.UTF-8
Biblioteki statyczne glib.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com glib.

%package apidocs
Summary:	Glib API documetation
Summary(pl.UTF-8):	Dokumentacja API Glib
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Glib API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API Glib.

%prep
%setup -q -n glib-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if !%{with apidocs}
sed -e '/SUBDIRS/s/docs//' -i Makefile.am
sed -e '/^docs.*Makefile$/d' -i configure.in
echo 'AC_DEFUN([GTK_DOC_CHECK],[])' >> acinclude.m4
%endif

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static \
	--enable-debug=%{?debug:yes} \
	--enable-man \
	--enable-threads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang glib20 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f glib20.lang
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
%{_aclocaldir}/*
%{?with_apidocs:%{_mandir}/man?/*}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
%endif
