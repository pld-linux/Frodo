Summary:	Commodore 64 emulator
Summary(pl):	Emulator Commodore 64
Name:		Frodo
Version:	4.1a
Release:	3
License:	non-commercial
Group:		Applications/Emulators
Source0:	http://iphcip1.physik.uni-mainz.de/~cbauer/%{name}V4_1a.Src.tar.gz
Patch0:		%{name}-16+bpp.patch
Patch1:		%{name}-TkGui.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-joy.patch
URL:		http://www.uni-mainz.de/~bauec002/FRMain.html
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	autoconf
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Frodo V4.1 is a free, portable C64 emulator for BeOS, Unix, MacOS,
AmigaOS, RiscOS and WinNT/95 systems.

Some of the emulation's features:

This emulator focuses on the exact reproduction of special graphical
effects possible on the C64, and has therefore relatively high system
requirements. It should only be run on systems with at least a
PowerPC/Pentium/68060. Frodo is capable of running most games and
demos correctly, even those with FLI, FLD, DYCP, open borders,
multiplexed sprites, timing dependent decoders, fast loaders etc. 6510
emulation: All undocumented opcodes, 100 percent correct decimal mode,
instruction/cycle exact emulation. VIC emulation: Line-/cycle-based
emulation, all display modes, sprites with collisions/priorities, DMA
cycles, open borders, all $d011/$d016 effects. SID emulation:
Real-time digital emulation (16 bit, 44.1kHz), including filters (only
under BeOS, Linux, HP-UX, MacOS and AmigaOS). 1541 emulation: Drive
simulation in directories, .d64/x64 or .t64/LYNX files, or
processor-level 1541 emulation that works with about 95 percent of all
fast loaders and even some copy protection schemes. Other peripherals:
Keyboard and joystick (real joysticks (only under BeOS, Linux and
AmigaOS) or keyboard emulation). The full source code in C++ is
available. Frodo is freeware. Why pay >$40 for a C64 emulator?

%description -l pl
Frodo jest darmowym, przeno¶nym emulatorem C64 dla BeOS, uniksów,
MacOS, AmigaOS, RiscOS i WinNT/Win9x.

%prep
%setup -q -n Frodo
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd Src
%{__autoconf}
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
CFLAGS="$CFLAGS -DX_USE_SHM -fno-exceptions -fno-rtti -fno-implicit-templates"
%configure
%{__make} all FRODOHOME="\\\"%{_libdir}/Frodo/\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/Frodo/{64prgs,64imgs},%{_bindir}}

install Src/Frodo Src/FrodoPC Src/FrodoSC $RPM_BUILD_ROOT%{_bindir}
install TkGui.tcl "Frodo Logo" $RPM_BUILD_ROOT%{_libdir}/Frodo
install "1541 ROM" "Basic ROM" "Char ROM" "Kernal ROM" $RPM_BUILD_ROOT%{_libdir}/Frodo
install 64prgs/* $RPM_BUILD_ROOT%{_libdir}/Frodo/64prgs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES Docs/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/Frodo
