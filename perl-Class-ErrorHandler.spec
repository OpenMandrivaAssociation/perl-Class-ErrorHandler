%define upstream_name	 Class-ErrorHandler
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    3

Summary:    Base class for error handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/tokuhirom/Class-ErrorHandler
Source0:    https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Class-ErrorHandler-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN::Meta)
BuildRequires: perl(Module::Build)
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-CBuilder
BuildArch:  noarch

%description
Class::ErrorHandler provides an error-handling mechanism that's generic enough
to be used as the base class for a variety of OO classes. Subclasses inherit
its two error-handling methods, error and errstr, to communicate error messages
back to the calling program.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%install
%make_install

%files
%doc Changes META.yml MYMETA.yml README.md
%{perl_vendorlib}/Class/*
%{_mandir}/*/*


