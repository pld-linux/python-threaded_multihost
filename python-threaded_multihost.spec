%define		module	threaded_multihost
Summary:	Helper utilities which enable Django installations to be multi-site aware.
Name:		python-threaded_multihost
Version:	1.0
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://gosatchmo.com/static/files/%{module}-%{version}_release.tar.gz
# Source0-md5:	a2bc485a2083f04a0fac4ed9993f7225
URL:		http://gosatchmo.com/apps/django-threaded-multihost/
#BuildRequires:	python-devel
#BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n sw/lib/python2.5/site-packages/%{module}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/%{module}
install * $RPM_BUILD_ROOT%{py_sitedir}/%{module}
install ../%{module}-%{version}_release-py2.5.egg-info $RPM_BUILD_ROOT%{py_sitedir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-%{version}_release-py2.5.egg-info
%endif
