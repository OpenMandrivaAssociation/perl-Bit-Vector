%define upstream_name	 Bit-Vector
%define upstream_version 7.2

%define TEST 1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Storable) >= 2.210.0
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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc CHANGES.txt CREDITS.txt INSTALL.txt README.txt examples
%{_mandir}/man3/Bit::Vector*
%dir %{perl_vendorarch}/Bit
%{perl_vendorarch}/Bit/Vector*
%dir %{perl_vendorarch}/auto/Bit
%{perl_vendorarch}/auto/Bit/Vector*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 7.100.0-7mdv2012.0
+ Revision: 765075
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 7.100.0-6
+ Revision: 763491
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 7.100.0-5
+ Revision: 667036
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 7.100.0-4mdv2011.0
+ Revision: 564362
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 7.100.0-3mdv2011.0
+ Revision: 555686
- rebuild

* Wed Mar 03 2010 Jérôme Quelin <jquelin@mandriva.org> 7.100.0-2mdv2010.1
+ Revision: 513799
- buildrequires min storable version

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 7.100.0-1mdv2010.1
+ Revision: 460790
- update to 7.1

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 7.0.0-1mdv2010.0
+ Revision: 420853
- update to 7.0

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 6.900.0-1mdv2010.0
+ Revision: 416946
- update to 6.9

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 6.600.0-1mdv2010.0
+ Revision: 410565
- update to 6.6

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 6.4-7mdv2009.1
+ Revision: 351678
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 6.4-6mdv2009.0
+ Revision: 223568
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 6.4-5mdv2008.1
+ Revision: 151390
- rebuild for perl-5.10.0

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 6.4-4mdv2008.1
+ Revision: 136664
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 6.4-4mdv2008.0
+ Revision: 23418
- rebuild


* Sat Jan 21 2006 Luca Berra <bluca@vodka.it> 6.4-3mdk
Rebuild for new perl

* Sun Nov 21 2004 Stefan van der Eijk <stefan@mandrake.org> 6.4-2mdk
- BuildRequires

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 6.4-1mdk
- New version 6.4

* Thu Feb 12 2004 Luca Berra <bluca@vodka.it> 6.3-4mdk
- rebuild for perl 5.8.3

* Tue Dec 30 2003 Luca Berra <bluca@vodka.it> 6.3-3mdk
- add parent dirs (distriblint)
- fixed permissions on examples

* Wed Oct 15 2003 Luca Berra <bluca@vodka.it> 6.3-2mdk
- added examples to documentation

* Sun Oct 05 2003 Luca Berra <bluca@vodka.it> 6.3-1mdk
- Initial build.

