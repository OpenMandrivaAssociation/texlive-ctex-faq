Name:		texlive-ctex-faq
Version:	15878
Release:	1
Summary:	LaTeX FAQ by the Chinese TeX Society (ctex.org)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/ctex-faq
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Most questions were collected on the bbs.ctex.org forum, and
were answered in detail by the author.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/ctex-faq/README
%doc %{_texmfdistdir}/doc/latex/ctex-faq/ctex-faq.pdf
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/ctex-faq.sty
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/ctex-faq.tex
%doc %{_texmfdistdir}/doc/latex/ctex-faq/src/make.bat

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
