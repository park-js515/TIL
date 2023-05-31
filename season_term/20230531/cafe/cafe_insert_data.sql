use ssafyweb;

-- 사용자 등록
insert into user (user_id, user_name, password, email, role)
values ('admin', '관리자', '1234', 'admin@ssafy.com', 100);

insert into user (user_id, user_name, password, email, role)
values ('kimssafy', '김싸피', '1234', 'kimssafy@naver.com', 0);

insert into user (user_id, user_name, password, email, role)
values ('parkssafy', '박싸피', '1234', 'parkssafy@kakao.com', 0);

insert into user (user_id, user_name, password, email, role)
values ('goossafy', '구싸피', '9876', 'goossafy@google.com', 0);

insert into user (user_id, user_name, password, email, role)
values ('leessafy', '이싸피', '7777', 'leessafy@line.com',0);

commit;

-- 게시판 형식 등록 (관리자)

insert into board_type (btype_name)
values ('공지사항');

insert into board_type (btype_name)
values ('한줄게시판');

insert into board_type (btype_name)
values ('일반게시판');

insert into board_type (btype_name)
values ('답변형게시판');

insert into board_type (btype_name)
values ('앨범형게시판');

insert into board_type (btype_name)
values ('자료실게시판');

commit;

-- 카테고리 생성 (관리자)

insert into category (cname)
values ('싸피 8기');

insert into category (cname)
values ('싸피 9기');

insert into category (cname)
values ('싸피 10기');

commit;

-- 게시판 생성 (관리자)

-- 싸피 8기, '8기 공지', 공지사항
insert into board_list (bname, ccode, btype)
values ('8기 공지', 1, 1);

-- 싸피 8기, '와글와글', 일반게시판
insert into board_list (bname, ccode, btype)
values ('와글와글', 1, 3);

-- 싸피 8기, '출첵은필수!!', 한줄게시판
insert into board_list (bname, ccode, btype)
values ('출첵은필수!!', 1, 2);

-- 싸피 8기, '울반자랑하기', 앨범형게시판
insert into board_list (bname, ccode, btype)
values ('울반자랑하기', 1, 5);

-- 싸피 9기, '수다쟁이들 모임', 일반게시판
insert into board_list (bname, ccode, btype)
values ('수다쟁이들 모임', 2, 3);

-- 싸피 9기, '취준이 궁금해?', 답변형게시판
insert into board_list (bname, ccode, btype)
values ('취준이 궁금해?', 2, 4);

-- 싸피 9기, '소스 공유해요', 자료실게시판
insert into board_list (bname, ccode, btype)
values ('소스 공유해요', 2, 6);

-- 싸피 9기, '우리 캠퍼스가 짱!!', 앨범형게시판
insert into board_list (bname, ccode, btype)
values ('우리 캠퍼스가 짱!!', 2, 5);

-- 싸피 10기, '싸피오기전 이것만은 꼭!!', 공지사항
insert into board_list (bname, ccode, btype)
values ('싸피오기전 이것만은 꼭!!', 3, 1);

-- 싸피 10기, '싸피 시작? 두근두근', 일반게시판
insert into board_list (bname, ccode, btype)
values ('싸피 시작? 두근두근', 3, 3);

commit;

-- 싸피 9기, 'MBTI 공유', 앨범형게시판
insert into board_list (bname, ccode, btype)
values ('MBTI 공유', 2, 5);

commit;

-- 게시글 등록 (사용자)
-- 1, 8기 공지, 관리자, 안녕하세요, 출첵하세요
insert into board (user_id, subject, content, bcode)
values ('admin', '안녕하세요', '출첵하세요', 1);

-- 2, 수다쟁이들 모임, 김싸피, 오늘 점심 머에염??, 배고파요!!
insert into board (user_id, subject, content, bcode)
values ('kimssafy', '오늘 점심 머에염??', '배고파요!!', 5);

-- 3, 취준이 궁금해?, 이싸피, 삼전가고 싶어요., 어떤걸 준비해야 할까요?
insert into board (user_id, subject, content, bcode)
values ('leessafy', '삼전가고 싶어요.', '어떤걸 준비해야 할까요?', 6);

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (3, 3, 0, 0, 0, 0);

-- 4, 싸피오기전 이것만은 꼭!!, 관리자, 알고리즘 공부는 필수, 알고는 사전 학습하고 오면 좋아요.
insert into board (user_id, subject, content, bcode)
values ('admin', '알고리즘 공부는 필수', '알고는 사전 학습하고 오면 좋아요.', 9);

