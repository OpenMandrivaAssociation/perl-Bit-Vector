%define	upstream_name	 Bit-Vector
%define	upstream_version 6.9

%define TEST 1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Carp-Clan
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl.
Bit::Vector is an efficient C library which allows you to handle
bit vectors, sets (of integers), "big integer arithmetic" and
boolean matrices, all of arbitrary sizes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod -R u+w examples

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%if %{TEST}
LANG=C %make test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc CHANGES.txt CREDITS.txt INSTALL.txt README.txt examples
%{_mandir}/man3/Bit::Vector*
%dir %{perl_vendorarch}/Bit
%{perl_vendorarch}/Bit/Vector*
%dir %{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Bit/Vector*
