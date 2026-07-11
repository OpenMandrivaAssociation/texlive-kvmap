%global tl_name kvmap
%global tl_revision 67201

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.5
Release:	%{tl_revision}.1
Summary:	Create Karnaugh maps with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kvmap
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kvmap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kvmap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kvmap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsmath)
Requires:	texlive(l3experimental)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package allows the creation of (even large) Karnaugh maps. It
provides a tabular-like input syntax and support for drawing bundles
(implicants) around adjacent values. It is based on an answer at
StackExchange.