-- 5, 8기 공지, 관리자, 잡페어 시간에 졸지 말기, 두눈 크게 뜨고 좋은 기업 찾아요.
insert into board (user_id, subject, content, bcode)
values ('admin', '잡페어 시간에 졸지 말기', '두눈 크게 뜨고 좋은 기업 찾아요.', 1);

-- 6, 취준이 궁금해?, 김싸피, [3 답글] 알고리즘 잘해야 해요, 알고는 필수!!!
insert into board (user_id, subject, content, bcode)
values ('kimssafy', '[3 답글] 알고리즘 잘해야 해요', '알고는 필수!!!', 6);

update reboard
set step = step + 1
where step > 0
and group_no = 3;

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (6, 3, 1, 1, 3, 0);

update reboard
set reply = reply + 1
where article_no = 3;

-- 7, 취준이 궁금해?, 구싸피, [3 답글] CS도 잘해야 해요, 면접에서 물어볼걸요??
insert into board (user_id, subject, content, bcode)
values ('goossafy', '[3 답글] CS도 잘해야 해요', '면접에서 물어볼걸요??', 6);

update reboard
set step = step + 1
where step > 0
and group_no = 3;

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (7, 3, 1, 1, 3, 0);

update reboard
set reply = reply + 1
where article_no = 3;

-- 8, MBTI 공유, 박싸피, ENFJ, 나랑 같은사람?
insert into board (user_id, subject, content, bcode)
values ('parkssafy', 'ENFJ', '나랑 같은사람?', 11);

-- 9, 우리 캠퍼스가 짱!!, 이싸피, 대전캠 정말 이뻐용, 점심먹고 동산 한바뀌 같이 도실분 있나요?
-- 1, 9, 20230531, cam.png, cam.png
insert into board (user_id, subject, content, bcode)
values ('leessafy', '대전캠 정말 이뻐용', '점심먹고 동산 한바뀌 같이 도실분 있나요?', 8);

insert into album (article_no, save_folder, original_picture, save_picture)
values (last_insert_id(), '20230531', 'cam.png', 'cam.png');

-- 10, 취준이 궁금해?, 구싸피, 구글 최종면접인데 어떤걸 준비해야 할까요?, 냉무
insert into board (user_id, subject, content, bcode)
values ('goossafy', '구글 최종면접인데 어떤걸 준비해야 할까요?', '냉무', 6);

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (10, 10, 0, 0, 0, 0);

-- 11, 취준이 궁금해?, 박싸피, [10 답글] 구글 최종면접인데 어떤걸 준비해야 할까요?, 영어 ㅠㅠ
insert into board (user_id, subject, content, bcode)
values ('parkssafy', '[10 답글] 구글 최종면접인데 어떤걸 준비해야 할까요?', '영어 ㅠㅠ', 6);

update reboard
set step = step + 1
where step > 0
and group_no = 10;

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (11, 10, 1, 1, 10, 0);

update reboard
set reply = reply + 1
where article_no = 10;

-- 12, 취준이 궁금해?, 박싸피, [6 답글] 마자요 알고 엄청 물어보더라구요, 알고 CS 둘다 준비해야 할듯요
insert into board (user_id, subject, content, bcode)
values ('parkssafy', '[6 답글] 마자요 알고 엄청 물어보더라구요', '알고 CS 둘다 준비해야 할듯요', 6);

-- update reboard
-- set step = step + 1
-- where step > 
-- and group_no = ;

-- insert into reboard (article_no, group_no, depth, step, parent_no, reply)
-- values (, , , , , );

-- update reboard
-- set reply = reply + 1
-- where article_no = ;

-- 13, 취준이 궁금해?, 박싸피, [7 답글] 둘다 물어봐요, 알고 CS 둘다 준비해야 할듯요
insert into board (user_id, subject, content, bcode)
values ('parkssafy', '[7 답글] 둘다 물어봐요', '알고 CS 둘다 준비해야 할듯요', 6);

update reboard
set step = step + 1
where step > 1
and group_no = 3;

insert into reboard (article_no, group_no, depth, step, parent_no, reply)
values (13, 3, 2, 2, 7, 0);

update reboard
set reply = reply + 1
where article_no = 7;

commit;















