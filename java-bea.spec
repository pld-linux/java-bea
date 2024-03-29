%define		fversion	%(echo %{version} |tr r _)
Summary:	WebLogic JRockit
Summary(pl.UTF-8):	Środowisko WebLogic JRockit
Name:		java-bea
Version:	1.4.2r04
Release:	0.1.1
License:	restricted, non-distributable
Group:		Development/Languages/Java
# download directly from http://commerce.bea.com/showproduct.jsp?family=WLJR&major=JR142SDK&minor=0
%ifarch %{ix86}
Source0:	jrockit-j2sdk%{fversion}-linux-ia32.bin
# NoSource0-md5: 81d0511feb32e7b7d61f7c07ee0b15e9
%endif
%ifarch ia64
Source0:	jrockit-j2sdk%{fversion}-linux-ipf.bin
# NoSource0-md5: 70ba79bdbf8cd2ba62f0fb99058c0ee9
%endif
Source1:	%{name}.xml
NoSource:	0
URL:		http://www.bea.com/
BuildRequires:	XFree86-libs
BuildRequires:	rpm-build >= 4.3-0.20040107.21
Requires:	%{name}-jre = %{version}-%{release}
Requires:	java-shared
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	java-sun
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java-sun
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	javadir		%{_libdir}/java
%define	jredir		%{_libdir}/java/jre
%define	netscape4dir	/usr/%{_lib}/netscape
%define	mozilladir	/usr/%{_lib}/mozilla
%define	firefoxdir	/usr/%{_lib}/mozilla-firefox

# rpm doesn't like strange version definitions provided by Sun's libs
#%%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
# the rest is because -jdbc wants unixODBC-devel(?)
#%%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libodbcinst.so' 'libodbc.so'
# don't depend on other JRE/JDK installed on build host
#%%define		_noautoreqdep	libjava.so libjvm.so

%description
Java Development Kit for Linux.

%description -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package jre-jdbc
Summary:	JDBC files for Sun Java
Summary(pl.UTF-8):	Pliki JDBC dla Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	libodbc.so.1
Requires:	libodbcinst.so.1
Provides:	%{name}-jdbc

%description jre-jdbc
This package contains JDBC files for Sun Java.

%description jre-jdbc -l pl.UTF-8
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	XFree86-libs
Requires:	java-jre-tools
Requires:	jpackage-utils
Provides:	jaas = %{version}
Provides:	java
Provides:	java1.4
Provides:	javaws = %{version}
Provides:	jce = %{version}
Provides:	jdbc-stdext = %{version}
Provides:	jdbc-stdext = 3.0
Provides:	jndi = %{version}
Provides:	jndi-cos = %{version}
Provides:	jndi-dns = %{version}
Provides:	jndi-ldap = %{version}
Provides:	jndi-rmi = %{version}
Provides:	jre = %{version}
Provides:	jsse = %{version}
Obsoletes:	jaas
Obsoletes:	java-blackdown-jre
Obsoletes:	java-sun-jre
Obsoletes:	jce
Obsoletes:	jdbc-stdext
Obsoletes:	jndi
Obsoletes:	jndi-provider-cosnaming
Obsoletes:	jndi-provider-dns
Obsoletes:	jndi-provider-ldap
Obsoletes:	jndi-provider-rmiregistry
Obsoletes:	jre
Obsoletes:	jsse

%description jre
Java Runtime Environment for Linux.

%description jre -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	%{name}-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	jar
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-shared

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package jre-tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	java-jre-tools

%description jre-tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description jre-tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Obsoletes:	java-blackdown-demos
Obsoletes:	jdk-demos

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package -n netscape4-plugin-%{name}
Summary:	Netscape 4.x Java plugin
Summary(pl.UTF-8):	Wtyczka Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown

%description -n netscape4-plugin-%{name}
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla Netscape 4.x.

%package mozilla-plugin
Summary:	Mozilla Java plugin file
Summary(pl.UTF-8):	Plik wtyczki Javy do Mozilli
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Obsoletes:	java-blackdown-mozilla-plugin

%description mozilla-plugin
Java plugin file for Mozilla.

