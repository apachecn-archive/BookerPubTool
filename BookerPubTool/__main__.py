import argparse
import sys
from . import __version__
from .pypi import *
from .npm import *
from .docker import *
from .ebook2site import *
from .libgen import *
from .zhihu_msger import *

def main():
    parser = argparse.ArgumentParser(prog="BookerPubTool", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"PYBP version: {__version__}")
    parser.set_defaults(func=lambda x: parser.print_help())
    subparsers = parser.add_subparsers()
    
    docker_pub_parser = subparsers.add_parser("pub-docker", help="publish book to dockerhub")
    docker_pub_parser.add_argument("dir", help="dir")
    docker_pub_parser.set_defaults(func=publish_docker)

    pypi_pub_parser = subparsers.add_parser("pub-pypi", help="publish book to pypi")
    pypi_pub_parser.add_argument("dir", help="dir")
    pypi_pub_parser.set_defaults(func=publish_pypi)
    
    pypi_config_parser = subparsers.add_parser("conf-pypi", help="configure pypi token")
    pypi_config_parser.add_argument("token", help="token")
    pypi_config_parser.set_defaults(func=config_pypi)
    
    npm_pub_parser = subparsers.add_parser("pub-npm", help="publish book to npm")
    npm_pub_parser.add_argument("dir", help="dir")
    npm_pub_parser.set_defaults(func=publish_npm)
    
    npm_config_parser = subparsers.add_parser("conf-npm", help="configure npm token")
    npm_config_parser.add_argument("token", help="token")
    npm_config_parser.set_defaults(func=config_npm)
    
    ebook2site_parser = subparsers.add_parser("ebook2site", help="convert an ebook to a site")
    ebook2site_parser.add_argument("name", help="name")
    ebook2site_parser.add_argument("file", help="file")
    ebook2site_parser.add_argument("-d", "--dir", help="dir", default='.')
    ebook2site_parser.set_defaults(func=ebook2site)
    
    libgen_parser = subparsers.add_parser("libgen", help="upload to libgen")
    libgen_parser.add_argument("series", help="series")
    libgen_parser.add_argument("fname", help="file name")
    libgen_parser.add_argument("-t", "--threads", type=int, default=3, help="thread count")
    libgen_parser.add_argument("-p", "--proxy", help="proxy")
    libgen_parser.set_defaults(func=upload_libgen)
    
    zhihu_msg_parser = subparsers.add_parser("zhihu-msg", help="send zhihu messages")
    zhihu_msg_parser.add_argument("uid_fname", help="file name including uids")
    zhihu_msg_parser.add_argument(
        "-m", "--content", 
        default='布客社区\n\n您永远在线的两性情感和技术变现专家\n\n🔗https://docs.apachecn.org', 
        help="message content",
    )
    zhihu_msg_parser.add_argument("-c", "--cookies", default=os.environ.get('ZHIHU_COOKIES', ''), help="zhihu cookies splited with ';;'")
    zhihu_msg_parser.add_argument("-o", "--old", action='store_true', help="whether to use old API")
    zhihu_msg_parser.add_argument("-s", "--wait-succ", type=float, default=60, help="how long to wait after success")
    zhihu_msg_parser.add_argument("-f", "--wait-fail", type=float, default=0, help="how long to wait after failure except HTTP403")
    zhihu_msg_parser.add_argument("-b", "--wait-403", type=float, default=0, help="how long to wait after HTTP403")
    zhihu_msg_parser.set_defaults(func=send_msg_handle)
    
    args = parser.parse_args()
    args.func(args)
    
if __name__ == '__main__': main()