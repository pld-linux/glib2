# TODO: use -Dmultiarch for arch-dependent binaries? (like gio-querymodules or gio-launch-desktop)
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
%bcond_without	static_libs	# static library
%bcond_without	selinux		# SELinux support in gio
%bcond_with	sysprof		# sysprof tracing support
%bcond_without	systemtap	# systemtap/dtrace tracing support

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
Version:	2.74.5
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/glib/2.74/glib-%{version}.tar.xz
# Source0-md5:	7561501d9f63f3418ddb23d2903cc968
Patch0:		%{name}-python_shebang.patch
Patch1:		gtk-doc-build.patch
URL:		https://www.gtk.org/
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	elfutils-devel
BuildRequires:	gettext-tools
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with apidocs}
BuildRequires:	gtk-doc >= 1.32.1
%endif
BuildRequires:	libffi-devel >= 3.0.0
BuildRequires:	libmount-devel >= 2.28
%{?with_selinux:BuildRequires:	libselinux-devel >= 2.2}
BuildRequires:	libstdc++-devel
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pcre2-8-devel >= 10.32
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.16
# in case of separate libelf (elfutils don't provide .pc file)
#BuildRequires:	pkgconfig(libelf) >= 0.8.12
BuildRequires:	pkgconfig(libffi) >= 3.0.0
BuildRequires:	python3 >= 1:3.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
%{?with_sysprof:BuildRequires:	sysprof-devel >= 3.38.0}
%{?with_systemtap:BuildRequires:	systemtap-sdt-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	iconv
Requires:	libmount >= 2.28
%{?with_selinux:Requires:	libselinux >= 2.2}
Requires:	pcre2-8 >= 10.32
Suggests:	gvfs
Provides:	glib2-libs
Obsoletes:	glib2-libs < 1:2.12.11-3
# see https://bugzilla.xfce.org/show_bug.cgi?id=9709
Conflicts:	xfce4-session < 4.10.0-5
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
いくつかの問題を解決するよう設計されており、多くのプログラムから要求される使いやすい 関数を提供します。

GLibはGDK, GTK+他多くのアプリケーションで利用される。このライブラリに依存するアプリケーション
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
Requires:	libffi-devel >= 3.0.0
Requires:	libmount-devel >= 2.28
Requires:	pcre2-8-devel >= 10.32
Requires:	python3-modules >= 1:3.5
# gio only
%{?with_selinux:Requires:	libselinux-devel >= 2.2}
Requires:	zlib-devel

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLib includes generally useful data
structures.

%description devel -l es.UTF-8
Conjunto de funciones gráficas utilitarias para desarrollo.

%description devel -l ja.UTF-8
glib2-develパッケージには、一般ライブラリとして有効なGIMPのXライブラリ群
(GtkとGDK)をサポートするライブラリ向けにスタティックライブラリとヘッダが 含まれています。

もしGLibを使ってプログラムを開発するならば、glib-develパッケージをインスト ールしてください。

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
Requires:	pcre2-8-static

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
BuildArch:	noarch

%description apidocs
GLib API documetation.

%description apidocs -l pl.UTF-8
Dokumentacja API GLib.

%package gdb
Summary:	GDB Python pretty printers for GObject/GLib types
Summary(pl.UTF-8):	Skrypty Pythona dla GDB do ładnego wypisywania typów GObject/GLib
Group:		Development/Debuggers
Requires:	gdb

%description gdb
GDB Python pretty printers for GObject/GLib types. This includes
support for GObject pointer pretty printing and signal frame
compression in backtraces.

%description gdb -l pl.UTF-8
Skrypty Pythona dla GDB do ładnego wypisywania typów GObject/GLib.
Obejmują także ładne wypisywanie wskaźników GObject oraz kompresję
ramek sygnagłów w zrzutach wywołań (backtrace).

%package -n bash-completion-gio
Summary:	bash-completion for gio utilities
Summary(pl.UTF-8):	Bashowe uzupełnianie nazw dla narzędzi gio
Group:		Applications/Shells
Requires:	bash-completion >= 1:2.0
Obsoletes:	bash-completion-gdbus < 1:2.26.0-4
BuildArch:	noarch

%description -n bash-completion-gio
bash-completion for gio utilities: gdbus and gsettings.

%description -n bash-completion-gio -l pl.UTF-8
Bashowe uzupełnianie nazw dla narzędzi gio: gdbus i gsettings.

%package -n systemtap-glib2
Summary:	systemtap/dtrace probes for GLib 2
Summary(pl.UTF-8):	Sondy systemtap/dtrace dla GLib 2
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	systemtap-client

%description -n systemtap-glib2
systemtap/dtrace probes for GLib 2.

%description -n systemtap-glib2 -l pl.UTF-8
Sondy systemtap/dtrace dla GLib 2.

%prep
%setup -q -n glib-%{version}
%patch0 -p1
%patch1 -p1

%build
%meson build \
	%{?debug:--debug} \
	-Ddtrace=%{__true_false systemtap} \
	-Dsystemtap=%{__true_false systemtap} \
%ifarch %{ix86}
	%{?with_systemtap:-Dtapset_install_dir=%{_datadir}/systemtap/tapset/i386} \
%endif
	-Dgtk_doc=%{__true_false apidocs} \
	-Dselinux=%{?with_selinux:enabled}%{!?with_selinux:disabled} \
	%{?with_sysprof:-Dsysprof=enabled} \
	-Dman=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gio/modules

%ninja_install -C build

> $RPM_BUILD_ROOT%{_libdir}/gio/modules/giomodule.cache
> $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/gschemas.compiled

%py3_comp $RPM_BUILD_ROOT%{_datadir}/glib-2.0/gdb
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/glib-2.0/gdb

# adjust for compatibility with names supported by glibc
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang glib20

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules || :

%postun	-p /sbin/ldconfig

%files -f glib20.lang
%defattr(644,root,root,755)
%doc README.md NEWS SECURITY.md
%attr(755,root,root) %{_bindir}/gapplication
%attr(755,root,root) %{_bindir}/gdbus
%attr(755,root,root) %{_bindir}/gio
%attr(755,root,root) %{_bindir}/gio-querymodules
%attr(755,root,root) %{_bindir}/glib-compile-schemas
%attr(755,root,root) %{_bindir}/gsettings
%attr(755,root,root) %{_libexecdir}/gio-launch-desktop
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
%ghost %{_libdir}/gio/modules/giomodule.cache
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%ghost %{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_mandir}/man1/gapplication.1*
%{_mandir}/man1/gdbus.1*
%{_mandir}/man1/gio.1*
%{_mandir}/man1/gio-querymodules.1*
%{_mandir}/man1/glib-compile-schemas.1*
%{_mandir}/man1/gsettings.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdbus-codegen
%attr(755,root,root) %{_bindir}/glib-compile-resources
%attr(755,root,root) %{_bindir}/glib-genmarshal
%attr(755,root,root) %{_bindir}/glib-gettextize
%attr(755,root,root) %{_bindir}/glib-mkenums
%attr(755,root,root) %{_bindir}/gobject-query
%attr(755,root,root) %{_bindir}/gresource
%attr(755,root,root) %{_bindir}/gtester
%attr(755,root,root) %{_bindir}/gtester-report
%attr(755,root,root) %{_libdir}/libgio-2.0.so
%attr(755,root,root) %{_libdir}/libglib-2.0.so
%attr(755,root,root) %{_libdir}/libgmodule-2.0.so
%attr(755,root,root) %{_libdir}/libgobject-2.0.so
%attr(755,root,root) %{_libdir}/libgthread-2.0.so
%{_libdir}/glib-2.0
%{_includedir}/gio-unix-2.0
%{_includedir}/glib-2.0
%dir %{_datadir}/glib-2.0/codegen
%{_datadir}/glib-2.0/codegen/*.py*
%dir %{_datadir}/glib-2.0/gettext
%{_datadir}/glib-2.0/gettext/po
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/valgrind
%{_datadir}/gettext/its/gschema.its
%{_datadir}/gettext/its/gschema.loc
%{_pkgconfigdir}/gio-2.0.pc
%{_pkgconfigdir}/gio-unix-2.0.pc
%{_pkgconfigdir}/glib-2.0.pc
%{_pkgconfigdir}/gmodule-2.0.pc
%{_pkgconfigdir}/gmodule-export-2.0.pc
%{_pkgconfigdir}/gmodule-no-export-2.0.pc
%{_pkgconfigdir}/gobject-2.0.pc
%{_pkgconfigdir}/gthread-2.0.pc
%{_aclocaldir}/glib-2.0.m4
%{_aclocaldir}/glib-gettext.m4
%{_aclocaldir}/gsettings.m4
%{_mandir}/man1/gdbus-codegen.1*
%{_mandir}/man1/glib-compile-resources.1*
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gresource.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*

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

%files gdb
%defattr(644,root,root,755)
%{_datadir}/gdb/auto-load/usr/%{_lib}/libglib-2.0.so.*.*.*-gdb.py
%{_datadir}/gdb/auto-load/usr/%{_lib}/libgobject-2.0.so.*.*.*-gdb.py
%{_datadir}/glib-2.0/gdb

%files -n bash-completion-gio
%defattr(644,root,root,755)
%{bash_compdir}/gapplication
%{bash_compdir}/gdbus
%{bash_compdir}/gio
%{bash_compdir}/gresource
%{bash_compdir}/gsettings

%if %{with systemtap}
%files -n systemtap-glib2
%defattr(644,root,root,755)
%{_datadir}/systemtap/tapset/*/libgio-2.0*.stp
%{_datadir}/systemtap/tapset/*/libglib-2.0*.stp
%{_datadir}/systemtap/tapset/*/libgobject-2.0*.stp
%endif
