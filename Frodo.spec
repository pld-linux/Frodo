Summary:	Commodore 64 emulator
Summary(pl):	Emulator Commodore 64
Name:		Frodo
Version:	4.1b
Release:	3
License:	non-commercial
Group:		Applications/Emulators
Source0:	http://iphcip1.physik.uni-mainz.de/~cbauer/%{name}V4_1b.Src.tar.gz
# Source0-md5:	095b9f21c03204cc13f7f249e8866cd9
Patch0:		%{name}-paths.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-alpha.patch
URL:		http://www.uni-mainz.de/~bauec002/FRMain.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
Requires:	tk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frodo V4.1 is a free, portable C64 emulator for BeOS, Unix, MacOS,
AmigaOS, RiscOS and WinNT/95 systems.

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
available. Frodo is freeware.

%description -l pl
Frodo jest darmowym, przeno¶nym emulatorem C64 dla BeOS, uniksów,
MacOS, AmigaOS, RiscOS i WinNT/Win9x.

Ten emulator skupia siê na dok³adnym odtworzeniu specjalnych efektów
graficznych osi±galnych na C64, wiêc ma dosyæ du¿e wymagania dotycz±ce
systemu. Powinien byæ uruchamiany tylko na systemach z co najmniej
PowerPC/Pentium/68060. Frodo jest w stanie uruchomiæ poprawnie
wiêkszo¶æ gier i dem, nawet te z FLI, FLD, DYCP, otwartymi ramkami,
zamienianymi duszkami, dekoderami zale¿nymi od czasu, szybkimi
loaderami itp. Emulacja 6510: wszystkie nieudokumentowane instrukcje,
w pe³ni poprawny tryb dziesiêtny, dok³adna emulacja liczby cykli dla
instrukcji. Emulacja VIC: bazuj±ca na liniach lub cyklach, wszystkie
tryby wy¶wietlania, duszki z kolizjami i priorytetami, cykle DMA,
otwarte ramki, wszystkie efekty $d011/$d016. Emulacja SID: emulacja
cyfrowa w czasie rzeczywistym (16 bitów. 44.1kHz), w³±cznie z filtrami
(tylko pod BeOS-em, Linuksem, HP-UX-em, MacOS-em i AmigaOS-em).
Emulacja 1541: symulacja dysków w katalogach, plikach .d64/x64 albo
.t64/LYNX, lub emulacja 1541 na poziomie procesora, obs³uguj±ca oko³o
95%% wszystkich szybkich loaderów i nawet niektóre rodzaje
zabezpieczeñ przed kopiowaniem. Inne peryferia: klawiatura i joystick
(prawdziwe joysticki (tylko pod BeOS-em, Linuksem i AmigaOS-em) lub
emulacja na klawiaturze). Dostêpne s± pe³ne ¼ród³a w C++. Frodo jest
freeware.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd Src
%{__autoconf}
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
CFLAGS="$CFLAGS -DX_USE_SHM -fno-exceptions -fno-rtti -fno-implicit-templates"
%configure
%{__make} all \
	FRODOHOME="\\\"%{_libdir}/Frodo/\\\"" \
	CC=%{__cc} \
	CXX=%{__cxx}

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
