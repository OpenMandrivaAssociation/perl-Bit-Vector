%define upstream_name	 Bit-Vector


%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_docdir}

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	7.4
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Bit::Vector
Source0:	https://cpan.metacpan.org/modules/by-module/Bit/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Storable) >= 2.210.0
BuildRequires:	perl-devel

# Help transitioning away from perl_convert_version
Obsoletes:	%{name} = 7.400.0-8

%description
%{upstream_name} module for perl.
Bit::Vector is an efficient C library which allows you to handle
bit vectors, sets (of integers), "big integer arithmetic" and
boolean matrices, all of arbitrary sizes.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
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
