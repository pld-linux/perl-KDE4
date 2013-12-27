%define         _state          stable
%define         orgname         perlkde
%define         qtver           4.8.0

# Conditional build:
%bcond_with	tests		# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	KDE4 - A Perl module interface to KDE4
Summary(pl.UTF-8):	KDE4 - interfejs Perla do KDE4
Name:		perl-KDE4
Version:	4.12.0
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6798dbcba3f6d265ce015c5e896aa0ad
URL:		http://www.kde.org/
# BuildRequires:	sonnet-devel
BuildRequires:	akonadi-devel
BuildRequires:	attica-devel
BuildRequires:	kde4-kate-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	kde4-okular-devel
BuildRequires:	kde4-smokekde-devel >= %{version}
BuildRequires:	perl-Qt4-devel >= %{version}
BuildRequires:	soprano-devel
BuildRequires:	xz
BuildRequires:	tar >= 1:1.22
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
	../
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
%dir %{perl_vendorarch}/auto
%dir %{perl_vendorarch}/auto/*
%attr(755,root,root)  %{perl_vendorarch}/auto/*/*.so
