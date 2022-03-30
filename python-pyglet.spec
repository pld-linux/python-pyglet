#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# unit tests (display required)

%define		module	pyglet
Summary:	A cross-platform windowing and multimedia library for Python
Summary(pl.UTF-8):	Międzyplatformowa biblioteka Pythona do obsługi okien i multimediów
Name:		python-%{module}
Version:	1.4.4
Release:	6
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/pyglet/
Source0:	https://files.pythonhosted.org/packages/source/p/pyglet/%{module}-%{version}.zip
# Source0-md5:	ebd53b60f55b5d50e63f86e7df121e7a
URL:		http://www.pyglet.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	OpenGL >= 3
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	OpenGL >= 3
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyglet provides an object-oriented programming interface for
developing games and other visually-rich applications.

%description -l pl.UTF-8
pyglet dostarcza interfejs do programowania zorientowanego obiektowo
dla rozwoju gier i innych aplikacji wizualnych.

%package -n python3-%{module}
Summary:	A cross-platform windowing and multimedia library for Python
Summary(pl.UTF-8):	Międzyplatformowa biblioteka Pythona do obsługi okien i multimediów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
pyglet provides an object-oriented programming interface for
developing games and other visually-rich applications.

%description -n python3-%{module} -l pl.UTF-8
pyglet dostarcza interfejs do programowania zorientowanego obiektowo
dla rozwoju gier i innych aplikacji wizualnych.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NOTICE README.rst RELEASE_NOTES
%{py_sitescriptdir}/pyglet
%{py_sitescriptdir}/pyglet-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NOTICE README.rst RELEASE_NOTES
%{py3_sitescriptdir}/pyglet
%{py3_sitescriptdir}/pyglet-%{version}-py*.egg-info
%endif
