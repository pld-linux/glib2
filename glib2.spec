Summary:	Useful routines for 'C' programming
Summary(cs):	©ikovná knihovna s funkcemi pro pomocné programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(fi):	Kirjasto, jossa on työkalufunktioita
Summary(fr):	Bibliothèque de fonctions utilitaires
Summary(pl):	Biblioteka zawieraj±ca wiele u¿ytecznych funkcji C
Summary(tr):	Yararlý ufak yordamlar kitaplýðý
Name:		glib2
Version:	1.3.6
Release:	7
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.3/glib-%{version}.tar.gz
URL:		http://www.gtk.org/
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

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
Glib jest zestawem bibliotek zawieraj±cych funkcje do obs³ugi list,
drzewek, funkcji mieszaj±cych, funkcji do alokacji pamiêci i wielu
innych podstawowych funkcji i ró¿nych struktur danych u¿ywanych przez
program GIMP i wiele innch.

%description -l tr
Yararlý yordamlar kitaplýðý. Geliþtirme kitaplýklarý ve baþlýk
dosyalarý glib-devel paketinde yer almaktadýr.

%package devel
Summary:	Glib heades files, documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do glib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.13
Requires:	automake >= 1.4
Requires:	libtool	 >= 1.3.2 

%description devel
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do glib przydatna przy pisaniu
programów wykorzystuj±cych tê bibliotekê.

%package static
Summary:	Static glib libraries
Summary(pl):	Biblioteki statyczne do glib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static glib libraries.

%description -l pl static
Biblioteki statyczne do glib.

%prep
%setup -q -n glib-%{version}

%build
gettextize --copy --force
autoconf
# Inside %%install gobject is linked against just built (installed)
# version of glib.
CFLAGS="-L%{buildroot}%{_libdir}"
export CFLAGS
%configure \
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}
	
mv $RPM_BUILD_ROOT%{_mandir}/man1/glib{,2}-mkenums.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/glib{,2}-genmarshal.1

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_libdir}/glib-2.0
%{_includedir}/*
%{_datadir}/gtk-doc/html/glib
%{_datadir}/gtk-doc/html/gobject
%{_aclocaldir}/*

#%{_infodir}/glib.info*

%{_mandir}/man1/glib*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
