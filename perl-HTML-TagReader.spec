%define real_name HTML-TagReader

Summary:	HTML-TagReader module for perl 
Name:		perl-%{real_name}
Version:	1.08
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Image-Size
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
TagReader is a perl extension module which allows you to read html/xml
files by tag. That is: in a similar way as you can read textfiles by
line with "while(<>)" you use TagReader::getbytoken to read a file by tag.

%prep
%setup -q -n %{real_name}-%{version} 

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


