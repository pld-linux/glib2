#
# Conditional build:
%bcond_without	apidocs         # disable gtk-doc
%bcond_without	static_libs	# don't build static library
%bcond_with	selinux		# gio with SELinux support
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
Version:	2.22.3
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib/2.22/glib-%{version}.tar.bz2
# Source0-md5:	25b043b208883194c57219e41a230a29
Patch0:		%{name}-makefile.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.11}
%{?with_apidocs:BuildRequires:	gtk-doc-automake >= 1.11}
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pcre-devel >= 7.8
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.16.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
%{!?with_apidocs:BuildRequires:	sed >= 4.0}
Requires:	iconv
Requires:	pcre >= 7.8
Provides:	glib2-libs
Obsoletes:	glib2-libs
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLib
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
GLib jest zestawem bibliotek zawierających funkcje do obsługi list i
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
Summary:	GLib heades files, documentation
Summary(es.UTF-8):	Conjunto de funciones gráficas utilitarias para desarrollo
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GLib
Summary(pt_BR.UTF-8):	Conjunto de ferramentas e biblioteca do kit de desenho do GIMP
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pcre-devel >= 7.8
# gio only
%{?with_selinux:Requires:	libselinux-devel}

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLib includes generally useful data
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
Pliki nagłówkowe i dokumentacja do GLib przydatna przy pisaniu
programów wykorzystujących tę bibliotekę.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para a biblioteca de suporte para
as bibliotecas X do GIMP, que são disponíveis como bibliotecas
públicas. A GLib inclui estruturas de dados genéricas úteis.

%package static
Summary:	Static GLib libraries
Summary(pl.UTF-8):	Biblioteki statyczne GLib
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com GLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static GLib libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GLib.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com GLib.

%package apidocs
Summary:	GLib API documetation
Summary(pl.UTF-8):	Dokumentacja API GLib
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GLib API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API GLib.

%prep
%setup -q -n glib-%{version}
%patch0 -p1

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
	--%{?with_selinux:en}%{!?with_selinux:dis}able-selinux \
	--%{?with_static_libs:en}%{!?with_static_libs:dis}able-static \
	--enable-debug=%{?debug:yes} \
	--enable-man \
	--enable-threads \
	--with-pcre=system

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/libgiofam.{la,a}

%find_lang glib20

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f glib20.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/libgio-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgio-2.0.so.0
%attr(755,root,root) %{_libdir}/libglib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglib-2.0.so.0
%attr(755,root,root) %{_libdir}/libgmodule-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmodule-2.0.so.0
%attr(755,root,root) %{_libdir}/libgobject-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgobject-2.0.so.0
%attr(755,root,root) %{_libdir}/libgthread-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgthread-2.0.so.0
%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%attr(755,root,root) %{_libdir}/gio/modules/libgiofam.so

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/glib-genmarshal
%attr(755,root,root) %{_bindir}/glib-gettextize
%attr(755,root,root) %{_bindir}/glib-mkenums
%attr(755,root,root) %{_bindir}/gobject-query
%attr(755,root,root) %{_bindir}/gtester
%attr(755,root,root) %{_bindir}/gtester-report
%attr(755,root,root) %{_libdir}/libgio-2.0.so
%attr(755,root,root) %{_libdir}/libglib-2.0.so
%attr(755,root,root) %{_libdir}/libgmodule-2.0.so
%attr(755,root,root) %{_libdir}/libgobject-2.0.so
%attr(755,root,root) %{_libdir}/libgthread-2.0.so
%{_libdir}/libgio-2.0.la
%{_libdir}/libglib-2.0.la
%{_libdir}/libgmodule-2.0.la
%{_libdir}/libgobject-2.0.la
%{_libdir}/libgthread-2.0.la
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/gettext
%attr(755,root,root) %{_datadir}/glib-2.0/gettext/mkinstalldirs
%{_datadir}/glib-2.0/gettext/po
%{_pkgconfigdir}/gio-2.0.pc
%{_pkgconfigdir}/gio-unix-2.0.pc
%{_pkgconfigdir}/glib-2.0.pc
%{_pkgconfigdir}/gmodule-2.0.pc
%{_pkgconfigdir}/gmodule-export-2.0.pc
%{_pkgconfigdir}/gmodule-no-export-2.0.pc
%{_pkgconfigdir}/gobject-2.0.pc
%{_pkgconfigdir}/gthread-2.0.pc
%{_libdir}/glib-2.0
%{_includedir}/gio-unix-2.0
%{_includedir}/glib-2.0
%{_aclocaldir}/glib-2.0.m4
%{_aclocaldir}/glib-gettext.m4
%if %{with apidocs}
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*
%endif

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgio-2.0.a
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gio
%{_gtkdocdir}/glib
%{_gtkdocdir}/gobject
%endif
