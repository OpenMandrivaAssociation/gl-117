%define	name	gl-117
%define	version	1.3.2
%define	rel	6
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
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel

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
%{makeinstall_std}

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
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

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

install -m644 doc/%{name}.6 -D %{buildroot}%{_mandir}/man6/%{name}.6

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


%changelog
* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 1.3.2-6mdv2011.0
+ Revision: 635837
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-5mdv2011.0
+ Revision: 618956
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2-4mdv2010.0
+ Revision: 429209
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.3.2-3mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2008.1
+ Revision: 167886
- fix no-buildroot-tag
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Aug 17 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.2-3mdv2008.0
+ Revision: 65299
- drop debian menu
- drop buildroot & clean
- lzma compressio
- Import gl-117



* Fri Jun 30 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.3.2-2mdv2007.0
- rebuild
- update buildrequires for new x.org
- add xdg menu

* Thu May 05 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.3.2-1mdk
- 1.3.2
- lib64 fix
- %%mkrel

* Tue Dec 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3.1-1mdk
- 1.3.1
- drop P0 (fixed upstream)
- update url

* Thu Aug 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3-2mdk
- fix url

* Mon Jun 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- 1.3

* Thu Feb 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-1mdk
- 1.2

* Sun Dec 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1-1mdk
- 1.1
- fix buildrequires (lib64..)
- don't bzip2 icons in src.rpm

* Thu Oct 30 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.1-2mdk
- 1.0.1-2 (bugfix release)

* Thu Oct 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Sun Aug 24 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-1mdk
- 1.0

* Sun Jun 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.9-1mdk
- 0.9

* Fri Jun 13 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.8-2mdk
- fix macro for summary so we don't get the debug package's summary as longtitle in menu item

* Tue Apr 29 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.8-1mdk
- 0.8.8
- added FAQ
- minor fixes

* Fri Apr 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.5-4mdk
- fixed buildrequires
- remove non-existing configure options

* Wed Apr 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.5-3mdk
- removed identical readme.txt file
- added missing buildrequires

* Wed Apr 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.5-2mdk
- clean out some crap
- added man page

* Sat Apr 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.5-1mdk
- initial mdk release
