# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	RRD
%define		pnam	Editor
%include	/usr/lib/rpm/macros.perl
Summary:	Portable, standalone (no need for RRDs.pm) tool to create and edit RRD files
Name:		perl-RRD-Editor
Version:	0.16
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RRD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	41d2d4feec7dbe748cde9aee1343debb
URL:		http://search.cpan.org/dist/RRD-Editor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RRD:Editor implements most of the functionality of RRDTOOL, apart from
graphing, plus adds some new editing and portability features. It aims
to be portable and self-contained (no need for RRDs.pm).

RRD::Editor provides the ability to add/delete DSs and RRAs and to
get/set most of the parameters in DSs and RRAs (renaming, resizing
etc). It also allows the data values stored in each RRA to be
inspected and changed individually. That is, it provides almost
complete control over the contents of an RRD.

The RRD files created by RRDTOOL use a binary format (let's call it
native-double) that is not portable across platforms. In addition to
this file format, RRD:Editor provides two new portable file formats
(portable-double and portable-single) that allow the exchange of
files. RRD::Editor can freely convert RRD files between these three
formats (native-double,portable-double and portable-single).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/RRD
%{_mandir}/man3/*.3*
