%define upstream_name	 Class-ErrorHandler
%define upstream_version 0.03

Summary:	Base class for error handling
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/Class-ErrorHandler-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)

%description
Class::ErrorHandler provides an error-handling mechanism that's generic enough
to be used as the base class for a variety of OO classes. Subclasses inherit
its two error-handling methods, error and errstr, to communicate error messages
back to the calling program.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes 
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*


