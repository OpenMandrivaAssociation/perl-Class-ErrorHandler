%define upstream_name	 Class-ErrorHandler
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Base class for error handling
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::ErrorHandler provides an error-handling mechanism that's generic enough
to be used as the base class for a variety of OO classes. Subclasses inherit
its two error-handling methods, error and errstr, to communicate error messages
back to the calling program.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-5mdv2012.0
+ Revision: 765085
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4
+ Revision: 763528
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3
+ Revision: 676619
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 676514
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 406874
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.01-5mdv2009.0
+ Revision: 255950
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.01-3mdv2008.1
+ Revision: 136683
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdv2008.0
+ Revision: 86107
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:35:05 (58390)
- mkrel

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:32:49 (58383)
Import perl-Class-ErrorHandler

* Tue Jun 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.01-1mdk
- Initial Mandriva release.

