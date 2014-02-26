#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyglet
Summary:	A cross-platform windowing and multimedia library for Python
Summary(pl.UTF-8):	Międzyplatformowa biblioteka Pythona do obsługi okien i multimediów
Name:		python-%{module}
Version:	1.1.4
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pyglet.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	b2363642dc3832e95dc4e63a6793467f
URL:		http://www.pyglet.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyOpenAL
Requires:	python-PyOpenGL
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
Requires:	python3-PyOpenAL
Requires:	python3-PyOpenGL

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
%{__python} setup.py build --build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG NOTICE README PKG-INFO doc examples
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pyglet/*.py[co]
%dir %{py_sitescriptdir}/%{module}/app
%{py_sitescriptdir}/pyglet/app/*
%dir %{py_sitescriptdir}/%{module}/font
%{py_sitescriptdir}/pyglet/font/*
%dir %{py_sitescriptdir}/%{module}/gl
%{py_sitescriptdir}/pyglet/gl/*
%dir %{py_sitescriptdir}/%{module}/graphics
%{py_sitescriptdir}/pyglet/graphics/*
%dir %{py_sitescriptdir}/%{module}/image
%{py_sitescriptdir}/pyglet/image/*
%dir %{py_sitescriptdir}/%{module}/media
%{py_sitescriptdir}/pyglet/media/*
%dir %{py_sitescriptdir}/%{module}/text
%{py_sitescriptdir}/pyglet/text/*
%dir %{py_sitescriptdir}/%{module}/window
%{py_sitescriptdir}/pyglet/window/*
%{py_sitescriptdir}/*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG NOTICE README PKG-INFO doc examples
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*.egg-info
%endif
