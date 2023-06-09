#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : netplan
Version  : 0.106
Release  : 4
URL      : https://github.com/canonical/netplan/archive/0.106/netplan-0.106.tar.gz
Source0  : https://github.com/canonical/netplan/archive/0.106/netplan-0.106.tar.gz
Summary  : Network configuration tool using YAML
Group    : Development/Tools
License  : GPL-3.0
Requires: netplan-bin = %{version}-%{release}
Requires: netplan-data = %{version}-%{release}
Requires: netplan-lib = %{version}-%{release}
Requires: netplan-libexec = %{version}-%{release}
Requires: netplan-license = %{version}-%{release}
Requires: netplan-man = %{version}-%{release}
Requires: PyYAML
Requires: pypi-netifaces
Requires: pypi-rich
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : pandoc
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : pypi-pytest
BuildRequires : yaml-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Loosen-Python-deps.patch
Patch2: 0002-Disable-tests.patch
Patch3: 0003-Find-generate-under-usr-libexec-instead-of-lib.patch

%description
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

Currently supported backends are NetworkManager and systemd-networkd.

%package bin
Summary: bin components for the netplan package.
Group: Binaries
Requires: netplan-data = %{version}-%{release}
Requires: netplan-libexec = %{version}-%{release}
Requires: netplan-license = %{version}-%{release}

%description bin
bin components for the netplan package.


%package data
Summary: data components for the netplan package.
Group: Data

%description data
data components for the netplan package.


%package dev
Summary: dev components for the netplan package.
Group: Development
Requires: netplan-lib = %{version}-%{release}
Requires: netplan-bin = %{version}-%{release}
Requires: netplan-data = %{version}-%{release}
Provides: netplan-devel = %{version}-%{release}
Requires: netplan = %{version}-%{release}

%description dev
dev components for the netplan package.


%package doc
Summary: doc components for the netplan package.
Group: Documentation
Requires: netplan-man = %{version}-%{release}

%description doc
doc components for the netplan package.


%package lib
Summary: lib components for the netplan package.
Group: Libraries
Requires: netplan-data = %{version}-%{release}
Requires: netplan-libexec = %{version}-%{release}
Requires: netplan-license = %{version}-%{release}

%description lib
lib components for the netplan package.


%package libexec
Summary: libexec components for the netplan package.
Group: Default
Requires: netplan-license = %{version}-%{release}

%description libexec
libexec components for the netplan package.


%package license
Summary: license components for the netplan package.
Group: Default

%description license
license components for the netplan package.


%package man
Summary: man components for the netplan package.
Group: Default

%description man
man components for the netplan package.


%prep
%setup -q -n netplan-0.106
cd %{_builddir}/netplan-0.106
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683158492
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
## install_prepend content
# Something in the build is trying to symlink up 3 levels when it should be doing 4
# /builddir/build/BUILDROOT/netplan-0.106-1.x86_64/usr/lib/systemd/system-generators/../../../usr/libexec/netplan/generate
# Make sure to rm the symlink in install_append so it doesn't end up in a package!
mkdir -p %{buildroot}/usr
ln -s ../usr %{buildroot}/usr/usr
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/netplan
cp %{_builddir}/netplan-%{version}/COPYING %{buildroot}/usr/share/package-licenses/netplan/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
# Undo the weird symlink we added in install_prepend so we don't end up installing it
rm %{buildroot}/usr/usr

# Now recreate the symlink as it was intended
ln -sf ../../../libexec/netplan/generate %{buildroot}/usr/lib/systemd/system-generators/netplan

# Also remove the symlink /lib/netplan/generate, which I don't even know where it came from
rm -rf %{buildroot}/lib

# Make sure we don't create and install a /usr/sbin directory from this package -- it's a symlink in the base filesystem
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/
rmdir %{buildroot}/usr/sbin
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-generators/netplan

%files bin
%defattr(-,root,root,-)
/usr/bin/netplan

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/netplan
/usr/share/dbus-1/system-services/io.netplan.Netplan.service
/usr/share/dbus-1/system.d/io.netplan.Netplan.conf
/usr/share/netplan/netplan.script
/usr/share/netplan/netplan/__init__.py
/usr/share/netplan/netplan/_features.py
/usr/share/netplan/netplan/cli/__init__.py
/usr/share/netplan/netplan/cli/commands/__init__.py
/usr/share/netplan/netplan/cli/commands/apply.py
/usr/share/netplan/netplan/cli/commands/generate.py
/usr/share/netplan/netplan/cli/commands/get.py
/usr/share/netplan/netplan/cli/commands/info.py
/usr/share/netplan/netplan/cli/commands/ip.py
/usr/share/netplan/netplan/cli/commands/migrate.py
/usr/share/netplan/netplan/cli/commands/set.py
/usr/share/netplan/netplan/cli/commands/sriov_rebind.py
/usr/share/netplan/netplan/cli/commands/status.py
/usr/share/netplan/netplan/cli/commands/try_command.py
/usr/share/netplan/netplan/cli/core.py
/usr/share/netplan/netplan/cli/ovs.py
/usr/share/netplan/netplan/cli/sriov.py
/usr/share/netplan/netplan/cli/utils.py
/usr/share/netplan/netplan/configmanager.py
/usr/share/netplan/netplan/libnetplan.py
/usr/share/netplan/netplan/terminal.py

%files dev
%defattr(-,root,root,-)
/usr/include/netplan/netplan.h
/usr/include/netplan/parse-nm.h
/usr/include/netplan/parse.h
/usr/include/netplan/types.h
/usr/include/netplan/util.h
/usr/lib64/libnetplan.so
/usr/lib64/pkgconfig/netplan.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/netplan/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnetplan.so.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/netplan/generate
/usr/libexec/netplan/netplan-dbus

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/netplan/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/netplan.5
/usr/share/man/man8/netplan-apply.8
/usr/share/man/man8/netplan-dbus.8
/usr/share/man/man8/netplan-generate.8
/usr/share/man/man8/netplan-get.8
/usr/share/man/man8/netplan-set.8
/usr/share/man/man8/netplan-try.8
