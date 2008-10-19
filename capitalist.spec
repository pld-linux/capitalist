#
Summary:	Server for the Monopoly®-like board game
Summary(pl.UTF-8):	Serwer gry planszowej typu Monopoly®.
Name:		capitalist
Version:	0.3.1
Release:	0.1
License:	GPL v2
Group:		Applications/Games/Boards
Source0:	http://dl.sourceforge.net/capitalist/%{name}-%{version}.tar.gz
# Source0-md5:	f93ee3ce9d29eba657e087762d8fd663
Patch0:		%{name}-autotools.patch
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
URL:		http://kapitalist.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kapitalist is a Monopoly®-like board game for 2-8 players. Walk around
the board, buy properties, receive rent from your competitors, try to
get monopolies to build houses and hotels on them and finally be the
richest on the board.

This package contains a server. You should also install the kapitalist
package.

%description -l pl.UTF-8
Kapitalist jest grą planszową typu Monopoly® dla 2-8 graczy.
Przemierzaj planszę, kupuj nieruchomości, otrzymuj renty od
współzawodników, spróbuj zdobyć wyłączność na budowę domów i hoteli na
poszczególnych posiadłościach, ostatecznie zostań najbogatszym z
graczy na planszy.

Ten pakiet zawiera serwer. Aby móc grać powinieneś również
zainstalować pakiet kapitalist.

%package doc
Summary:	Documentaion for capitalist
Summary(pl.UTF-8):	Dokumentacja kapitalist
Group:		Documentation

%description doc
Documentaion for capitalist.

%description doc -l pl.UTF-8
Dokumentacja capitalist.

%prep
%setup -q

%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_docdir}/%{name}-doc-%{version}/html}

install capitalist/capitalist $RPM_BUILD_ROOT%{_bindir}
install capitalist/docs/capitalist.6 $RPM_BUILD_ROOT%{_mandir}/man6/capitalist.6
install capitalist/docs/en/index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index.html
install capitalist/docs/en/index-1.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-1.html
install capitalist/docs/en/index-2.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-2.html
install capitalist/docs/en/index-3.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-3.html
install capitalist/docs/en/index-4.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-4.html
install capitalist/docs/en/index-5.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-5.html
install capitalist/docs/en/index-6.html $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/html/index-6.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/capitalist
%{_mandir}/man6/capitalist.6*

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
