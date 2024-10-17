%define upstream_name    HTML-TagReader
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	HTML-TagReader module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Image::Size)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
TagReader is a perl extension module which allows you to read html/xml
files by tag. That is: in a similar way as you can read textfiles by
line with "while(<>)" you use TagReader::getbytoken to read a file by tag.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/tr_*
%{perl_vendorlib}/*/HTML/TagReader.pm
%{perl_vendorlib}/*/auto/HTML/TagReader
%{_mandir}/*/*



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.100.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 555256
- rebuild

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 399599
- update to 1.10
- using %%perl_convert_version
- fixed license & source fields

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2009.0
+ Revision: 257205
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.08-2mdv2008.1
+ Revision: 152119
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.08-1mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.08-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.08-1mdk
- initial Mandriva package

