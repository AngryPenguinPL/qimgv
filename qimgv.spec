#
# spec file for package qimgv
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           qimgv
Version:        0.7.1
Release:        1
Summary:        Qt5 image viewer
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Add patch to fix build issue https://github.com/easymodo/qimgv/issues/63
# https://github.com/easymodo/qimgv/commit/33cccbe76736bdb6245ba4eb6d7de50473d7b3d1
Patch0:         qimgv0.7.1-fix-build-QImageReader-del-const.patch
BuildRequires:  cmake
BuildRequires:  qmake5
#BuildRequires:  gcc-c++
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

%description
Qt5 image viewer with webm support.

%prep
%setup -q
%autopatch -p0

%build
#export CC=gcc
#export CXX=g++

%cmake
make %{?_smp_mflags}

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

