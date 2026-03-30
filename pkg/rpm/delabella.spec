Name:     delabella
Version:  2.0
Release:  %autorelease
Summary:  2D Delaunay triangulation (dela) - super stable (bella!)
License:  MIT
URL:      https://github.com/msokalski/delabella
Source:   %{url}/archive/V%{version}/delabella-%{version}.tar.gz
Patch1:   gnu-install-dirs.patch
Patch2:   include-ctime.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc

%description
2D Exact Delaunay triangulation

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Headers and static library for delabella.

%prep
%autosetup -n delabella-%{version} -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libdelabella.so.%{version}
%{_libdir}/libdelabella.so.%(echo %{version} | cut -d. -f1)

%files devel
%{_includedir}/delabella.h
%{_libdir}/libdelabella.so

%changelog
%autochangelog
