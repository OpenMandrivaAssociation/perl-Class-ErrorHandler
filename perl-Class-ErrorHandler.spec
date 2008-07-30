%define module	Class-ErrorHandler
%define name	perl-%{module}
%define version	0.01
%define	release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Base class for error handling
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Class::ErrorHandler provides an error-handling mechanism that's generic enough
to be used as the base class for a variety of OO classes. Subclasses inherit
its two error-handling methods, error and errstr, to communicate error messages
back to the calling program.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*

