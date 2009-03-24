%define 	module	pyglet
Summary:	A cross-platform windowing and multimedia library for Python
Summary(pl.UTF-8):	Międzyplatformowa biblioteka Pythona do obsługi okien i multimediów
Name:		python-%{module}
Version:	1.1.3
Release:	1
License:	BSD/BSD
Group:		Development/Languages/Python
Source0:	http://pyglet.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	54530c20a95fffeb6c60fd4a9b073b83
URL:		http://www.pyglet.org/
BuildRequires:	python-devel >= 1:2.5
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

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
