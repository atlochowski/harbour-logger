Name:       harbour-logger-ofono
Summary:    Ofono logger
Version:    1.0.9
Release:    1
Group:      Applications/System
License:    BSD
URL:        http://github.com/monich/harbour-logger
Source0:    %{name}-%{version}.tar.bz2

Requires:   sailfishsilica-qt5
BuildRequires: pkgconfig(sailfishapp)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(mlite5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: desktop-file-utils
BuildRequires: qt5-qttools-linguist

%description
Application for gathering ofono logs

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake5 CONFIG+=ofono
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/*.desktop

# Build artifacts
rm %{buildroot}/%{_bindir}/liblogger.a
rm %{buildroot}/%{_libdir}/libharbour-lib.a
rm %{buildroot}/%{_libdir}/pkgconfig/harbour-lib.pc
rm -fr %{buildroot}/%{_includedir}/harbour-lib
rm -fr %{buildroot}/%{_datarootdir}/logger

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/translations
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Jun 10 2017 Slava Monich <slava.monich@jolla.com> 1.0.9
- Added Swedish translations
- Add /etc/hw-release to the tarball
- Automatically enable logging at startup
- Automatically reset logging on exit

* Mon Jan 23 2017 Slava Monich <slava.monich@jolla.com> 1.0.8
- Save the state of the connmans's cellular technology
- Another connectivity fix

* Wed Jan 11 2017 Slava Monich <slava.monich@jolla.com> 1.0.7
- Don't directly invoke Qt code from glib callbacks
- Make sure that verbose trace is enabled
- Save rilerror file

* Tue Oct 25 2016 Slava Monich <slava.monich@jolla.com> 1.0.6
- Save connection context configuration

* Tue Oct 25 2016 Slava Monich <slava.monich@jolla.com> 1.0.5
- Added "Fix mobile data" menu item
- Collect more ofono information

* Mon Oct 10 2016 Slava Monich <slava.monich@jolla.com> 1.0.4
- Added default email address

* Sun Oct 09 2016 Slava Monich <slava.monich@jolla.com> 1.0.3
- Compatibility with Qt 5.6

* Thu Sep 08 2016 Slava Monich <slava.monich@jolla.com> 1.0.2
- Made font size configurable

* Thu Sep 08 2016 Slava Monich <slava.monich@jolla.com> 1.0.1
- Fixed a few visual glitches
- Made screen buffer size configurable
- Added openrepos build with settings plugin

* Wed May 25 2016 Slava Monich <slava.monich@jolla.com> 1.0.0
- Initial release
