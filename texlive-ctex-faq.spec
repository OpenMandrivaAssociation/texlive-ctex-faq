%global tl_name ctex-faq
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX FAQ by the Chinese TeX Society (ctex.org)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/ctex-faq
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctex-faq.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Most questions were collected on the bbs.ctex.org forum, and were
answered in detail by the author.

