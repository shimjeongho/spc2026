from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader("./Javascript_Secure_Coding.pdf")
pages = loader.load()

print(f"PDF 페이지수: {len(pages)}\n")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)

chunks = splitter.split_documents(pages)
print(f"청킹 후 문서 갯수: {len(chunks)}\n")

first = chunks[0]
print(first.metadata)
print(first.page_content)
print('-' * 60)

first = chunks[50]
print(first.metadata)
print(first.page_content)

"""
PDF 페이지수: 159

청킹 후 문서 갯수: 153

{'producer': 'Hancom PDF 1.3.0.546', 'creator': 'Hwp 2020 11.0.0.8362', 'creationdate': '2024-04-01T17:52:07+09:00', 'author': 'TEST', 'moddate': '2024-04-01T17:52:07+09:00', 'pdfversion': '1.4', 'source': './Javascript_Secure_Coding.pdf', 'total_pages': 159, 'page': 1, 'page_label': '2'}
CONTENTS
PART 제1장 개요제1절 배경····················································································2제2절 왜 자바스크립트인가··························································4제3절 가이드 목적 및 구성·························································6
PART 제2장 시큐어코딩 가이드제1절 입력데이터 검증 및 표현················································101. SQL 삽입············································································102. 코드 삽입·············································································163. 경로 조작 및 자원 삽입······················································194. 크로스사이트 스크립트(XSS)··············································235. 운영체제 명령어 삽입··························································326. 위험한 형식 파일 업로드····················································357. 신뢰되지 않은 URL주소로 자동접속 연결·························388. 부적절한 XML 외부 개체 참조··········································409. XML 삽입············································································4310. LDAP 삽입········································································4611. 크로스사이트 요청 위조(CSRF)·······································5012. 서버사이드 요청 위조·······················································5613. 보안기능 결정에 사용되는 부적절한 입력값····················59
------------------------------------------------------------
{'producer': 'Hancom PDF 1.3.0.546', 'creator': 'Hwp 2020 11.0.0.8362', 'creationdate': '2024-04-01T17:52:07+09:00', 'author': 'TEST', 'moddate': '2024-04-01T17:52:07+09:00', 'pdfversion': '1.4', 'source': './Javascript_Secure_Coding.pdf', 'total_pages': 159, 'page': 54, 'page_label': '55'}
PART 제2장 시큐어코딩 가이드 ❘ 제1절 입력데이터 검증 및 표현
49
참고: 자바스크립트 기반 LDAP 데이터 처리 함수
1:2:3:4:5:6:7:8:9:10:11:12:13:14:15:16:17:19:20:21:22:23:24:25:26:27:28:29:30:31:32:33:34:35:36:37:38:
// (참고) ldapjs 패키지를 사용해 ldap 데이터를 처리하는 코드 예시로, 앞서 제시한 두 코드에서// 생략된 searchLDAP 함수의 전체 코드const ldap = require('ldapjs');const config = {  url: 'ldap://ldap.forumsys.com',  base: 'dc=example,dc=com',  dn: 'cn=read-only-admin,dc=example,dc=com',  password: 'password',};async function searchLDAP (search) {  const opts = {    filter: `(&(objectClass=${search}))`,    attributes: ['sn', 'cn', 'mail', 'telephonenumber', 'uid'],    scope: 'sub',  };  const users = [];  const client = ldap.createClient({ url: config.url });  return new Promise((resolve, reject) => {    client.bind(config.dn, config.password, (err) => {      if (err) {        console.log('LDAP bind error - ', err);      } else {        client.search(config.base, opts, (err, res) => {            res.on('searchEntry', (entry) => {            users.push(entry.object);          });          ...          res.on('end', (result) => {            console.log('status: ' + result.status);            resolve(users);          });        });      }    });  });}
"""