%description mozilla-plugin -l pl.UTF-8
Plik wtyczki z obsługą Javy dla Mozilli.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla Java plugin
Summary(pl.UTF-8):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
Requires:	%{name}-mozilla-plugin = %{version}-%{release}
Requires:	mozilla-embedded
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java-sun
Obsoletes:	mozilla-plugin-gcc3-java-sun
Obsoletes:	mozilla-plugin-gcc32-java-sun
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun

%description -n mozilla-plugin-%{name}
Java plugin for Mozilla compiled using gcc 3.

%description -n mozilla-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla Mozilli skompilowana przy użyciu gcc 3.

%package -n mozilla-firefox-plugin-%{name}
Summary:	Mozilla Firefox Java plugin
Summary(pl.UTF-8):	Wtyczka Javy do Mozilli Firefox
Group:		Development/Languages/Java
Requires:	%{name}-mozilla-plugin = %{version}-%{release}
Requires:	mozilla-firefox
Obsoletes:	mozilla-firefox-plugin-gcc2-java-sun
Obsoletes:	mozilla-firefox-plugin-gcc3-java-sun
Obsoletes:	mozilla-firefox-plugin-java-blackdown

%description -n mozilla-firefox-plugin-%{name}
Java plugin for Mozilla Firefox compiled using gcc 3.

%description -n mozilla-firefox-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla Mozilli Firefox skompilowana przy użyciu
gcc 3.

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{javadir},%{_mandir}/{,ja/}man1,%{_bindir}}
sed -e "s#DESTDIR#$RPM_BUILD_ROOT%{javadir}#g" <%{SOURCE1} >%{name}.xml
chmod +x %{SOURCE0}
%{SOURCE0} -mode=silent -silent_xml=%{name}.xml

mv $RPM_BUILD_ROOT%{javadir}/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{javadir}/man/ja_JP.eucJP/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

# conflict with heimdal/krb5
for i in kinit klist ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/j$i
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/man1/j${i}.1
	mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/j${i}.1
done

for i in ControlPanel java java_vm keytool ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap javaws jconsole jdb jinfo jmap jps \
	 jsadebugd jstack jstat jstatd native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

#for i in javaplugin rt sunrsasign ; do
#	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
#done

install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{firefoxdir}/plugins,%{jredir}/plugin/i386/ns610}

ln -sf %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins
ln -sf %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{firefoxdir}/plugins

install  -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_javadir}}
mv $RPM_BUILD_ROOT%{jredir}/plugin/desktop/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{jredir}/plugin/desktop/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

# these binaries are in %{jredir}/bin - not needed in %{javadir}/bin?
rm -f $RPM_BUILD_ROOT%{javadir}/bin/{ControlPanel,keytool,kinit,klist,ktab,orbd,policytool,rmid,rmiregistry,servertool,tnameserv}

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javadir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javadir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javadir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{_javadir}/jce.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jndi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jndi-ldap.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jndi-cos.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jndi-rmi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jaas.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jdbc-stdext.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javadir}/jdbc-stdext-3.0.jar

ln -sf %{jredir}/lib/javaws.jar $RPM_BUILD_ROOT%{_javadir}/javaws.jar
mv -f $RPM_BUILD_ROOT{%{jredir}/lib,%{_datadir}}/locale

# standardize dir names
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}
#mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_HK.BIG5HK,zh_HK}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ko.UTF-8,zh.GBK,zh_TW.BIG5}

%clean
rm -rf $RPM_BUILD_ROOT

