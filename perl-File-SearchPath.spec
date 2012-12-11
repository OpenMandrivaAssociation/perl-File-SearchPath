%define upstream_name    File-SearchPath
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Search for a file in an environment variable path
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJENNESS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module provides the ability to search a path-like environment variable for
a file (that does not necessarily have to be an executable).

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
%doc README
%{perl_vendorlib}/File/SearchPath.pm
%{_mandir}/man3/File::SearchPath.3pm*

%changelog
* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 612362
- new version

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 403179
- rebuild using %%perl_convert_version

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 345100
- update to new version 0.05

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 268510
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 194852
- update to new version 0.03
- update to new version 0.03

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2008.1
+ Revision: 104410
- import perl-File-SearchPath


* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2008.1
- initial Mandriva package 
