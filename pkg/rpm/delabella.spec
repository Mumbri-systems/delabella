Name:     delabella
Version:  2.0
Release:  %autorelease
Summary:  2D Delaunay triangulation (dela) - super stable (bella!)
License:  MIT
URL:      https://github.com/msokalski/delabella/tree/V2.0
Source:   https://github.com/Mumbri-systems/delabella/archive/refs/heads/master.zip

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
%autosetup -n delabella-master

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE

%files devel
%{_includedir}/delabella.h
%{_libdir}/libdelabella.so

%changelog
%autochangelog