%pre jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%files
%defattr(644,root,root,755)
#%doc COPYRIGHT LICENSE README.html
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
#%attr(755,root,root) %{javadir}/bin/javaws
%attr(755,root,root) %{javadir}/bin/appletviewer
#%attr(755,root,root) %{javadir}/bin/apt
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
#%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
#%attr(755,root,root) %{javadir}/bin/jinfo
#%attr(755,root,root) %{javadir}/bin/jmap
#%attr(755,root,root) %{javadir}/bin/jps
#%attr(755,root,root) %{javadir}/bin/jsadebugd
#%attr(755,root,root) %{javadir}/bin/jstack
#%attr(755,root,root) %{javadir}/bin/jstat
#%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/serialver
%{javadir}/include
%dir %{javadir}/lib
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl
%{_mandir}/man1/appletviewer.1*
#%{_mandir}/man1/apt.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jdb.1*
#%{_mandir}/man1/jinfo.1*
#%{_mandir}/man1/jmap.1*
#%{_mandir}/man1/jps.1*
#%{_mandir}/man1/jsadebugd.1*
#%{_mandir}/man1/jstack.1*
#%{_mandir}/man1/jstat.1*
#%{_mandir}/man1/jstatd.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
#%{_mandir}/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*
#%lang(ja) %{_mandir}/ja/man1/apt.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
#%lang(ja) %{_mandir}/ja/man1/jinfo.1*
#%lang(ja) %{_mandir}/ja/man1/jmap.1*
#%lang(ja) %{_mandir}/ja/man1/jps.1*
#%lang(ja) %{_mandir}/ja/man1/jsadebugd.1*
#%lang(ja) %{_mandir}/ja/man1/jstack.1*
#%lang(ja) %{_mandir}/ja/man1/jstat.1*
#%lang(ja) %{_mandir}/ja/man1/jstatd.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
#%lang(ja) %{_mandir}/ja/man1/jconsole.1*

%files jre-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libJdbcOdbc.so

