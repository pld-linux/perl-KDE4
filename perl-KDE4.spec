%define         state          stable
%define         orgname         perlkde
%define         qtver           4.8.0

# Conditional build:
%bcond_with	tests		# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	KDE4 - A Perl module interface to KDE4
Summary(pl.UTF-8):	KDE4 - interfejs Perla do KDE4
Name:		perl-KDE4
Version:	4.14.3
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://download.kde.org/%{state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c94a719d680707dae5b35a9ebba1a9f0
URL:		http://www.kde.org/
# BuildRequires:	sonnet-devel
BuildRequires:	akonadi-devel
BuildRequires:	attica-devel
BuildRequires:	automoc4
BuildRequires:	kde4-kate-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	kde4-okular-devel
BuildRequires:	kde4-smokekde-devel >= %{version}
BuildRequires:	perl-Qt4-devel >= %{version}
BuildRequires:	soprano-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(.*_internal)

%description
This module provides bindings to the KDE 4 libraries for Perl.

%description -l pl.UTF-8
Moduł dostarcza dowiązania do KDE4 4 dla Perla.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCUSTOM_PERL_SITE_ARCH_DIR=%{perl_vendorarch} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kperlpluginfactory.so
%{perl_vendorarch}/*.pm
%dir  %{perl_vendorarch}/auto/Akonadi
%dir  %{perl_vendorarch}/auto/Attica
%dir  %{perl_vendorarch}/auto/KDECore4
%dir  %{perl_vendorarch}/auto/KDEUi4
%dir  %{perl_vendorarch}/auto/KFile
%dir  %{perl_vendorarch}/auto/KHTML
%dir  %{perl_vendorarch}/auto/KIO4
%dir  %{perl_vendorarch}/auto/KNewStuff2
%dir  %{perl_vendorarch}/auto/KNewStuff3
%dir  %{perl_vendorarch}/auto/KParts
%dir  %{perl_vendorarch}/auto/KTextEditor
%dir  %{perl_vendorarch}/auto/KUtils
%dir  %{perl_vendorarch}/auto/Kate
%dir  %{perl_vendorarch}/auto/Nepomuk
%dir  %{perl_vendorarch}/auto/NepomukQuery
%dir  %{perl_vendorarch}/auto/Okular
%dir  %{perl_vendorarch}/auto/Plasma4
%dir  %{perl_vendorarch}/auto/Solid
%dir  %{perl_vendorarch}/auto/Soprano
%dir  %{perl_vendorarch}/auto/SopranoClient
%dir  %{perl_vendorarch}/auto/SopranoServer
%attr(755,root,root) %{perl_vendorarch}/auto/Akonadi/Akonadi.so
%attr(755,root,root) %{perl_vendorarch}/auto/Attica/Attica.so
%attr(755,root,root) %{perl_vendorarch}/auto/KDECore4/KDECore4.so
%attr(755,root,root) %{perl_vendorarch}/auto/KDEUi4/KDEUi4.so
%attr(755,root,root) %{perl_vendorarch}/auto/KFile/KFile.so
%attr(755,root,root) %{perl_vendorarch}/auto/KHTML/KHTML.so
%attr(755,root,root) %{perl_vendorarch}/auto/KIO4/KIO4.so
%attr(755,root,root) %{perl_vendorarch}/auto/KNewStuff2/KNewStuff2.so
%attr(755,root,root) %{perl_vendorarch}/auto/KNewStuff3/KNewStuff3.so
%attr(755,root,root) %{perl_vendorarch}/auto/KParts/KParts.so
%attr(755,root,root) %{perl_vendorarch}/auto/KTextEditor/KTextEditor.so
%attr(755,root,root) %{perl_vendorarch}/auto/KUtils/KUtils.so
%attr(755,root,root) %{perl_vendorarch}/auto/Kate/Kate.so
%attr(755,root,root) %{perl_vendorarch}/auto/Nepomuk/Nepomuk.so
%attr(755,root,root) %{perl_vendorarch}/auto/NepomukQuery/NepomukQuery.so
%attr(755,root,root) %{perl_vendorarch}/auto/Okular/Okular.so
%attr(755,root,root) %{perl_vendorarch}/auto/Plasma4/Plasma4.so
%attr(755,root,root) %{perl_vendorarch}/auto/Solid/Solid.so
%attr(755,root,root) %{perl_vendorarch}/auto/Soprano/Soprano.so
%attr(755,root,root) %{perl_vendorarch}/auto/SopranoClient/SopranoClient.so
%attr(755,root,root) %{perl_vendorarch}/auto/SopranoServer/SopranoServer.so
