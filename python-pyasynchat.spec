%define module pyasynchat
%bcond tests 1

Name:		python-pyasynchat
Summary:	Make asynchat available for Python 3.12 onwards
Version:	1.0.5
Release:	2
License:	PSF-2.0
Group:		Development/Python
URL:		https://github.com/simonrob/pyasynchat
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:	python-test
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyasyncore)
%endif

%description
This package contains the asynchat module as found in Python versions
prior to 3.12.

It is provided so that existing code relying on import asynchat is able
to continue being used without significant refactoring.

Please note that new projects should prefer to use the Python standard
library's asyncio library.

%prep -a
# lets not publish executable documents
chmod -x LICENSE README.md

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -rs
%endif

%files
%doc README.md
%license LICENSE
%{python_sitelib}/asynchat
%{python_sitelib}/%{module}-%{version}*.*-info
