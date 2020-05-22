# ############## Local Domain Settings ##############

my_host_name = '127.0.0.1'  # !!!本机的域名!!!! 必须修改!

my_host_scheme = 'https://'  # 本机的协议, 可选为 "http://" 和 "https://"



# ############## Target Domain Settings ##############

target_domain = 'www.pornhub.com'  # !!!!你的目标域名!!!!

target_scheme = 'https://'



# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里

# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.

# 自动采集(如果开启的话)会不断告诉你新域名

external_domains = [
    'www.pornhub.com'

]



# 这些是一些公共的静态资源域名, 会被自动添加到你上面的 external_domains 中

BOILERPLATE_EXTERNAL_DOMAINS = [
    'accounts.google.com',
    'apis.google.com',

    "ajax.aspnetcdn.com",
    "cdn.jsdelivr.net",
    "maxcdn.bootstrapcdn.com",

]



# 在这里面的站点会被强制使用HTTPS, 暂不支持通配符

force_https_domains = [

    # "example.com",

    # "example.org",

]



# 自动动态添加域名

enable_automatic_domains_whitelist = True

domains_whitelist_auto_add_glob_list = (

    # 将你的域名通配符填写到这, 比如下面这样:

    "*.pornhub.com",

    # "*.example.org",

)



# ############## Proxy Settings ##############

# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理

is_use_proxy = False

# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies

requests_proxies = dict(

    http='http://127.0.0.1:8123',

    https='https://127.0.0.1:8123',

)



# ### 其他高级配置请看 config_default.py 中的详细说明





# ------------ 以下部分为一些简单的逻辑, 请不要修改下面的代码 ----------------

external_domains += BOILERPLATE_EXTERNAL_DOMAINS  # 将公共静态资源域名加入到external_domains中

# 将公共静态资源域名设置为强制HTTPS

if force_https_domains == "NONE":

    force_https_domains = BOILERPLATE_EXTERNAL_DOMAINS

elif isinstance(force_https_domains, (list, tuple)):

    force_https_domains = list(force_https_domains) + BOILERPLATE_EXTERNAL_DOMAINS
