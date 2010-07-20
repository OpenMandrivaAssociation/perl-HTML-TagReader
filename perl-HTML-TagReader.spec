%define upstream_name    HTML-TagReader
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	HTML-TagReader module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
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

