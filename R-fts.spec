%global packname  fts
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.7.7
Release:          3
Summary:          R interface to tslib (a time series library in c++)
Group:            Sciences/Mathematics
License:          GPL-3
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-utils R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils R-stats
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
fast operations for time series objects

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.7-1
+ Revision: 775345
- Import R-fts
- Import R-fts