%files jre
%defattr(644,root,root,755)
#%doc jre/{CHANGES,COPYRIGHT,LICENSE,README,*.txt}
#%doc jre/Welcome.html
#%doc jre/Xusage*
%attr(755,root,root) %{_bindir}/ControlPanel
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/jkinit
%attr(755,root,root) %{_bindir}/jklist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
#%attr(755,root,root) %{jredir}/bin/javaws
#%attr(755,root,root) %{jredir}/bin/pack200
#%attr(755,root,root) %{jredir}/bin/unpack200
#%attr(755,root,root) %{javadir}/bin/pack200
#%attr(755,root,root) %{javadir}/bin/unpack200
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/ControlPanel
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/kinit
%attr(755,root,root) %{jredir}/bin/klist
%attr(755,root,root) %{jredir}/bin/ktab
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%{jredir}/lib/fonts
%dir %{jredir}/lib/i386
#%dir %{jredir}/lib/i386/xawt
#%dir %{jredir}/lib/i386/motif21
#%dir %{jredir}/lib/i386/headless
%attr(755,root,root) %{jredir}/lib/i386/client
%attr(755,root,root) %{jredir}/lib/i386/native_threads
%attr(755,root,root) %{jredir}/lib/i386/jrockit
#%attr(755,root,root) %{jredir}/lib/i386/server
%{jredir}/lib/i386/jvm.cfg
%attr(755,root,root) %{jredir}/lib/i386/awt_robot
%attr(755,root,root) %{jredir}/lib/i386/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/i386/libjsoundalsa.so
%{jredir}/lib/im
%{jredir}/lib/images
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 mtime size) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
#%%{jredir}/lib/*.cfg
#%%{jredir}/lib/tzmappings
%lang(ja) %{jredir}/lib/*.properties.ja
##%lang(zh) %{jredir}/lib/*.properties.zh
%dir %{jredir}/plugin
%dir %{jredir}/plugin/i386
%dir %{_javadir}
%{_javadir}/jaas.jar
%ifarch %{ix86}
%{_javadir}/javaws*.jar
%endif
%{_javadir}/jce.jar
%{_javadir}/jcert.jar
%{_javadir}/jdbc-stdext*.jar
%{_javadir}/jndi*.jar
%{_javadir}/jnet.jar
%{_javadir}/jsse.jar
#%{jredir}/lib/classlist
#%{jredir}/lib/fontconfig.RedHat.2.1.bfc
#%{jredir}/lib/fontconfig.RedHat.2.1.properties.src
#%{jredir}/lib/fontconfig.RedHat.3.bfc
#%{jredir}/lib/fontconfig.RedHat.3.properties.src
#%{jredir}/lib/fontconfig.RedHat.8.0.bfc
#%{jredir}/lib/fontconfig.RedHat.8.0.properties.src
#%{jredir}/lib/fontconfig.RedHat.bfc
#%{jredir}/lib/fontconfig.RedHat.properties.src
#%{jredir}/lib/fontconfig.SuSE.bfc
#%{jredir}/lib/fontconfig.SuSE.properties.src
#%{jredir}/lib/fontconfig.Sun.2003.bfc
#%{jredir}/lib/fontconfig.Sun.2003.properties.src
#%{jredir}/lib/fontconfig.Sun.bfc
#%{jredir}/lib/fontconfig.Sun.properties.src
#%{jredir}/lib/fontconfig.Turbo.8.0.bfc
#%{jredir}/lib/fontconfig.Turbo.8.0.properties.src
#%{jredir}/lib/fontconfig.Turbo.bfc
#%{jredir}/lib/fontconfig.Turbo.properties.src
#%{jredir}/lib/fontconfig.bfc
#%{jredir}/lib/fontconfig.properties.src
#%attr(755,root,root) %{jredir}/lib/i386/gtkhelper
#%attr(755,root,root) %{jredir}/lib/i386/headless/libmawt.so
#%attr(755,root,root) %{jredir}/lib/i386/libsaproc.so
#%attr(755,root,root) %{jredir}/lib/i386/libunpack.so
#%attr(755,root,root) %{jredir}/lib/i386/motif21/libmawt.so
#%attr(755,root,root) %{jredir}/lib/i386/xawt/libmawt.so
#%dir %{jredir}/lib/javaws
#%{jredir}/lib/javaws/Java1.5.ico
#%{jredir}/lib/javaws/messages.properties
#%{jredir}/lib/javaws/messages_de.properties
#%{jredir}/lib/javaws/messages_es.properties
#%{jredir}/lib/javaws/messages_fr.properties
#%{jredir}/lib/javaws/messages_it.properties
#%{jredir}/lib/javaws/messages_ja.properties
#%{jredir}/lib/javaws/messages_ko.properties
#%{jredir}/lib/javaws/messages_sv.properties
#%{jredir}/lib/javaws/messages_zh_CN.properties
#%{jredir}/lib/javaws/messages_zh_HK.properties
#%{jredir}/lib/javaws/messages_zh_TW.properties
#%{jredir}/lib/javaws/miniSplash.jpg
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/sunw_java_plugin.mo
#%lang(zh_HK) %{_datadir}/locale/zh_HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
#%dir %{jredir}/lib/management
#%{jredir}/lib/management/jmxremote.access
#%{jredir}/lib/management/jmxremote.password.template
#%{jredir}/lib/management/management.properties
#%{jredir}/lib/management/snmp.acl.template
%{_mandir}/man1/java.1*
%{_desktopdir}/sun_java.desktop
%{_pixmapsdir}/sun_java.png
%{_mandir}/man1/javaws.1*
%{_mandir}/man1/jkinit.1*
%{_mandir}/man1/jklist.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/ktab.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/policytool.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
#%{_mandir}/man1/*pack200.1*
#%lang(ja) %{_mandir}/ja/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%lang(ja) %{_mandir}/ja/man1/jkinit.1*
%lang(ja) %{_mandir}/ja/man1/jklist.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/ktab.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*
%dir %{jredir}/javaws
##%{jredir}/javaws/resources
%attr(755,root,root) %{jredir}/javaws/javaws
##%attr(755,root,root) %{jredir}/javaws/javawsbin
##%{jredir}/javaws/cacerts
##%{jredir}/javaws/*.gif
##%{jredir}/javaws/*.jar
##%{jredir}/javaws/*.policy
##%{jredir}/javaws/*.html

%files jre-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libjsoundalsa.so

#%files demos
#%defattr(644,root,root,755)
#%{javadir}/demo

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/rmic
%{_mandir}/man1/jar.1*
%{_mandir}/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*

%files jre-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/bin/rmiregistry
%{_mandir}/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*

%files mozilla-plugin
%defattr(644,root,root,755)
%dir %{jredir}/plugin/i386/ns610
%attr(755,root,root) %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{mozilladir}/plugins/libjavaplugin_oji.so

%files -n mozilla-firefox-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{firefoxdir}/plugins/libjavaplugin_oji.so
