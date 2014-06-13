%define upstream_name	 Bit-Vector
%define upstream_version 7.3

%define TEST 1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Bit/Bit-Vector-%{upstream_version}.tar.gz

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

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%if %{TEST}
LANG=C %make test
%endif

%install
%makeinstall_std

%files
%doc CHANGES.txt CREDITS.txt INSTALL.txt README.txt examples
%dir %{perl_vendorarch}/Bit
%{perl_vendorarch}/Bit/Vector*
%dir %{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Bit/Vector*
%{_mandir}/man3/Bit::Vector*


