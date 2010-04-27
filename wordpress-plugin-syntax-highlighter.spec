Summary:	Syntax Highlighter plugin for the WordPress personal publishing system
Summary(pl.UTF-8):	Wtyczka do podświetlania składni dla WordPressa
Name:		wordpress-plugin-syntax-highlighter
Version:	0
Release:	1
License:	LGPL v3
Group:		Applications/Publishing
# Extract .php file from:
# http://www.lastengine.com/wp-content/uploads/2010/01/syntax-highlighter-and-code-prettifier.zip
Source0:	%{name}.php
URL:		http://www.lastengine.com/syntax-highlighter-wordpress-plugin/
Requires:	js-syntaxhighlighter
Requires:	wordpress
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	%{_datadir}/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir		%{wordpressdir}/%{pluginssubdir}

%description
Syntax highlighter plugin for WordPress personal publishing system. It
supports following languages: Bash/shell, C#, C++, CSS, Delphi, Diff,
Groovy, JavaScript, Java, Perl, PHP, Plain Text, Python, Ruby, Scala,
SQL, Visual, Basic, XML.

%description -l pl.UTF-8
Wtyczka wzbogacająca WordPress o podświetlanie składni następujących
języków: Bash/shell, C#, C++, CSS, Delphi, Diff, Groovy, JavaScript,
Java, Perl, PHP, Plain Text, Python, Ruby, Scala, SQL, Visual, Basic,
XML.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{wordpressdir} $RPM_BUILD_ROOT%{pluginsdir}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{pluginsdir}/syntax-highlighter.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{pluginsdir}/syntax-highlighter.php
