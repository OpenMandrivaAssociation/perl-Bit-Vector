%define upstream_name	 Bit-Vector
%define upstream_version 7.4


%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_docdir}

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Bit/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Storable) >= 2.210.0
BuildRequires:	perl-devel

%description
%{upstream_name} module for perl.
Bit::Vector is an efficient C library which allows you to handle
bit vectors, sets (of integers), "big integer arithmetic" and
boolean matrices, all of arbitrary sizes.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
chmod -R u+w examples
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' examples/benchmk1.pl
perl -pi -e 's|^#!perl\b|#!%{__perl}|' \
    examples/{benchmk{2,3},primes,SetObject}.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%install
%make_install

%files
%doc CHANGES.txt CREDITS.txt INSTALL.txt README.txt examples
%dir %{perl_vendorarch}/Bit
%{perl_vendorarch}/Bit/Vector*
%dir %{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Bit/Vector*
%{_mandir}/man3/Bit::Vector*
