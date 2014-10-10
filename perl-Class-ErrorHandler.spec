%define upstream_name	 Class-ErrorHandler
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Base class for error handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build)
BuildRequires:	perl-devel
BuildArch:  noarch

%description
Class::ErrorHandler provides an error-handling mechanism that's generic enough
to be used as the base class for a variety of OO classes. Subclasses inherit
its two error-handling methods, error and errstr, to communicate error messages
back to the calling program.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.yml MYMETA.yml README.md
%{perl_vendorlib}/Class/*
%{_mandir}/*/*


