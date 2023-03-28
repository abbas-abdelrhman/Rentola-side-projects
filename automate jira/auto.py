# -*- coding: utf-8 -*-
# Author: Adham Mansour

import json
from collections import Counter
import requests
import scrapy
from colorama import Fore, Back, Style
from scrapy import Selector

from ..helper import *


class CFindboligerDkSpider(scrapy.Spider):
    name = 'c_findboliger_dk_assigning_botv2'
    # authorization
    # the dashboard acronym
    projectKey = "SPIDERPROD"
    country = ''
    start_urls = [
        # \/top 500 unassigned domains from all countries\/
        f'https://c.findboliger.dk/spider_details?utf8=%E2%9C%93&per_page=500&spider_detail%5Bcountry%5D={country}&spider_detail%5Bstatus%5D=&spider_detail%5Bcategory%5D=&spider_detail%5Bassigned%5D=Not+Assigned&spider_detail%5Boperator%5D=&spider_detail%5Blisting_count%5D=&spider_detail%5Bteam_id%5D=&spider_detail%5Bdeveloped_by_id%5D=&spider_detail%5Bapproval_status%5D=&spider_detail%5Bflag_status%5D=&spider_detail%5Bwith_errors%5D=0&spider_detail%5Bname%5D=&spider_detail%5Bdomain%5D=&commit=Search',
        # f'https://c.findboliger.dk/spider_details?utf8=%E2%9C%93&per_page=500&spider_detail%5Bcountry%5D=portugal&spider_detail%5Bstatus%5D=&spider_detail%5Bcategory%5D=&spider_detail%5Bassigned%5D=Not+Assigned&spider_detail%5Boperator%5D=&spider_detail%5Blisting_count%5D=&spider_detail%5Bteam_id%5D=&spider_detail%5Bdeveloped_by_id%5D=&spider_detail%5Bapproval_status%5D=&spider_detail%5Bflag_status%5D=&spider_detail%5Bwith_errors%5D=0&spider_detail%5Bname%5D=&spider_detail%5Bdomain%5D=&commit=Search'
    ]
    jira_developer_id = {}
    headers = {
        "Accept": "application/json"
    }
    custom_settings = {
        'dont_filter': False,
        "DUPEFILTER_CLASS": 'scrapy.dupefilters.BaseDupeFilter'

    }

    def get_jira_developer_id(self):
        url = "https://rentola-dev.atlassian.net/rest/api/3/user/assignable/multiProjectSearch?projectKeys=SPIDERPROD"

        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            auth=self.auth
        )
        json_data = json.loads(response.text)
        response.close()
        # gathering the ids and the names of the developers on jira
        for i in json_data:
            self.jira_developer_id[i['accountId']] = i['displayName']
        # removing and popping out individuals who does not need spiders
        self.jira_developer_id.pop('615ad0e6c5388b0069674cbb', None)  # Abanoub Moris:::615ad0e6c5388b0069674cbb
        self.jira_developer_id.pop('624d93817a3f9e006ab65e12', None)  # Abdelrahman Amr:::624d93817a3f9e006ab65e12
        self.jira_developer_id.pop('612f4a146b6661006909bea5', None)  # Ahmed Atef:::612f4a146b6661006909bea5
        self.jira_developer_id.pop('6282006262e0790069a4d0f5', None)  # Alex Polishchuk:::6282006262e0790069a4d0f5
        self.jira_developer_id.pop('61ae02d26d002b006b24f751', None)  # Allana Sørensen:::61ae02d26d002b006b24f751
        self.jira_developer_id.pop('60e2a8e0471e61006a29eeda', None)  # Amit Patel:::60e2a8e0471e61006a29eeda
        self.jira_developer_id.pop('60df2da07fcd820073faed30', None)  # Anna K:::60df2da07fcd820073faed30
        self.jira_developer_id.pop('6295d46ce76a9c00705d9a51', None)  # anna.hirnyk:::6295d46ce76a9c00705d9a51
        self.jira_developer_id.pop('70121:c285f1c1-8806-4d80-9ee4-6ab810701c97',
                                   None)  # benjamin:::70121:c285f1c1-8806-4d80-9ee4-6ab810701c97
        self.jira_developer_id.pop('61dc2efdce3652006a0b7f45', None)  # Brindis Joensen:::61dc2efdce3652006a0b7f45
        self.jira_developer_id.pop('5e86008a9b6a000c1a4333b8', None)  # Elin Edwertz:::5e86008a9b6a000c1a4333b8
        self.jira_developer_id.pop('61570c3999b4b8006a74f88b', None)  # elizabeth:::61570c3999b4b8006a74f88b
        self.jira_developer_id.pop('61602d48d9820f0070dda887', None)  # Emily Madsen:::61602d48d9820f0070dda887
        self.jira_developer_id.pop('70121:c64bd6e7-cd72-4cf6-95df-ce593f106646',
                                   None)  # Erik Nilsson:::70121:c64bd6e7-cd72-4cf6-95df-ce593f106646
        self.jira_developer_id.pop('61f807ced8d7cf006a8ecc18', None)  # Fatma Yılmaz:::61f807ced8d7cf006a8ecc18
        self.jira_developer_id.pop('61dc2efd0586a200699e9143', None)  # frida:::61dc2efd0586a200699e9143
        self.jira_developer_id.pop('61f807cec6bd1a00691c4b22', None)  # Hasan:::61f807cec6bd1a00691c4b22
        self.jira_developer_id.pop('61dc2efde67ea2006b1cac59', None)  # Hesham:::61dc2efde67ea2006b1cac59
        self.jira_developer_id.pop('610a5f2deb7aef0069f6f74d', None)  # Hesham Youssef:::610a5f2deb7aef0069f6f74d
        self.jira_developer_id.pop('605af43a570829006ae7e61f', None)  # Jacob Dinesen:::605af43a570829006ae7e61f
        self.jira_developer_id.pop('5b113cede249415c02f6823a', None)  # Jacob Lund:::5b113cede249415c02f6823a
        self.jira_developer_id.pop('70121:2d738f1c-a1b2-44ee-91eb-93e4fa310a60',
                                   None)  # jan:::70121:2d738f1c-a1b2-44ee-91eb-93e4fa310a60
        self.jira_developer_id.pop('70121:596401d2-bbf8-4529-aefd-6068e80e544d',
                                   None)  # Janrevald:::70121:596401d2-bbf8-4529-aefd-6068e80e544d
        self.jira_developer_id.pop('615571cbc669a6006923a63a', None)  # Jordan Trajkov:::615571cbc669a6006923a63a
        self.jira_developer_id.pop('61f807ce49fc430069506f32', None)  # Kubra:::61f807ce49fc430069506f32
        self.jira_developer_id.pop('557058:f183dbea-7d6c-4a79-80f2-a67b4adc4cd2',
                                   None)  # Łukasz Jachymczyk:::557058:f183dbea-7d6c-4a79-80f2-a67b4adc4cd2
        self.jira_developer_id.pop('612f4a39b7859000710ee6e4', None)  # Mahmoud Wessam:::612f4a39b7859000710ee6e4
        self.jira_developer_id.pop('61d1a579e67ea2006baf072f', None)  # Malou Guldbæk:::61d1a579e67ea2006baf072f
        self.jira_developer_id.pop('5e15e2d6cbf1830daa9d3421', None)  # marcinTichoniuk:::5e15e2d6cbf1830daa9d3421
        self.jira_developer_id.pop('5af173591864357363fa75b4', None)  # Mateusz Siedlecki:::5af173591864357363fa75b4
        self.jira_developer_id.pop('61b98a68ef5b460071131679', None)  # Mehmet Kurtipek:::61b98a68ef5b460071131679
        self.jira_developer_id.pop('557058:9862ab0d-05bf-4501-b3ec-8595815faabd',
                                   None)  # Mehmet Kurtipek:::557058:9862ab0d-05bf-4501-b3ec-8595815faabd
        self.jira_developer_id.pop('70121:520a7a75-bef5-4c3f-a5ef-fcd05aa7ee95',
                                   None)  # miklas:::70121:520a7a75-bef5-4c3f-a5ef-fcd05aa7ee95
        self.jira_developer_id.pop('60dde6b67d016900703db36a', None)  # MO:::60dde6b67d016900703db36a
        self.jira_developer_id.pop('61630b7e07ac3c00685c2165', None)  # Mohamed Hossam:::61630b7e07ac3c00685c2165
        self.jira_developer_id.pop('6139fb8714e8340071ffa3df', None)  # Mohamed Zakaria:::6139fb8714e8340071ffa3df
        self.jira_developer_id.pop('6267f398185ac2006930dcbd', None)  # Mohammad Ashraf:::6267f398185ac2006930dcbd
        self.jira_developer_id.pop('61aa19d4c75da800721a7130', None)  # Muhammad Alaa:::61aa19d4c75da800721a7130
        self.jira_developer_id.pop('626fa4fd2db3080070238495', None)  # Nanna Stage:::626fa4fd2db3080070238495
        self.jira_developer_id.pop('5bbe1442da617e7586b864cf', None)  # Nilas:::5bbe1442da617e7586b864cf
        self.jira_developer_id.pop('61f807ce8d9e3c00688e0bb1', None)  # Nilay Cezik:::61f807ce8d9e3c00688e0bb1
        self.jira_developer_id.pop('612f4a78b7859000710eea2c', None)  # Noorulhoda Khaled:::612f4a78b7859000710eea2c
        self.jira_developer_id.pop('6188fb7ae601490068818604', None)  # Omar Salama:::6188fb7ae601490068818604
        self.jira_developer_id.pop('61dc2efdf3037f0069531932', None)  # Pierre:::61dc2efdf3037f0069531932
        self.jira_developer_id.pop('6218d907ba649b006aae4019', None)  # Roció Hernández:::6218d907ba649b006aae4019
        self.jira_developer_id.pop('6203c90deaf9e200707496c0', None)  # ronalyn:::6203c90deaf9e200707496c0
        self.jira_developer_id.pop('6151d53f7a6be40071892031', None)  # Rune Baarts-Jensen:::6151d53f7a6be40071892031
        self.jira_developer_id.pop('61f807ce8d9e3c00688e0bb2', None)  # Semih Sener:::61f807ce8d9e3c00688e0bb2
        self.jira_developer_id.pop('625969319770e600716aee66', None)  # Tarek EL-Sayyad:::625969319770e600716aee66
        self.jira_developer_id.pop('60d6e95cdae567006827135f', None)  # Tarek Samni:::60d6e95cdae567006827135f
        self.jira_developer_id.pop('61ee8155aeaacb0072e62060',
                                   None)  # Tennyson Takudzwa Zvaita:::61ee8155aeaacb0072e62060
        self.jira_developer_id.pop('61bb35483afc8a0070a3bffc', None)  # test alkpote:::61bb35483afc8a0070a3bffc
        self.jira_developer_id.pop('6151925c289a54006aa471e8', None)  # Vijay Sookha:::6151925c289a54006aa471e8
        self.jira_developer_id.pop('61dc2efd125b120071309066', None)  # viktoriia:::61dc2efd125b120071309066
        self.jira_developer_id.pop('627cc6fe9bb660006995d6ba', None)  # Yusuf:::627cc6fe9bb660006995d6ba
        self.jira_developer_id.pop('62b590bfa58208122da287fb', None)  # NIKITA:::
        self.jira_developer_id.pop('62b32e68b065974c3e248f29', None)  # denys:::
        self.jira_developer_id.pop('62b32db4b065974c3e248e9e', None)  # denys:::
        self.jira_developer_id.pop(' 60f53a9dd0134900692d368c', None)  # denys:::

    def get_dev_issues_count(self, dict):
        # gets how many fixes and assigned domains does each dev have
        for key, value in dict.items():
            assigned_fixes = {}
            url = "https://rentola-dev.atlassian.net/rest/api/3/search"
            # gets the number of assigned domains to the dev
            query = {
                'jql': f"project = {self.projectKey} AND assignee in ({key}) AND status in ('Assigned -','currently being developped -') AND hierarchyLevel = 0"
            }
            response = requests.request(
                "GET",
                url,
                headers=self.headers,
                params=query,
                auth=self.auth
            )
            json_data = json.loads(response.text)
            response.close()
            assigned_fixes['assigned'] = (len(json_data['issues']))

            # gets the number of fixes needed from the dev
            query = {
                'jql': f"project = {self.projectKey} AND assignee in ({key}) AND status in ('To be fixed -') AND hierarchyLevel = 0"
            }
            response = requests.request(
                "GET",
                url,
                headers=self.headers,
                params=query,
                auth=self.auth
            )
            json_data = json.loads(response.text)
            response.close()
            assigned_fixes['fixes'] = (len(json_data['issues']))
            assigned_fixes['name'] = value
            self.jira_developer_id[key] = assigned_fixes

    def github_names_adder(self, jira_id, github_name):
        value = self.jira_developer_id[jira_id]
        value['github_name'] = github_name
        self.jira_developer_id[jira_id] = value

    def get_dev_checks(self):
        # 2) \/ go to the pr checks page
        # https://github.com/revamediadk/pyspiders/pulls?q=is%3Apr+is%3Aopen+label%3Adev_check
        # copy your header details and  replace it with the variable down there [header] most probably just the cookie for your own verification
        header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': "_octo=GH1.1.2136890076.1638041219; _device_id=e83b4c31a77623e3c592273e4932d6dd; user_session=I4K-I_km1J1x1po31GHt3mG1XlqxdxpLy6_xwnksOlbrvgoh; __Host-user_session_same_site=I4K-I_km1J1x1po31GHt3mG1XlqxdxpLy6_xwnksOlbrvgoh; logged_in=yes; dotcom_user=meladakram; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=dark; tz=Africa%2FCairo; _gh_sess=2icvQxkmaH1UGPhhM9Mr9sbf449Jg8TH5ay0yVH3MDu1XG8Puy0P8LemfYBCT1UTMCMQuUHmdACadDtKMcMPHFvU9%2Bnop2otTouc%2FgA91P4mID6JGFLVmA5KvVVnTI8nF%2FmahBvPL8e%2BuPO35M6w4%2Fe4DGytlfCw%2FLFkF87XmQEl454clxcla1qwntjV63zNXCyArvjAtOJmdf8g81swhJwQFAs%2BrJ1WwgUcs5wKWK4y3Bfyr2GtVPIwbMI6LJqGslaNm5fwSTdFsv8Ic8O0ewWy8SLGz7WQa6jnfX0AvtifIoLPJ2kEnfaGX2VCcp7kl3TswTjCJ8ZiN5p42AwukTxJ63llYf0xwiWfzrAbb%2FXcZXh83TaIBb%2BMPvfPvtD48l0OBLgu5egSfUXVCANrsO34AU527B%2B6%2BIDIkiPdzvJYFrXhwQ4I6lQVCQCEfJMPGCBlaU9emEdLbK5KmvH6RoXviQA1D%2BJ8JJu27Yq4rj5p2PRpGEpqZ1hXJg4LXioNVIh9rIo0BFbZCILJfrzivVtm3PHD%2BTwXt19rZqetdBhk6XX1BmdJiKqR7gIrW4bjxuPrRJcGE%2FiMPa%2FQ5aV4mf083jAa3l1gEmd3Wfh7cPPFekI%2Fs8K710ZgS9WiTmV%2FJO1gfNu91TQUbltuUWfLb6vCtib8E6uEIILwUgUwfjHMUgAHqkF4mrIQUz97l6uMu98xhPYw3itffYdqqK%2BYsfgR%2Bv1J4CgBn%2BYiX4C2JvYXApmawr8wyTKB%2B9Ato9Hp10Z7VqfO8cs%2FK7ELTmh3cIMs%2FGHkd7iz0XN5TFCd0jxPUUIXHdqr8VD8HGEbS%2F%2BtxNw1FmbRKJfCvogSqqCEHBqkovF%2FZqFvaDtvWjYkbrAJua%2BHs%2FDvDAQvVBs5TFIIMdCL7Xt1aJnZ%2FMCzyJnvh6yoM1ymHnzZAzDHaOlys1oDa5tyq37JUjhmRUhBfRNphJCZC6KWjs9DMCCP2NhyXla7BBJcYQRpXnpH8QDw6g%2BASDSB1Ok1pE1nVhVBBS2zm8mg%2FsZwpGDgXkZcpKaFqYUqsxs0vl7RZaU9HRXhTPI8EIp1Ba3lLA%3D%3D--IY1H6mLPfEuLPtEF--HoZW8zJUTVlR9IzzNPtFzg%3D%3D",
            "if-none-match": 'W/"750ac274f254bc2f0157b375b4a4d01e"',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        }
        response = requests.request(
            "GET",
            'https://github.com/revamediadk/pyspiders/pulls?q=is%3Aopen+is%3Apr+label%3Adev_check',
            headers=header,
        )
        html_data = Selector(text=response.text, type="html")  ##important bit
        dev_checks = Counter(html_data.css('.pr-md-2 .Link--muted::text').extract())
        self.github_names_adder(jira_id='61af317f657a05007044561b', github_name='seafgomaa')
        self.github_names_adder(jira_id='61893c0f22ce4900709a280e', github_name='OmarIbrahim991')
        self.github_names_adder(jira_id='61e56a235fcc370068593255', github_name='Nuranii')
        self.github_names_adder(jira_id='61e56a2308c1f7006a0bc58f', github_name='mohamedhelmyy28')
        self.github_names_adder(jira_id='623859b3bef8a60068c5c8cc', github_name='Skiperz69')
        self.github_names_adder(jira_id='61fba4b9f5f5b80070c81a23', github_name='Doomzy')
        self.github_names_adder(jira_id='61e56a237ae0dc006a8ae661', github_name='meladakram')
        self.github_names_adder(jira_id='61fba4b9c6bd1a00691def0a', github_name='KhaledElOlemy')
        self.github_names_adder(jira_id='61e6839554627a00705cc579', github_name='FawziElNaggar')
        self.github_names_adder(jira_id='61a4b6e8977c5b0072fb9322', github_name='AsmaaElshahat')
        self.github_names_adder(jira_id='61fbd7b6c224b80069c91e61', github_name='AmeerAkram220')
        self.github_names_adder(jira_id='61fba4b91c9bb000727d15b9', github_name='alyabozied')
        self.github_names_adder(jira_id='61e56a23fd5a690068b04e21', github_name='ahmed2299')
        self.github_names_adder(jira_id='6183b0aef6da6a006a8e1038', github_name='AhmedSh4hien')
        self.github_names_adder(jira_id='617ff9f5860f78006b8d548b', github_name='omran96')
        self.github_names_adder(jira_id='615adeb372f69700694732cb', github_name='AhmedAshrafHegab ')
        self.github_names_adder(jira_id='623859b3b75ca80070550299', github_name='ahmedasem1')
        self.github_names_adder(jira_id='623859b31c7f6a007048178d', github_name='AhmedElWardany')
        self.github_names_adder(jira_id='61838861f485cd0068384a8b', github_name='adhamnaeim')
        self.github_names_adder(jira_id='61fba4b9845d670071f3b934', github_name='Abdelrahman-bedier')
        self.github_names_adder(jira_id='618bb7fe86c210006a94aa22', github_name='abbas-abdelrhman')
        for key, value in self.jira_developer_id.items():
            if 'github_name' in value.keys():
                github_name = value['github_name']
                if github_name in dev_checks.keys():
                    value = self.jira_developer_id[key]
                    value['dev_checks'] = str(dev_checks[github_name])
                    self.jira_developer_id[key] = value
                else:
                    value = self.jira_developer_id[key]
                    value['dev_checks'] = '0'
                    self.jira_developer_id[key] = value
            else:
                value = self.jira_developer_id[key]
                value['dev_checks'] = '0'
                self.jira_developer_id[key] = value
        return Counter(html_data.css('.pr-md-2 .Link--muted::text').extract())

    # 1. SCRAPING level 1
    def start_requests(self):
        self.get_jira_developer_id()
        self.get_dev_issues_count(self.jira_developer_id)
        self.get_dev_checks()

        # 3) go to spidernest and replace the cookie using your own verification
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': '_spider_nest_session=oBjJhLVHM%2Bgqq3kXG9PfD3OU%2FNnasklwaalaphqP%2BbRfeG5qaJUeA9b%2BKy5II4MhjWR4IMMhaLIv%2FyQyvjd5sjO5m3gETSqtAC63qcqgri5bzqasO8ZHs35ubspwOsB3hG%2BELs1juFcQgKDvfx8zR62STPcm9YlsnEbpVUUVusVgveIC8QM%2BfGC3Iz438rpvvTmiMK8cTQS13LDcOi4QKm%2FuXUvkCVhkOx6Gbq0KxwUvAdMVq37kFjBdVrZQqDVr--VQr99OaN6DGzPzoD--L6v99tn3ly9Dv%2F08Zbhilw%3D%3D; path=/; HttpOnly',
            'referer': 'https://c.findboliger.dk/users/sign_in',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response, **kwargs):
        developers_id = response.css('#spider_detail_developed_by_id option::attr(value)').extract()[1:]
        developer_name = response.css('#spider_detail_developed_by_id option::text').extract()
        devs_dict = dict(zip(developers_id, developer_name))
        devs_dict.pop('64', None)  # other helmy
        devs_dict.pop('56', None)  # other helmy
        devs_dict.pop('58', None)  # moharram
        devs_dict.pop('37', None)  # adeel
        devs_dict.pop('103', None)  # adeel saeed
        devs_dict.pop('102', None)  # afzal manzoor
        devs_dict.pop('53', None)  # ahmed atef
        devs_dict.pop('80', None)  # aishwarya
        devs_dict.pop('111', None)  # al fahad
        devs_dict.pop('34', None)  # alexandra
        devs_dict.pop('8', None)  # amit
        devs_dict.pop('71', None)  # Anna k
        devs_dict.pop('9', None)  # Arsalan
        devs_dict.pop('10', None)  # asmita
        devs_dict.pop('108', None)  # awais saleem
        devs_dict.pop('26', None)  # Bechir
        devs_dict.pop('59', None)  # benjamin
        devs_dict.pop('11', None)  # bhavesh
        devs_dict.pop('24', None)  # daniel
        devs_dict.pop('35', None)  # daphne
        devs_dict.pop('44', None)  # drashtant
        devs_dict.pop('7', None)  # erik
        devs_dict.pop('12', None)  # Fahad
        devs_dict.pop('107', None)  # Farhan ashraf
        devs_dict.pop('90', None)  # fatma mehmet
        devs_dict.pop('33', None)  # hamza
        devs_dict.pop('46', None)  # hardik
        devs_dict.pop('91', None)  # hasan mehmet
        devs_dict.pop('49', None)  # hasit
        devs_dict.pop('13', None)  # Hatri
        devs_dict.pop('41', None)  # Hien
        devs_dict.pop('109', None)  # isham ali
        devs_dict.pop('43', None)  # ishwar
        devs_dict.pop('2', None)  # Jacob
        devs_dict.pop('19', None)  # kalpesh
        devs_dict.pop('32', None)  # kavita
        devs_dict.pop('45', None)  # kevin
        devs_dict.pop('27', None)  # kristine
        devs_dict.pop('94', None)  # kubra mehmet
        devs_dict.pop('81', None)  # logix bi
        devs_dict.pop('1', None)  # martin
        devs_dict.pop('20', None)  # mehmet
        devs_dict.pop('6', None)  # miklas
        devs_dict.pop('21', None)  # miteSh
        devs_dict.pop('113', None)  # moh ashraf
        devs_dict.pop('73', None)  # moh alaa
        devs_dict.pop('14', None)  # murilo
        devs_dict.pop('18', None)  # Naiya
        devs_dict.pop('15', None)  # Naman
        devs_dict.pop('3', None)  # Nilas
        devs_dict.pop('92', None)  # nilay mehmet
        devs_dict.pop('51', None)  # Noor
        devs_dict.pop('104', None)  # Nouman comsian
        devs_dict.pop('52', None)  # Nouran
        devs_dict.pop('68', None)  # Omar Hammad
        devs_dict.pop('25', None)  # Pankaj
        devs_dict.pop('50', None)  # parimal
        devs_dict.pop('78', None)  # Prasanth
        devs_dict.pop('105', None)  # S. Faiz
        devs_dict.pop('83', None)  # Saba Javaid
        devs_dict.pop('79', None)  # Sai mohanraj
        devs_dict.pop('16', None)  # sangh
        devs_dict.pop('93', None)  # Semih
        devs_dict.pop('23', None)  # Sounak
        devs_dict.pop('77', None)  # sriram
        devs_dict.pop('42', None)  # syed
        devs_dict.pop('40', None)  # tahir
        devs_dict.pop('60', None)  # Team 1 lead
        devs_dict.pop('61', None)  # Team 2 lead
        devs_dict.pop('17', None)  # tejasvini
        devs_dict.pop('76', None)  # Uma Rani
        devs_dict.pop('5', None)  # Umair
        devs_dict.pop('82', None)  # Umair Gill
        devs_dict.pop('106', None)  # usman hamid
        devs_dict.pop('22', None)  # Valeriy
        devs_dict.pop('48', None)  # Vijay
        devs_dict.pop('36', None)  # Yazgi
        devs_dict.pop('114', None)  # sangary
        devs_dict.pop('88', None)  # youssef essam
        devs_dict.pop('38', None)  # zaman
        devs_dict.pop('110', None)  # zeeshan gill
        devs_dict.pop('75', None)  # logalingam
        devs_dict.pop('39', None)  # oshomoji@rentola.com
        devs_dict['117'] = 'Mohamed Abo El Naga'
        devs_dict['89'] = 'Fawzi Abdelnaby Elnaggar'
        devs_dict['101'] = 'ameer'
        devs_dict['87'] = 'ahmedhossam'
        devs_dict['116'] = 'Ahmed Amr El-Wardany'
        devs_dict['47'] = 'Floris Chretiennot'
        # puts the spidernest key in the jira dictionary
        for key, value in self.jira_developer_id.items():
            jira_name = value['name']
            for Skey, Svalue in devs_dict.items():
                spidernest_name = Svalue
                if jira_name.lower() == spidernest_name.lower():
                    value['spidernest_key'] = Skey
                    self.jira_developer_id[key] = value
                continue
        # having the developers with the low domains at the bottom for ease of assinging
        self.jira_developer_id = dict(
            sorted(self.jira_developer_id.items(), key=lambda item: item[1]['assigned'], reverse=True))
        for key, value in self.jira_developer_id.items():
            # developers colored green can get assigned spiders
            print(Back.GREEN + Fore.BLACK) if int(value['assigned']) < 6 and int(value['dev_checks']) < 2 else False
            # developers colored red needs to finish their fixes
            # developers not colored does not need domains
            print(Fore.RED) if int(value['fixes']) > 3 else False
            print(value['name'] + ' >> ' + str(key) + '\nassigned: ' + str(value['assigned']) + ', fixes: ' + str(
                value['fixes']) + ', dev checks: ' + str(value['dev_checks']) + Style.RESET_ALL)
            print('-------------------------')

        # getting the domains
        domain_rows = response.css('.table tr')[1:]
        domains = {}
        for domain in domain_rows:
            domain_id = domain.css('td:nth-child(1)').extract_first()
            domain_id = extract_number_only(re.findall('spider_detail_\d+', str(domain_id))[0])
            domains[domain_id] = []

            website = domain.css('td:nth-child(2) a::text').extract_first()
            domains[domain_id].append(website)

            status = domain.css('td:nth-child(4)::text').extract_first()
            domains[domain_id].append(status)

            est_listing = domain.css('td:nth-child(5)::text').extract_first()
            domains[domain_id].append(est_listing)

            country = domain.css('td:nth-child(6)::text').extract_first().lower()
            domains[domain_id].append(country)

        countries_count = {}
        countries_label = {
            'australia': 'AU🇦🇺',
            'austria': "AT🇦🇹",
            'belgium': "BE🇧🇪",
            'canada': "CA🇨🇦",
            'chile': "CL🇨🇱",
            'croatia': "HR🇭🇷",
            'czech_republic': "CZ🇨🇿",
            'denmark': "DK🇩🇰",
            'egypt': "EG🇪🇬",
            'finland': "FI🇫🇮",
            'france': "FR🇫🇷",
            'germany': "DE🇩🇪",
            'greece': "GR🇬🇷",
            'hong_kong': "HK🇭🇰",
            "hungary": "HU🇭🇺",
            "iceland": "IS🇮🇸",
            "india": "IN🇮🇳",
            "ireland": "IE🇮🇪",
            "italy": "IT🇮🇹",
            "jamaica": "JM🇯🇲",
            "japan": "JP🇯🇵",
            "lithuania": "LT🇱🇹",
            "malaysia": "my🇲🇾",
            "mexico": "mx🇲🇽",
            "netherlands": "NL🇳🇱",
            "new_zealand": "NZ🇳🇿",
            "norway": "NO🇳🇴",
            "philippines": "PH🇵🇭",
            "poland": "PL🇵🇱",
            "portugal": "PT🇵🇹",
            "qatar": "QA🇶🇦",
            "saudi_arabia": "SA🇸🇦",
            "singapore": "SG🇸🇬",
            "south_africa": "ZA🇿🇦",
            "south_korea": "KR🇰🇷",
            "spain": "ES🇪🇸",
            "sri_lanka": "LK🇱🇰",
            "sweden": "SE🇸🇪",
            "switzerland": "CH🇨🇭",
            "thailand": "TH🇹🇭",
            "turkey": "TR🇹🇷",
            "united_arab_emirates": "AE🇦🇪",
            "united_states": "US🇺🇸",
            "united_kingdom": "UK🇬🇧",
            "venezuela": "VS🇻🇪"
        }

        for key, value in domains.items():
            value_country = value[-1]
            if value_country in countries_count.keys():
                countries_count[value_country] += 1
            else:
                countries_count[value_country] = 0
        countries_count = dict(sorted(countries_count.items(), key=lambda item: item[1], reverse=True))
        print('country with the highest domains >>', list(countries_count.items())[0])
        print('country with the lowest domains >>', list(countries_count.items())[-1])
        print(countries_count)
        desired_dev_id = str(input('insert the id of the developer you would like to assign to '))
        if desired_dev_id in list(self.jira_developer_id.keys()):
            individual_dev_info = self.jira_developer_id[desired_dev_id]
            print(f'{desired_dev_id} exists')
        else:
            print(f'{desired_dev_id} is INCORRECT ABORTING!!!')
            return
        desired_country = str(input('insert the designated country '))
        if desired_country in countries_count.keys():
            print(f'{desired_country}exists')
        else:
            print(f'{desired_country} is INCORRECT ABORTING!!!')
            return
        desired_amount = str(input('insert how many spiders you would like to assign '))
        if desired_amount.isnumeric():
            print(f'{desired_amount}is valid')
        else:
            print(f'{desired_amount} is INCORRECT ABORTING!!!')
            return
        assigned_domains = []
        assigned_domains_id = []
        for key, value in domains.items():
            value_country = value[-1]
            if len(assigned_domains) < int(desired_amount):
                if value_country == desired_country:
                    assigned_domains.append(value[0])
                    assigned_domains_id.append(key)
        string = ''
        for i in assigned_domains_id:
            if i == assigned_domains_id[-1]:
                string = string + i
            else:
                string = string + i + '%2C'
        print(assigned_domains)
        # 4) go to the start url. open the dev tools and open the network
        # assign to yourself a random spider and collect your own formdata. you must change the authenticity_token
        # \/\/
        formdata = f'utf8=%E2%9C%93&authenticity_token=L0RlHOWPy6G9mfvW56ShGoIWEDxlWxgsA8DZKZvftddQabCXxzZFQ06c7Fi1U4nwcXgfimy3ReQQSdvVhAtSMQ%3D%3D&source=individuals-tab&selected_ids={string}&team_id=2&developed_by_id={individual_dev_info["spidernest_key"]}'

        # 5) change the cookie verfication to your own here too
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczRObDBzSWlReVlTUXhNU1JzTGtJMlVtWnZZVTFoU0ZVMlNEaGFTMGRvZGxCUElpd2lNVFkxTmpReU5UZzVPQzQ0TkRBMU16WTJJbDA9IiwiZXhwIjoiMjAyMi0wNy0xMlQxNDoxODoxOC44NDBaIiwicHVyIjpudWxsfX0%3D--685def317409c2b61b8d4f507790032e624dbcb6; _spider_nest_session=oBjJhLVHM%2Bgqq3kXG9PfD3OU%2FNnasklwaalaphqP%2BbRfeG5qaJUeA9b%2BKy5II4MhjWR4IMMhaLIv%2FyQyvjd5sjO5m3gETSqtAC63qcqgri5bzqasO8ZHs35ubspwOsB3hG%2BELs1juFcQgKDvfx8zR62STPcm9YlsnEbpVUUVusVgveIC8QM%2BfGC3Iz438rpvvTmiMK8cTQS13LDcOi4QKm%2FuXUvkCVhkOx6Gbq0KxwUvAdMVq37kFjBdVrZQqDVr--VQr99OaN6DGzPzoD--L6v99tn3ly9Dv%2F08Zbhilw%3D%3D',
            'dnt': '1',
            'origin': 'https://c.findboliger.dk',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

        execute = input(
            f'<<{desired_amount} domains wil be assigned from {desired_country} to {self.jira_developer_id[desired_dev_id]["name"]}, \nexecute?>>')
        if execute == 'y':
            print('execution initiated')
            yield scrapy.FormRequest('https://c.findboliger.dk/spider_details/assign_spiders',
                                     callback=self.populate_item, headers=headers, body=formdata, method='POST',
                                     meta={'domains': assigned_domains,
                                           "country_label": countries_label[desired_country],
                                           'jira_key': desired_dev_id})
        else:
            print('execution aborted')
            return

    # 3. SCRAPING level 3

    def populate_item(self, response):
        print(response.css('.alert-info'))
        url = "https://rentola-dev.atlassian.net/rest/api/3/issue/bulk"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        assignee = response.meta['jira_key']
        issueupdates = []

        print('\n+++++++++++++++++++++++++++++++++++')
        for i in response.meta['domains']:
            issue = {
                "update": {
                },
                "fields": {
                    "summary": i,
                    "issuetype": {
                        "name": "Domain -> Spider"
                    },
                    "project": {
                        "id": '10004'
                    },
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "text": "",
                                        "type": "text"
                                    }
                                ]
                            }
                        ]
                    },
                    "labels": [
                        response.meta['country_label'],
                    ],
                    "assignee": {
                        "id": assignee
                    }
                }
            }
            issueupdates.append(issue)

        payload = json.dumps({
            "issueUpdates": issueupdates
        })
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=self.auth
        )
        response.close()
        json_data = json.loads(response.text)
        for i in json_data['issues']:
            print(i)
        print('++++++++++++++++++++++++++++++++++++\n')
        print('execution succeeded')
        execute = input(f'want to assign again??')
        if execute is 'y':
            # 7) change your cookie verification here
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '_spider_nest_session=INNqE7aRL9vi6gObDO8BCLv+WUR9OWxvMzebgh3VLRp6E03Bs6Z8Etl6RR1a3Kw3/e+Cjt49FmN2jnEZz4QJDsuVtGmjnAVJfuC59eqbZSiMiJMoFPh4+Udkid78nbiNo+HaZGvvATFnHMAEvxUla+o+BMOZxbMR0vvklxObCKIi0Q2pFIvaeBIDmvGA06RiYhV9l8tQV+vh/ieS5rxLqVFEowWsWTVPGQy/hTnJSZNuKxB1p2/S5VGtYBy/iJC8175S4dRfoMw1miT0JteOWnMC5JXIhzfgjs7sUxCLRFcVpJFGL93IgObihwErlf4zcHsX4W/HuGi7skkW4ktGKRUrX8XEOjJBPpO4psYgFQ+Gt4FBHwXCf+pfLLK7--9F+N/wTUpSgh2rlb--GvfTT/mSzHHlHnXErvrLPQ==; path=/; HttpOnly',
                'referer': 'https://c.findboliger.dk/users/sign_in',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            }
            yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=headers, dont_filter=False)
