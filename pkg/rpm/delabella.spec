Name:     delabella
Version:  2.0
Release:  %autorelease
Summary:  2D Delaunay triangulation (dela) - super stable (bella!)
License:  NASA-1.3
URL:      https://github.com/msokalski/delabella/tree/V2.0
Source:   https://github.com/Mumbri-systems/delabella/archive/refs/heads/master.zip


%description
2D Exact Delaunay triangulation

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files

%doc README.md
%license LICENSE

%changelog
%autochangelog
