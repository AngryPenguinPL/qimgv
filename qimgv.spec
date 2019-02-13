Name:           qimgv
Version:        0.7.3
Release:        1
Summary:        Simple Qt5 image viewer
License:        GPL
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}/%{name}-%{version}.tar.gz
# Add patch to fix build issue https://github.com/easymodo/qimgv/issues/63
# https://github.com/easymodo/qimgv/commit/33cccbe76736bdb6245ba4eb6d7de50473d7b3d1
#Patch0:         qimgv0.7.1-fix-build-QImageReader-del-const.patch
BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(mpv) >= 1.22.0
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ninja

%description
Qt5 image viewer also with video support.

%prep
%setup -q
#autopatch -p0

%build

%cmake -G Ninja -DVIDEO_SUPPORT=ON
%ninja_build

%install
%ninja_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

