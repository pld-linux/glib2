Summary:	Useful routines for 'C' programming
Summary(cs):	©ikovná knihovna s funkcemi pro pomocné programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(fi):	Kirjasto, jossa on työkalufunktioita
Summary(fr):	Bibliothèque de fonctions utilitaires
Summary(pl):	Biblioteka zawieraj±ca wiele u¿ytecznych funkcji C
Summary(tr):	Yararlý ufak yordamlar kitaplýðý
Name:		glib2
Version:	2.0.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v2.0/glib-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%description -l cs
©ikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavièky jsou v balíèku glib-devel.

%description -l da
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l fi
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l pl
Glib jest zestawem bibliotek zawieraj±cych funkcje do obs³ugi list i
drzew, funkcje mieszaj±ce, funkcje do alokacji pamiêci i du¿o
innych podstawowych funkcji i ró¿nych struktur danych u¿ywanych przez
program GIMP i wiele innych.

%description -l tr
Yararlý yordamlar kitaplýðý. Geliþtirme kitaplýklarý ve baþlýk
dosyalarý glib-devel paketinde yer almaktadýr.

%package devel
Summary:	Glib heades files, documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do glib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do glib przydatna przy pisaniu
programów wykorzystuj±cych tê bibliotekê.

%package static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static glib libraries.

%description static -l pl
Biblioteki statyczne glib.

%prep
%setup -q -n glib-%{version}
%patch0 -p1

%build
#%{__libtoolize}
#%{__gettextize}
aclocal
%{__autoconf}
#%{__automake}

# Inside %%install gobject is linked against just built (installed)
# version of glib.
LDFLAGS="%{rpmldflags} -L%{buildroot}%{_libdir}"
%configure \
	--enable-threads \
	--enable-gtk-doc=no \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

mv -f $RPM_BUILD_ROOT%{_mandir}/man1/glib{,2}-mkenums.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/glib{,2}-genmarshal.1

%find_lang glib --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f glib.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_pkgconfigdir}/*
%{_libdir}/glib-2.0
%{_includedir}/*
%{_datadir}/glib-2.0/*
%{_datadir}/gtk-doc/html/glib
%{_datadir}/gtk-doc/html/gobject
%{_aclocaldir}/*
%{_mandir}/man?/glib*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
