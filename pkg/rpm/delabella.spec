%global commit 0b8d371c28c82492d0a945f535bd7d73c467b630
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260402

Name:     delabella
Version:  2.0^%{commitdate}git%{shortcommit}
Release:  %autorelease
Summary:  2D Delaunay triangulation (dela) - super stable (bella!)
License:  MIT
URL:      https://github.com/msokalski/delabella
Source:   %{url}/archive/%{commit}/stepcode-%{shortcommit}.tar.gz

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
%autosetup -n delabella-%{commit}

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
