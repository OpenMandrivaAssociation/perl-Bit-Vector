%define	module	Bit-Vector
%define	version	6.4
%define	release	%mkrel 4
%define	pdir	Bit

%define TEST 1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release:	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	perl-Carp-Clan

%description
%{module} module for perl.
Bit::Vector is an efficient C library which allows you to handle
bit vectors, sets (of integers), "big integer arithmetic" and
boolean matrices, all of arbitrary sizes.

%prep
%setup -q -n %{module}-%{version}
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

