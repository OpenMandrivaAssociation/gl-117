%define	name	gl-117
%define	version	1.3.2
%define	rel	2
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
Summary:	%{Summary}
BuildRequires:	mesaglu-devel SDL_mixer-devel X11-devel nas-devel
BuildRequires:	smpeg-devel oggvorbis-devel mesa-common-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="GL-117"\
		longtitle="%{Summary}" \
		xdg="true"
EOF

install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat <<EOF > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=GL-117
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

install -m644 doc/%{name}.6 -D $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ
%{_mandir}/man6/%{name}.6*
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*