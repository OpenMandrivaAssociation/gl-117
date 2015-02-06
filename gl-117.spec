Summary:	Action flight simulator
Name:		gl-117
Version:	1.3.2
Release:	8
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.heptargon.de/
Source0:	http://prdownloads.sourceforge.net/gl-117/%{name}-%{version}-src.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)

%description
GL-117 is an action flight simulator for Linux/Unix and MSWindows.
Enter the Eagle Squadron and succeed in several challenging missions
leading though different landscapes. Five predefined levels of video
quality and an amount of viewing ranges let you perfectly adjust the
game to the performance of your system. Joystick, mouse,
sound effects, music...

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ
%{_mandir}/man6/%{name}.6*
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-src

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}
%make

%install
%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=GL-117
Comment=Action flight simulator
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

install -m644 doc/%{name}.6 -D %{buildroot}%{_mandir}/man6/%{name}.6


