%define	name	gl-117
%define	version	1.3.2
%define	rel	3
%define	release	%mkrel %{rel}
%define	Summary	Action flight simulator

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.heptargon.de/
Source0:	http://prdownloads.sourceforge.net/gl-117/%{name}-%{version}-src.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL
Group:		Games/Arcade
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	%{Summary}
BuildRequires:	mesaglu-devel SDL_mixer-devel X11-devel nas-devel
BuildRequires:	smpeg-devel oggvorbis-devel mesa-common-devel

%description
GL-117 is an action flight simulator for Linux/Unix and MSWindows.
Enter the Eagle Squadron and succeed in several challanging missions
leading though different landscapes. Five predefined levels of video
quality and an amount of viewing ranges let you perfectly adjust the
game to the performance of your system. Joystick, mouse,
sound effects, music... 

%prep
%setup -q -n %{name}-%{version}-src

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat <<EOF > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=GL-117
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

install -m644 doc/%{name}.6 -D $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ
%{_mandir}/man6/%{name}.6*
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*
