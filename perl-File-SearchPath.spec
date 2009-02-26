%define real_name File-SearchPath

Summary:	Search for a file in an environment variable path
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJENNESS/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides the ability to search a path-like environment variable for
a file (that does not necessarily have to be an executable).

%prep

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/File/SearchPath.pm
%attr(0644,root,root) %{_mandir}/man3/File::SearchPath.3pm*

