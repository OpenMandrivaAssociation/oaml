%define major   1
%define libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Name:           oaml
Version:        1.3.4
Release:        1
Summary:        Open Adaptive Music Library
Group:          System/Libraries
License:        MIT
URL:            https://oamldev.github.io
Source0:        https://github.com/oamldev/oaml/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         oaml-1.2-git-shared-library-name.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbisfile)

%description
OAML is a library the makes it easy to implement adaptive music in games.

#----------------------------------------------------------------------

%package -n %{libname}
Summary:        Open Adaptive Music Library
Group:          System/Libraries

%description -n %{libname}
OAML is a library the makes it easy to implement adaptive music in games.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

#----------------------------------------------------------------------

%package -n %{devname}
Summary:        Development files for OAML
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package is contains the development library and headers for OAML,
the Open Adaptive Music Library.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITYPLUGIN=OFF
%make_build

%install
%make_install -C Build
